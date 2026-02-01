# 通过KMP算法进行字符串查找

def kmp_match(txt: str, pat: str) -> int:
    """通过KMP算法进行字符串查找"""
    pt = 1          # 遍历txt的游标
    pp = 0          # 遍历pat的游标
    skip = [0] * (len(pat) + 1)     # 跳转表

    # 创建跳转表
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]

    # 查找
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

    return pt - pp if pp == len(pat) else -1

if __name__ == '__main__':
    s1 = input('文本串：')    # 文本字符串
    s2 = input('模式串：')    # 模式字符串

    idx = kmp_match(s1, s2)     # 通过KMP算法从s1字符串中查找s2字符串

    if idx == -1:
        print('文本串中不包含模式串。')
    else:
        print(f'第{(idx + 1)}个字符匹配成功。')
