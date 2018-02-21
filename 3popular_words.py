#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator

f = open('dreams_words_normal.txt', 'r')
data = f.readlines()[1:]
f.close()

big_25 = ['Москва','Санкт-Петербург','Новосибирск','Екатеринбург','Нижний Новгород','Самара','Омск','Казань','Челябинск',
'Ростов-на-Дону','Уфа','Волгоград','Пермь','Красноярск','Воронеж','Саратов','Краснодар','Тольятти','Ижевск','Ульяновск',
'Барнаул','Владивосток','Ярославль','Иркутск','Тюмень']

city_dict = {}
region_dict = {}

for line in data:
    #print line
    els = line.strip('\n').split(',')
    num = els[0]
    word = els[1]
    normal_word = els[2]
    part_of_speech = els[3]
    city = els[4]
    region = els[5]
    if city in big_25:
        if city not in city_dict:
            city_dict[city] = {}
            city_dict[city][normal_word] = 1
            city_dict[city]['sum'] = 1
        else:
            if normal_word not in city_dict[city]:
                city_dict[city][normal_word] = 1
                city_dict[city]['sum'] += 1
            else:
                city_dict[city][normal_word] += 1
                city_dict[city]['sum'] += 1
    if region not in region_dict:
        region_dict[region] = {}
        region_dict[region][normal_word] = 1
        region_dict[region]['sum'] = 1
    else:
        if normal_word not in region_dict[region]:
            region_dict[region][normal_word] = 1
            region_dict[region]['sum'] += 1
        else:
            region_dict[region][normal_word] += 1
            region_dict[region]['sum'] += 1

out_city = open('popular_words_city.txt', 'w')
out_region = open('popular_words_region.txt', 'w')
#out.write('dream_num,word,normal_word,part_of_speech,city,region\n')
for city in city_dict:
    total_words = float(city_dict[city]['sum'])
    city_words = city_dict[city]
    sorted_words = sorted(city_words.items(), key=operator.itemgetter(1))
    best_5 = sorted_words[-6:][::-1]
    for tup in best_5:
        out_city.write(city+','+tup[0]+','+str(tup[1])+','+str(tup[1]/total_words)+'\n')
        
for region in region_dict:
    total_words = float(region_dict[region]['sum'])
    region_words = region_dict[region]
    sorted_words = sorted(region_words.items(), key=operator.itemgetter(1))
    best_5 = sorted_words[-6:][::-1]
    for tup in best_5:
        out_region.write(region+','+tup[0]+','+str(tup[1])+','+str(tup[1]/total_words)+'\n')

out_city.close()
out_region.close()
    
