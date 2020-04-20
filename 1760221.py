import os
import re
import ntpath
from bs4 import BeautifulSoup
import nltk
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer

my_stopwords = set(stopwords.words('english') + list(punctuation))


def get_text(file):
    read_file = open(file, "r")
    text = read_file.readlines()
    text  =  ' '.join(text);
    return text

def clear_html(text):
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text()

def remove_special_character(text):
    string  = re.sub('[^\w\s]', '',text)
    string = re.sub('\s+', ' ', string)
    string  = string.strip()
    return string

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def rename_files(string):
    listString = string.split('.')
    return listString[0]+"_word."+listString[1]

def listToString(s):  
    
    str1 = ""  
    
    for ele in s:  
        str1 += ele   
     
    return str1  

def write_file(string_file, words):
    dir_name_file = './output/'+string_file

    os.makedirs(os.path.dirname(dir_name_file), exist_ok=True)
    with open(dir_name_file, "w") as f:
        f.write(listToString(words))

list_path = []

for root, dirs, files in os.walk('./input'):
    for file in files:
        list_path.append(root+"/"+file)

j = 0 
for j in range(len(list_path)):
    read_file = open(list_path[j], "r")
    a = read_file.read()
    # goi xu ly cac ham da dinh nghia
    # print(remove_special_character(clear_html(get_text(list_path[j]))))

i = 0
for i in range(len(list_path)):
    text = get_text(list_path[i])
    text_cleared = clear_html(text)

    sents = sent_tokenize(text_cleared)
    sents_cleared = [remove_special_character(s) for s in sents]
    text_sents_join = ''.join(sents_cleared)

    words = word_tokenize(text_sents_join)

    words = [word.lower() for word in words]

    words = [word for word in words if word not in my_stopwords]



ps = PorterStemmer()
words = [ps.stem(word) for word in words]

k = 0 
for k in range(len(list_path)):
    list_file_des = rename_files(path_leaf(list_path[k]));
    
    write_file(list_file_des, words)
   



# in ra cac dong
print(words)


