#!/usr/bin/env python3

import os

name_dict = dict.fromkeys(open('./name/names').readlines(), 0)
name_list_done = os.listdir('./') + os.listdir('name')


#print(name_dict)
#print(name_list_done)
for name in name_dict:
	for j in name_list_done:
		if name.strip() in j:
			name_dict[name] += 1


没交 = []
交了 = []
for name, i in name_dict.items():
	if i == 0:
		没交.append(name.strip())
	else:
		for temp in range(i):
			交了.append(name.strip())
		if i > 1:
			print(name.strip())


print('没交还有:',len(没交),'人')
for i in 没交:
	print(i, ' ', end='' )
print()
print()
print()
print()



print('交了:',len(交了))
for i in 交了:
	print(i, ' ', end='' )
print()
