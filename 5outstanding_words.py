#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator
import math
import heapq
import sys

def nck(n, r):
	r = min(r, n-r)
	if r == 0: return 1
	numer = reduce(operator.mul, xrange(n, n-r, -1))
	denom = reduce(operator.mul, xrange(1, r+1))
	return numer//denom

def binom(k,n,p):
	a = nck(n,k)
	b = math.pow(p,k)
	c = math.pow((1-p),(n-k))
	d = b*c#/100000
	return a*d

f = open('dreams_words_normal.txt', 'r')
data = f.readlines()[1:]
f.close()

g = open('word_freq.txt', 'r')
wf = g.readlines()[1:]
g.close()

h = open('regions.txt', 'r')
wh = h.readlines()
h.close

freq_dict = {}
occur_dict = {}
for word in wf:
	w = word.strip('\n').split(',')
	freq_dict[w[1]] = math.exp(float(w[4]))
	occur_dict[w[1]] = int(w[2])
#print freq_dict

regions = []
for line in wh:
	r = line.strip('\n')
	regions.append(r)

big_cities = ['Москва','Санкт-Петербург','Новосибирск','Екатеринбург','Нижний Новгород','Самара','Омск','Казань','Челябинск',
'Ростов-на-Дону','Уфа','Волгоград','Пермь','Красноярск','Воронеж','Саратов','Краснодар','Тольятти','Ижевск','Ульяновск',
'Барнаул','Владивосток','Ярославль','Иркутск','Тюмень']


word_counter = 0
line_counter = 0
out = open("outstanding_regions.txt", "w")
#out.write('city,word,prob_of_observed,observed_prob,word_hit,words,expected_prob\n')
for s in regions:
	word_dict = {}
	prob_dict = {}
	obs_prob_dict = {}
	for line in data:
		els = line.strip('\n').split(',')
		word = els[2]
		try:
			city = els[5]
			line_counter += 1
			if line_counter % 500 == 0:
				print line_counter
			if city in [s]:
				word_counter += 1
				if word in word_dict:
					word_dict[word] += 1
				else:
					word_dict[word] = 1		
		except IndexError:
			i = 1	
	for word in word_dict.keys():
		num = word_dict[word]
		if True:#num >= 20:
			freq = float(num)/word_counter
			if word in freq_dict:# and occur_dict[word]>=20:
				base_prob = freq_dict[word]
				obs_prob = float(num)/word_counter
				obs_prob_dict[word] = obs_prob
				if obs_prob >= base_prob:
					try:
						prob = binom(num, word_counter, base_prob)
					except OverflowError:
						print num
						print word_counter
						print base_prob
						break
					if prob > 0:
						#log_prob = math.log(prob)
						prob_dict[word] = prob
					#print 1111
					else:
						prob_dict[word] = sys.maxint
					#print 2222
				else:
					prob_dict[word] = sys.maxint
				#print 3333
			else:
				prob_dict[word] = sys.maxint
			#print 4444
	best = heapq.nsmallest(10, prob_dict, key=prob_dict.get)
	for b in best:

		out.write(s + "," + 
	
		b + "," +
		
		str(prob_dict[b])+","+

		str(obs_prob_dict[b])+","+
		
		str(word_dict[b])+","+
		
		str(word_counter)+","+

		str(freq_dict[b])+","+

		str(occur_dict[b])+"\n")


out.close()

