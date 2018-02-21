#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open('test_data_dreams.txt', 'r')
data = f.readlines()[1:]
f.close()

g = open('cities_regions_pop.txt', 'r')
regions = g.readlines()[1:]
g.close()

region_dict = {}
for line in regions:
    els = line.strip('\n').split('\t')
    city = els[0]
    code = els[1]
    region = els[2]
    center = els[3]
    pop = els[4]
    region_dict[city] = (code, region, center, pop)
#cities_wo_regions = open('cities_without_regions.txt', 'w')
cities_wo_regions_dict = {}
city_dict = {}
out = open('dreams_words.txt', 'w')
out.write('dream_num,word,city,region\n')
for line in data:
    els = line.strip('\n').split('\t')
    num = els[0]
    phrase = els[1]
    city = els[2]
    if city in city_dict:
        city_dict[city] += 1
    else:
        city_dict[city] = 1
    phrase_upd = phrase.replace(',', '').replace('?', '').replace('снится', '').replace('сниться', '').replace('во сне', '').replace('сонник', '')
    words = phrase_upd.split(' ')
    for word in words:
        if word in ['я'] or len(word) > 2: #слова длиннее 1 буквы или 2 знаков юникода
            try:
                region = region_dict[city][1]
                out.write(num + ',' + word + ',' + city + ',' + region + '\n')
            except KeyError:
                out.write(num + ',' + word + ',' + city + ',-\n')
                #if city not in cities_wo_regions_dict:
                    #print city
                    #cities_wo_regions_dict[city] = 1
                #else:
                    #cities_wo_regions_dict[city] += 1
            
out.close()

out_city = open('city_count.txt', 'w')
out_city.write('city,dreams,region,center,pop\n')
for city in sorted(city_dict):
    if city in region_dict:
        info = region_dict[city]
        out_city.write(city + ',' + str(city_dict[city]) + ',' + info[1] + ',' + info[2] + ',' + info[3] + '\n')
    else:
        out_city.write(city + ',' + str(city_dict[city]) + ',-,-,-\n')
out_city.close()

#for city in cities_wo_regions_dict:
    #print city + ',' + str(cities_wo_regions_dict[city])


