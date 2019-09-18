print('Welcome to the Reverse Pig Latin Translator!')
pyg = 'ay'
original = input('Enter a Word:') 
if len(original) > 0 and original.isalpha(): #untuk memastikan ascii alfabet semua
    word = original.lower() #mengecilkan semua huruf
    n = len(word)
    i = 0
    new_word = ''
    while i < n-3:
        new_word = new_word + word[i]
        i = i+1
    final_word = word[n-3] + new_word
    print(final_word)
else:
    print('empty')
