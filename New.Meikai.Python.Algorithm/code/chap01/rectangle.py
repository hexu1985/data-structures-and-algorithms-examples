# 枚举边长为整数且面积为area的矩形的边长

area = int(input('面积是：'))

for i in range(1, area + 1):
    if i * i > area: break
    if area % i : continue
    print(f'{i}×{area // i}')
