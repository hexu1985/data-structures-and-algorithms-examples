# 将读取的十进制数转换为二进制数～三十六进制数后输出

def card_conv(x: int, r: int) -> str:
    """将整数x转换为r进制数后，再以字符串的形式输出"""

    d = ''        # 转换后的字符串
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(str(x))     # 转换前的位数

    print(f'{r:2} | {x:{n}d}')
    while x > 0:
        print('   +' + (n + 2) * '-')
        if x // r:
            print(f'{r:2} | {x // r:{n}d} … {x % r}')
        else:
            print(f'     {x // r:{n}d} … {x % r}')

        d += dchar[x % r]    # 提取相应字符后连接
        x //= r

    return d[::-1]           # 反转后返回

if __name__ == '__main__':
    print('对十进制数进行进制转换。')

    while True:
        while True:                             # 读取非负整数
            no = int(input('要转换的非负整数：'))
            if no > 0:
                break

        while True:                             # 读取2~36的整数
            cd = int(input('转换成几进制数（2-36）：'))
            if 2 <= cd <= 36:
                break

        print(f'用{cd}进制数表示为{card_conv(no, cd)}。')

        retry = input("是否再转换一次（Y表示是／N表示否）：")
        if retry in {'N', 'n'}:
            break
