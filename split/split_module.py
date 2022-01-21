

## Split sentence to words
sentence = "The quick brown fox jumps over the lazy dog" 

words = sentence.split()

# print(words) 

## Split on double space
sentence = "The  quick  brown  fox  jumps  over  the  lazy dog" 

words = sentence.split()

# print(words) 

## Split on comma
sentence = "The,quick,brown,fox,jumps,over,the,lazy,dog" 

words = sentence.split(",")

# print(words)

## Limit number of splits by space
sentence = "The quick brown fox jumps over the lazy dog" 

words = sentence.split(maxsplit=5)

# print(words) 

## Limit number of splits by comma 
sentence = "The,quick,brown,fox,jumps,over,the,lazy,dog" 

words = sentence.split(",", maxsplit=5)

# print(words)

sentence = "The,quick,brown,fox,jumps over,the,lazy dog" 

words = sentence.split(",")
words = [word.split() for word in words]
print(words)
new_words = []
for word in words:
    new_words.extend(word)

print(new_words)
