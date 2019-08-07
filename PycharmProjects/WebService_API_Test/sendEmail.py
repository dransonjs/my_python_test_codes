# coding:utf-8
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from selenium import webdriver
from PIL import Image

from email.mime.image import MIMEImage
from run import report_path, img_path


def SendMail(sender, receivers, mail_pass, content, file, image, cc_mail=None):
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器

    # 构造一个MIMEMultipart对象代表邮件本身
    message = MIMEMultipart()
    message.attach(MIMEText(content, 'html', 'utf-8'))  # 正文内容   plain代表纯文本,html代表支持html文本

    message['From'] = sender
    message['To'] = ','.join(receivers)  # 与真正的收件人的邮箱不是一回事
    message['Cc'] = ','.join(cc_mail)

    subject = 'Python自动邮件-%s' % time.ctime()
    message['Subject'] = subject  # 邮件标题

    # 添加文件到附件
    with open(file, 'rb') as f:
        # MIMEBase表示附件的对象
        mime = MIMEBase('text', 'txt', filename=file)
        # filename是显示附件名字
        mime.add_header('Content-Disposition', 'attachment', filename=file)
        # 获取附件内容
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        # 作为附件添加到邮件
        message.attach(mime)

    with open(image, 'rb') as f:
        # 图片添加到附件
        mime = MIMEBase('image', 'image', filename=image)
        mime.add_header('Content-Disposition', 'attachment', filename=image)
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        message.attach(mime)

    # 将图片显示在正文
    with open(image, 'rb') as f:
        # 图片添加到正文
        msgImage = MIMEImage(f.read())
    #     # 定义图片ID
    msgImage.add_header('Content-ID', '<image1>')
    message.attach(msgImage)

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(sender, mail_pass)
        smtpObj.sendmail(sender, receivers + cc_mail, str(message))  # message.as_string()
        smtpObj.quit()
        u"邮件发送成功"
    except smtplib.SMTPException as e:
        raise e


def capture(url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)  # Load page
    #     #先将页面的滚动条拖到最下方，再拖回顶部，然后才截图。这样的好处是避免页面下方有一些延迟加载的内容
    driver.execute_script("""
    (function () {
      var y = 0;
      var step = 100;
      window.scroll(0, 0);

      function f() {
        if (y < document.body.scrollHeight) {
          y += step;
          window.scroll(0, y);
          setTimeout(f, 50);
        } else {
          window.scroll(0, 0);
          document.title += "scroll-done";
        }
      }

      setTimeout(f, 1000);
    })();
  """)

    for i in range(30):
        if "scroll-done" in driver.title:
            break
        time.sleep(1)

    filename = img_path
    # 截屏
    driver.save_screenshot(filename)

    element = driver.find_element_by_xpath('//*[@id="title"]')  # 报告描述
    # 获取元素上下左右的位置
    left = element.location['x']
    top = element.location['y']

    b = driver.find_element_by_xpath('//*[@id="header_row"]')  # table上方

    right = b.location['x'] + b.size['width']
    bottom = b.location['y']
    # 打开刚才的截图
    im = Image.open(filename)
    # 截取对应位置
    im = im.crop((left, top, right, bottom))
    # 保存覆盖原有截图
    im.save(filename)
    driver.quit()


if __name__ == "__main__":
    from Tools.get_path import *

    filepath = 'file:///' + report_path
    capture(filepath)

    sender = '70xxxxx379@qq.com'  # 用户名与发送方
    receivers = ['70xxxxx379@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    cc_mail = ['1619xxxxx@qq.com']  # 抄送人

    # 口令,QQ邮箱是输入授权码，在qq邮箱设置 里用验证过的手机发送短信获得，不含空格
    mail_pass = "nswezlakxxevbdib"

    # htmlf = open(r'F:\mle_auto\web\MLE_UI\result.html', encoding='utf-8')
    # content = htmlf.read()
    # index_table = content.find('<table')
    # index_table_end = content.find('</table>')
    # content = content.replace(content[index_table:index_table_end], '')

    content = '''测试报告
            <h1>测试</h1>
            <h2 style="color:red">仅用于测试</h1>
            <a href="http://www.runoob.com/python/python-email.html">晋商1.0版本</a><br>
            <p>测试结果如下：详情请查看附件</p>
            <p><img src="cid:image1"></p>
          '''
    file = report_path
    image = img_path
    SendMail(sender, receivers, mail_pass, content, file, image, cc_mail)
