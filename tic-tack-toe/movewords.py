
f=open("word_list", "r+") 
foods = (f.readlines())
for i in foods:
    i = [l.strip() for l in foods if l.strip()] 
with open('new_list', "w") as f:
    f.writelines('\n'.join(i)) 

f.close() 
