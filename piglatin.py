print('Welcome to the Pig Latin Translator!')
pyg = 'ay'
original = input('Enter a Word:') 
if len(original) > 0 and original.isalpha(): #untuk memastikan ascii alfabet semua
    word = original.lower() #mengecilkan semua huruf
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print(new_word)
else:
    print('empty')
