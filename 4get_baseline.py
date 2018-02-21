#!/usr/bin/env python
# -*- coding: utf-8 -*-

from string import digits
import math
import heapq

f = open('dreams_words_normal.txt', 'r')
data = f.readlines()[1:]
f.close()

word_dict = {}
word_counter = 0

line_counter = 0

for line in data:
	if line_counter % 200 == 0:
		print line_counter
	line_counter += 1
	els = line.strip('\n').split(',')
	word = els[2]
	word_counter += 1

	if word in word_dict:
		word_dict[word] += 1
	else:
		word_dict[word] = 1

wf = open("word_freq.txt", "w")
wf.write("word,number_of_occurences,frequency,log_frequency\n")
for w in word_dict.keys():
	num = word_dict[w]
	freq = float(num)/word_counter
	log_freq = math.log(freq)
	wf.write(w + "," + str(num) + "," + str(freq) +"," + str(log_freq) + "\n")

wf.close()
print word_counter