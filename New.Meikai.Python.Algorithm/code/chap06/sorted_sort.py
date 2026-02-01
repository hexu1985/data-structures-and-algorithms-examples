# 使用sorted函数排序

print('使用sorted函数排序')
num = int(input('元素个数：'))
x = [None] * num    # 创建一个元素个数为num的数组

for i in range(num):
    x[i] = int(input(f'x[{i}]：'))

# 对数组x进行升序排序
x = sorted(x)
print('已按升序排序。')
for i in range(num):
    print(f'x[{i}]＝{x[i]}')

# 对数组x进行降序排序
x = sorted(x, reverse=True)
print('已按降序排序。')
for i in range(num):
    print(f'x[{i}]＝{x[i]}')
