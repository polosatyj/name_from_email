# -*- coding: utf-8 -*-
import string
f1 = open('emailes.txt',  'r')
f2 = open('names.txt','r')
f3 = open('named_emails.csv','w')
res = ''
chekthis = ''
names = []
# грузим имена
for line in f2:
	names.append(line)
f2.close()
names.sort()
names.reverse()
# сравниваем начало эмайла с именем
for line in f1:
	line.lower()
	chekthis = line.split('@')[0]
	chekthis.strip('._-0123456789')
	for x in names:
		if chekthis.startswith(x.split()[0]):
			res = '%s;%s' % (x.split()[1], line)
			f3.write(res)
			print x.split()[0], line.rstrip()
			chekthis = ''
			break
f1.close()
f3.close()