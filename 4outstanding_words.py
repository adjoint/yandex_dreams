#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv, copy
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
	return nck(n,k) * math.pow(p,k) * math.pow((1-p),(n-k))

def log_binom(k,n,p):
	log = 0
	for i in range(n-k+1,n+1):
		log += math.log(i)
	for j in range(1,k+1):
		log -= math.log(j)
	return log + k*math.log(p) + (n-k)*math.log(1-p)
#5 город 6 регион 7 слово
f = open('dreams_words_normal.txt', 'r')
data = f.readlines()[1:]
f.close()
regions = []
"""for line in data:
    els = line.strip('\n').split(',')
    num = els[0]
    region = els[5]
    if region not in regions:
        regions.append(region)"""
#print data[:10]
big_cities = ['Москва','Санкт-Петербург','Новосибирск','Екатеринбург','Нижний Новгород','Самара','Омск','Казань','Челябинск',
'Ростов-на-Дону','Уфа','Волгоград','Пермь','Красноярск','Воронеж','Саратов','Краснодар','Тольятти','Ижевск','Ульяновск',
'Барнаул','Владивосток','Ярославль','Иркутск','Тюмень']
#print big_cities[:1]
out = open("outstanding_cities.txt", "w")
for s in big_cities:
    print s
    rest_word_counter = 0    
    rest_word_dict = {}
    for line in data:
        els = line.strip('\n').split(',')
        word = els[2]
        city = els[4]       
        rest_word_counter += 1
        if word in rest_word_dict:
            rest_word_dict[word] += 1
        else:
			rest_word_dict[word] = 1
        
for s in big_cities:
    print s
    hit_word_counter = 0
    hit_word_dict = {}
    res_word_dict = {}
    for line in data:
        els = line.strip('\n').split(',')
        word = els[2]
        city = els[4]
        if city in [s]:
            hit_word_counter += 1
            if word in hit_word_dict:
                hit_word_dict[word] += 1
            else:
				hit_word_dict[word] = 1
	for word in hit_word_dict.keys():
		if True: #placeholder for some condition
			hit_num = hit_word_dict[word]
			#if hit_num <10:
				#continue
			hit_prob = float(hit_num)/hit_word_counter
			if word in rest_word_dict and rest_word_dict[word]>=50:
				rest_num = rest_word_dict[word]
				rest_prob = float(rest_num)/rest_word_counter
				log_hit_prob = math.log(hit_prob)
				log_rest_prob = math.log(rest_prob)
				
				if log_hit_prob >= log_rest_prob:
					log_prob = log_binom(hit_num, hit_word_counter, rest_prob)
					res_word_dict[word] = log_prob
				else:
					res_word_dict[word] = 2
			else:
				res_word_dict[word] = 2
	best = heapq.nsmallest(20, res_word_dict, key=res_word_dict.get)
    for b in best:
        """try:
            i = rest_word_dict[b]
        except KeyError:
            rest_word_dict[b] = 0
            print b.decode('utf8')"""
        out.write(s + "," + 
		
		b + "," +
		
		str(hit_word_dict[b])+","+
		
		str(hit_word_counter)+","+
		
		str(rest_word_dict[b])+","+
		
		str(rest_word_counter)+"\n")
		

out.close()