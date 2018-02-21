#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open('dreams_words_normal2.txt', 'r')
data = f.readlines()[1:]
f.close()

g = open('word_freq2.txt', 'r')
wf = g.readlines()[1:]
g.close()

id_dict = {}
for word in wf:
	w = word.strip('\n').split(',')
	id_dict[w[1]] = w[0]

out = open('edges.txt', 'w')
out.write('source,target,type\n')

line0 = data[0]
els0 = line0.strip('\n').split(',')
num0 = els0[0]
word0 = els0[2]
for line in data[1:]:
	els = line.strip('\n').split(',')
	num = els[0]
	word = els[2]
	if num == num0:
		try:
			id0 = id_dict[word0]
		except KeyError:
			print word0
		try:	
			id1 = id_dict[word]
		except KeyError:
			print word	
		out.write(id0 + ',' + id1 + ',directed\n')
	(num0, word0) = (num, word)

out.close()