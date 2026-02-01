# 读取5名学生的成绩后，输出总分和平均分

print('求5名学生成绩的总分和平均分。')

tensu1 = int(input('第1名学生的成绩：'))
tensu2 = int(input('第2名学生的成绩：'))
tensu3 = int(input('第3名学生的成绩：'))
tensu4 = int(input('第4名学生的成绩：'))
tensu5 = int(input('第5名学生的成绩：'))

total = 0
total += tensu1
total += tensu2
total += tensu3
total += tensu4
total += tensu5

print(f'总分为{total}分。')
print(f'平均分为{total / 5}分。')
