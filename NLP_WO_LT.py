# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 17:30:27 2020

@author: User
"""



import streamlit as st
import malaya

from nltk.tokenize import sent_tokenize
import string

from ngram_malaya import ngram_stem_malaya

st.header("DEMO FYP PART1 - APPLYING NATURAL LANGUAGE PROCESSING ON THE LYRICS")

tokenizer = malaya.preprocessing.SocialTokenizer().tokenize
corrector = malaya.spell.probability()
normalizer = malaya.normalize.normalizer(corrector)
stemmer = malaya.stem.deep_model()
transformer_small = malaya.translation.en_ms.transformer(model = 'small')

#----------------------------------------------------------------------
#---------------------****UPLOAD LYRICS*****-------------------------
#----------------------------------------------------------------------
st.subheader("Upload Lyrics")
st.set_option('deprecation.showfileUploaderEncoding', False)
file1 =[]
file2 = []

txt = st.file_uploader("Choose a file")

if txt is not None:
    
    #file_details = {"filename":txt.name}
    #st.write(file_details)
    #file2.append(txt)
    for line in txt: 
        st.write(line.strip()) 
        file1.append(line)
        file2.append(line)

    
    
    

filtered_sentence = [] 


malay_stopwords = ["ada", "inikah", "sampai", "adakah", "inilah", "sana", "adakan", "itu", "adalah",
"itukah", "adanya", "itulah", "saya", "adapun","jadi", "se", "agak", 
"seandainya", "agar", "sebab", "akan", "jika", "sebagai", "aku", "jikalau",
"sebagaimana", "akulah", "jua", "sebanyak", "akupun", "juapun", "sebelum", "al", "juga",
"sebelummu", "alangkah", "kalau", "sebelumnya", "allah", "kami", "sebenarnya", "amat",
"kamikah", "secara", "antara", "kamipun", "sedang", "antaramu", "kamu", "sedangkan", "antaranya",
"kamukah", "sedikit", "apa", "kamupun", "sedikitpun", "apa-apa", "katakan", "segala", "apabila",
"ke", "sehingga", "apakah", "kecuali", "sejak", "apapun", "kelak", "sekalian", "atas", "kembali",
"sekalipun", "atasmu", "kemudian", "sekarang", "atasnya", "kepada", "sekitar", "atau", "kepadaku",
"selain", "ataukah", "kepadakulah",  "ataupun", "kepadamu", "selama", "bagaimana", "kepadanya",
"selama-lamanya", "bagaimanakah", "kepadanyalah", "seluruh", "bagi", "kerana", "seluruhnya", "bagimu",
"kerananya", "sementara", "baginya", "kesan", "semua", "bahawa", "ketika", "semuanya", "bahawasanya", "kini",
"semula", "bahkan", "kita", "senantiasa", "bahwa", "ku", "sendiri", "banyak", "kurang", "sentiasa", "banyaknya", "lagi",
"seolah", "barangsiapa", "lain", "seolah-olah", "bawah", "lalu", "seorangpun", "beberapa", "lamanya", "separuh",
"begitu", "langsung", "sepatutnya", "begitupun", "lebih", "seperti", "belaka", "maha", "seraya", "belum", "mahu",
"sering", "belumkah", "mahukah", "serta", "berada", "mahupun", "seseorang", "berapa", "maka", "sesiapa", "berikan",
"malah", "sesuatu", "beriman", "mana", "sesudah", "berkenaan", "manakah", "sesudahnya", "berupa", "manapun", "sesungguhnya",
"beserta", "masih", "sesungguhnyakah", "biarpun", "masing", "setelah", "bila", "masing-masing", "setiap", "bilakah", "melainkan",
"siapa", "bilamana", "memang", "siapakah", "bisa", "mempunyai", "sini", "boleh", "mendapat", "situ", "bukan", "mendapati",
"situlah", "bukankah", "mendapatkan", "suatu", "bukanlah", "mengadakan", "sudah", "dahulu", "mengapa", "sudahkah",
"dalam", "mengapakah", "sungguh", "dalamnya", "mengenai", "sungguhpun", "dan", "menjadi", "supaya",
"dapat", "menyebabkan", "tadinya", "dapati", "menyebabkannya", "tahukah", "dapatkah", "mereka", "dapatlah",
"merekalah", "dari", "merekapun", "tanya", "daripada", "meskipun", "tanyakanlah", "daripadaku", "mu",
"tapi", "daripadamu", "nescaya", "telah", "daripadanya", "niscaya", "tentang", "demi", "nya", "tentu", "demikian",
"olah", "terdapat", "demikianlah", "oleh", "terhadap", "dengan", "orang", "terhadapmu", "dengannya", "pada", "termasuk",
"di", "padahal", "terpaksa", "dia", "padamu", "tertentu", "dialah", "padanya", "tetapi", "didapat", "paling",
"didapati", "para""dimanakah", "pasti", "engkau", "patut", "tiap", "engkaukah",
"patutkah", "tiap-tiap", "engkaulah", "per", "engkaupun", "pergilah", "hai", "perkara",
"hampir", "perkaranya", "turut", "hampir-hampir", "perlu", "untuk", "hanya", "pernah", "untukmu",
"hanyalah", "pertama", "wahai", "hendak", "pula", "walau", "hendaklah", "pun", "walaupun", "hingga", "sahaja",
"ya", "ia", "saja", "yaini", "iaitu", "saling", "yaitu", "ialah", "sama", "yakni", "ianya", "sama-sama", "yang",
"inginkah", "samakah", "ini", "sambil"]


#----------------------------------------------------------------------
#----------------****STEMMING & LEMMATIZATION*****----------------------
#----------------------------------------------------------------------
st.subheader("Stemming & Lemmatization")

for_sent = []

def listToString(s):  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s)) 

for line in file1: 
    txt = line.strip().lower().translate(str.maketrans('', '', string.punctuation))
    
    #normalized = transformer_small.translate([txt], beam_search = False)
    #normalized = normalized[0].lower().translate(str.maketrans('', '', string.punctuation))
    
    sentence_tokens = sent_tokenize(txt)
    
    for i in sentence_tokens:
        word_token = tokenizer(i)
        
        
        #list2.append(word_token)
        
        for w in word_token: 
            
            w2 = normalizer.normalize(w, normalize_entity = False)
            w2 = w2['normalize']
            #st.write('1st w2: ', w2)
            
            if w2 not in malay_stopwords: 
                #st.write('2nd w2: ', w2)
                if w2 not in filtered_sentence:
                    filtered_sentence.append(w2)  

        word = listToString(filtered_sentence)
        st.write(ngram_stem_malaya(word))
        #for_sent.append(ngram_stem_malaya(word))
                                
        filtered_sentence = []

st.header("Polarity")
file2_combined = ' '.join(file2) 
sent = malaya.sentiment.multinomial()
st.write(sent.predict_proba([file2_combined], add_neutral = False))

#st.write(file2_combined)
    
        #f = open("C:/Users/User/Documents/Year 3/FYP/implementation/lyrics-data/CLEANED LYRICS/2BY2 - Bukan Jodoh Kita.txt", "a")
        #to_write = ngram_stem_malaya(word)
        #f.write(to_write)
        
        #filtered_sentence = []

