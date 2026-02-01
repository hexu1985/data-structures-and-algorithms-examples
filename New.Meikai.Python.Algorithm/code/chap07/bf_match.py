# 通过暴力匹配算法进行字符串查找

def bf_match(txt: str, pat: str) -> int:
    """通过暴力匹配算法进行字符串查找"""
    pt = 0          # 遍历txt的游标
    pp = 0          # 遍历pat的游标

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0

    return pt - pp if pp == len(pat) else -1

if __name__ == '__main__':
    s1 = input('文本串：')    # 文本字符串
    s2 = input('模式串：')    # 模式字符串

    idx = bf_match(s1, s2)      # 通过暴力匹配算法从s1字符串中查找s2字符串

    if idx == -1:
        print('文本串中不包含模式串。')
    else:
        print(f'第{(idx + 1)}个字符匹配成功。')
