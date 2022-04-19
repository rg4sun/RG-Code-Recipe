'''
生成 handbook 的 markdown格式跳转链接
Presented By R.G. 2020.03.31
'''
import os
import re

# ROOT = os.getcwd() # 获取本地绝对路径了
ROOT = './'
things = os.listdir(ROOT)
# for i in things:
#     if re.findall('hand.*?md', i) == []:
#         things.remove(i); // 遍历i的同时删除i会导致问题，调试可以看到
# handbooks = [ i if re.findall('hand.*?md', i) == [] else None for i in things]
# 不好，还要处理 none
handbook = []
for i in things:
    if re.findall('hand.*?md', i) != []:
        handbook.append(i)
handbook.sort()

with open('./pathBook.md', 'w') as fp:
    for i in handbook:
        fp.write(
            '+ [**{}**]({})\n'.format(
                i[:-3], os.path.join(ROOT, i)
            )
        )

print('Done, result in ./pathBook.md')
