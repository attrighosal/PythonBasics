words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'] 

sentence = ""

for word in words: 
    sentence += word+" "

# print(sentence)


## Join in one line 

sentence="".join(words) 

# print(sentence) 


## Join space

sentence=" ".join(words) 

# print(sentence) 


## Join using comma

sentence=",".join(words) 

print(sentence) 
