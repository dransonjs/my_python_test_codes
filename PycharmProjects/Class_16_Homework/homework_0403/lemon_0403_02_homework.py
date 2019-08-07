# 用户输入考试成绩，当分数高于90（包含90）时打印A；
# 否则如果分数高于80（包含80）时打印B；
# 否则如果分数高于70（包含70）时打印C；
# 否则如果分数高于60（包含60）时打印D；
# 其他情况就打印E

score = int(input('输入考试成绩：'))

if 100 >= score >= 0:
    if 100 >= score >= 90:
        print('A')
    elif 90 > score >= 80:
        print('B')
    elif 80 > score >= 70:
        print('C')
    elif 70 > score >= 60:
        print('D')
    else:
        print('E')
else:
    print('请输入正常的分数值！')