
word = " python  " 

print("Unstripped word :"+word+":") 
print("Stripped word :"+word.strip()+":") 
print("Left Stripped word :"+word.lstrip()+":") 
print("Right Stripped word :"+word.rstrip()+":") 

sentence = "the quick brown fox jumped over the lazy dog the" 
print("Sentence after removing \"the\": "+sentence.strip("the").replace("the", ""))
