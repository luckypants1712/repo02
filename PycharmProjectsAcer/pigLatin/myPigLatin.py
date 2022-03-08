sentence = 'My name is AL SWEIGART and I am 40,  years old.'
vowels = ['a', 'e', 'i', 'o', 'u']
newSentence = []

for word in sentence.split():
    if word[0].lower() in vowels:
        word = word + 'yay'
        newSentence.append(word)
        continue

    for i in word:
        if i.lower() not in vowels:
            word += i
            word = word[1:]
        else:
            break
    word = word + 'ay'
    newSentence.append(word)
print(newSentence)





