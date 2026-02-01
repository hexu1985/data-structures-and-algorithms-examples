# 查找字符串（find系列方法）

txt = input('字符串txt：')
ptn = input('字符串ptn：')

c = txt.count(ptn)

if c == 0:                                              # 不包含
    print('txt中不包含ptn。')
elif c == 1:                                            # 只包含1个
    print('ptn在txt中的索引：', txt.find(ptn))
else:                                                   # 包含2个或多个
    print('ptn在txt中的第一个索引：', txt.find(ptn))
    print('ptn在txt中的最后一个索引：', txt.rfind(ptn))
