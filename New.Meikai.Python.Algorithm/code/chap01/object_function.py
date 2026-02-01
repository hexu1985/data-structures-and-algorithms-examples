# 在函数内部和外部定义的变量和对象
# 输出对象和变量的标识符

n = 1            # 全局变量（在函数内部和外部均可使用）

def put_id():
    x = 1        # 局部变量（仅在函数内部使用）
    print(f'id(x) = {id(x)}')

print(f'id(1) = {id(1)}')
print(f'id(n) = {id(n)}')
put_id()
