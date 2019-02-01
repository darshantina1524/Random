from textblob import TextBlob

original = input('Enter a string to be translated \n')

print('Welcome to Translater')
print('Language to translate the text in:')
print('1. English')
print('2. French')
print('3. Hindi')
print('4. Spanish')
print('5. Urdu')
print('6. Chineese')
d = {1:'en',2:'fr',3:'hi',4:'es',5:'ar',6:'zh-CN'}
option = int(input('Select an option above \n'))

import nltk

from textblob import Word

original_without_error = ""
test = TextBlob(original)
for i in test.words:
    w = Word(i)
    test = sorted(w.spellcheck(),key=lambda x:-x[1])[0]
    original_without_error += test[0]+" "

print(original_without_error)
lang = TextBlob(original_without_error)
my = lang.translate(to=d[option])
print('Input of the string is in',lang.detect_language())
print(my)
print('Current language of the text is',my.detect_language())
