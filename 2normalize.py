#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymorphy2
morph = pymorphy2.MorphAnalyzer()

f = open('dreams_words.txt', 'r')
data = f.readlines()[1:]
f.close()

#('dream_num,word,city,region\n')

out = open('dreams_words_normal.txt', 'w')
out.write('dream_num,word,normal_word,part_of_speech,city,region\n')

for line in data:
    els = line.strip('\n').split(',')
    num = els[0]
    word = els[1]
    city = els[2]
    region = els[3]
    p = morph.parse(unicode(word, 'utf8'))[0] #0 - первый, самый вероятный вариант ответа, например, "стали" скорее глагол, чем существительное
    normal_word = p.normal_form
    part_of_speech = p.tag.POS
    pos = '-'
    try:
        if 'VERB' in p.tag.POS or 'INFN' in p.tag.POS:
            pos = 'verb'
        elif 'NOUN' in p.tag.POS:
            pos = 'noun'
        elif 'ADJF' in p.tag.POS:
            pos = 'adj'
        elif 'ADVB' in p.tag.POS:
            pos = 'adv'
    except TypeError:
        i = 1
    #print word
    #print normal_word
    #print part_of_speech
    out.write(num+','+word+','+normal_word.encode('utf8')+','+pos+','+city+','+region+'\n')
    """print type(normal_word)
    out.write(num)
    out.write(word)
    out.write(normal_word.encode('utf8'))
    out.write(part_of_speech)
    out.write(city)
    out.write(region)"""
    
out.close()

