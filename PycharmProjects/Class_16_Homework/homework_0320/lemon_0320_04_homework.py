# 把website = 'http://www.python.org'中的python字符串取出来
website = 'http://www.python.org'
print(website[website.find('python'):website.index('.org')])