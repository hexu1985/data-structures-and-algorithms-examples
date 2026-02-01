# 使用enumerate函数遍历列表中的所有元素（从1开始计数）

x = ('John', 'George', 'Paul', 'Ringo')

for i, name in enumerate(x, 1):
    print(f'第{i}个 = {name}')
