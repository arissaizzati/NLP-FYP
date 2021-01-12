# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 14:54:44 2020

@author: User
"""

from tatabahasa import *
#from nltk.tokenize import word_tokenize
import malaya
model = malaya.stem.deep_model()

#text = 'Bahasa Melayu mempunyai berbagai-bagai jenis ayat untuk menyatakan maksud'
#word = word_tokenize(text) #to get how many words in the list (sentence)
#len_word = len(word)
#print(len(word))
tokenizer = malaya.preprocessing.SocialTokenizer().tokenize

def word2ngrams(text, exact=True):
    
    #word_count = 0 #utk loop how many elems in the sentence
    #while word_count <= len_word:
    
    n = len(text) #TO GET THE NUM OF CHARS IN THE WORD
    dict_ngram = [] #dict for n gram
    #found_word = [] #words from dict_ngram that are found from the tatabahasa dictionary
    
    i=4
    while i<=n:
        n_text = (["".join(j) for j in zip(*[text[i:] for i in range(i)])])
        #dict_ngram.append(n_text)
        dict_ngram.insert(0, n_text) #Insert new n gram words to the front of list
        i=i+1
    #print(dict_ngram)
    #wordSearch(dict_ngram)

#def wordSearch(dict_ngram):

    flatten_list = [j for sub in dict_ngram for j in sub] #to convert 2d array to 1d
    len_flatten_list = len(flatten_list)
    
    ori_word = flatten_list[:1]
    #print('ori_word:', ori_word)
    
    found_tatabahasa = []
    
    #print('flatten_list=', len(flatten_list))
    #find_word = flatten_list[:1]
    
    i = 0
    while i < len_flatten_list:
        find_word = flatten_list[:1]
        #print(find_word)
        
        first_char = (', '.join(find_word))[0]
        #print('first_char:', first_char)
        
        if len(flatten_list) != 0: 
            flatten_list.pop(0)
        i=i+1
        
        
        if first_char == 'a':
            #print('A')
            if (', '.join(find_word)) in A:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
                
        if first_char == 'b':
            #print('A')
            if (', '.join(find_word)) in B:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
                
        if first_char == 'c':
            #print('A')
            if (', '.join(find_word)) in C:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
                
        if first_char == 'd':
            #print('A')
            if (', '.join(find_word)) in D:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
                
        if first_char == 'e':
            #print('A')
            if (', '.join(find_word)) in E:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
        
        if first_char == 'f':
            #print('A')
            if (', '.join(find_word)) in F:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
        
        if first_char == 'g':
            #print('A')
            if (', '.join(find_word)) in G:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
        
        if first_char == 'h':
            #print('A')
            if (', '.join(find_word)) in H:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
        
        if first_char == 'i':
            #print('A')
            if (', '.join(find_word)) in I:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
                
        if first_char == 'j':
            #print('A')
            if (', '.join(find_word)) in J:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
                
        if first_char == 'k':
            #print('A')
            if (', '.join(find_word)) in K:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
                
        if first_char == 'l':
            #print('A')
            if (', '.join(find_word)) in L:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
        
        if first_char == 'm':
            #print('A')
            if (', '.join(find_word)) in M:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
        
        if first_char == 'n':
            #print('A')
            if (', '.join(find_word)) in N:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
        
        if first_char == 'o':
            #print('A')
            if (', '.join(find_word)) in O:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
                
        if first_char == 'p':
            #print('A')
            if (', '.join(find_word)) in P:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
                
        if first_char == 'q':
            #print('A')
            if (', '.join(find_word)) in Q:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
                
        if first_char == 'r':
            #print('A')
            if (', '.join(find_word)) in R:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
                
        if first_char == 's':
            #print('A')
            if (', '.join(find_word)) in S:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
        
        if first_char == 't':
            #print('A')
            if (', '.join(find_word)) in T:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
                
        if first_char == 'u':
            #print('A')
            if (', '.join(find_word)) in U:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
        
        if first_char == 'v':
            #print('A')
            if (', '.join(find_word)) in V:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
                
        if first_char == 'w':
            #print('A')
            if (', '.join(find_word)) in W:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
                
        if first_char == 'x':
            #print('A')
            if (', '.join(find_word)) in X:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
                
        if first_char == 'y':
            #print('A')
            if (', '.join(find_word)) in Y:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
        
        if first_char == 'z':
            #print('A')
            if (', '.join(find_word)) in Z:
                found_tatabahasa.append(', '.join(find_word))
                #print("FOUND IN TATABAHASA", (', '.join(find_word)))
                
        
    #print(found_tatabahasa)
    
    if not found_tatabahasa: #found_tatabahasa is empty
        #print('CALL MALAYA')
        malaya_stemmed = model.stem((', '.join(ori_word))) #LEMMATIZATION / STEMMING BUT CALL MALAYA
        #print (malaya_stemmed)
        return malaya_stemmed
        #print_sentence_stemmed.append(malaya_stemmed)
    else:
        #TO GET LONGEST MATCH
        longest_match = found_tatabahasa[:1]
        longest_match = (', '.join(longest_match))
        #print(longest_match)
        return longest_match
        #print_sentence_stemmed.append(longest_match)

def ngram_stem_malaya(word):
    word2 = tokenizer(word)
    print_sentence_stemmed = []
    #word2ngrams(text)
    if word2:
        for t in word2:
            word2ngrams(t.lower())
            #print (t)
            print_sentence_stemmed.append(word2ngrams(t.lower()))
            #print(print_sentence_stemmed)

    listToStr = ' '.join([str(elem) for elem in print_sentence_stemmed]) 
    #print(listToStr)
    return listToStr


#text = 'Bahasa Melayu mempunyai berbagai-bagai jenis ayat untuk menyatakan maksud'
#text = 'selangkah'

#text = ''''ISU memartabatkan bahasa Melayu kembali bergoncang susulan tindakan seorang menteri yang didakwa mengeluarkan kenyataan rasmi dalam bahasa Mandarin.
#Perbuatan itu mengundang kecaman ramai pencinta bahasa meskipun kenyataan rasmi dalam bahasa kebangsaan dan bahasa Inggeris turut juga dikeluarkan.
#Ramai mempersoalkan apa rasionalnya kenyataan rasmi dalam bahasa Mandarin masih perlu dikeluarkan juga.
#'''

#word = word_tokenize(text)
#print_sentence_stemmed = []

#if word:
 #   for t in word:
  #      word2ngrams(t.lower())
        #print (t)
   #     print_sentence_stemmed.append(word2ngrams(t.lower()))
        #print(print_sentence_stemmed)

#listToStr = ' '.join([str(elem) for elem in print_sentence_stemmed]) 
#print(listToStr)