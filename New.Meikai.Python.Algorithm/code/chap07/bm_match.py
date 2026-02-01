# 通过Boyer-Moore算法进行字符串查找（支持0～255个字符）

def bm_match(txt: str, pat: str) -> int:
    """通过Boyer-Moore算法进行字符串查找"""
    skip = [None] * 256     # 跳转表

    # 创建跳转表
    for pt in range(256):
        skip[pt] = len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1

    # 查找
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp \
              else len(pat) - pp

    return -1

if __name__ == '__main__':
    s1 = input('文本串：')    # 文本字符串
    s2 = input('模式串：')    # 模式字符串

    idx = bm_match(s1, s2)      # 通过Boyer-Moore算法从s1字符串中查找s2字符串

    if idx == -1:
        print('文本串中不包含模式串。')
    else:
        print(f'第{(idx + 1)}个字符匹配成功。')
