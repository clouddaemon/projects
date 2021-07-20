## making a histagram
import time
dup = []
blds = {} 
count = 1
first_names = ['efrem','steve','marcia','ethan','ethan','efrem','efrem']
#first_names = ['steve','ethan']

### assign any first name in list:1 (example efrem:1) ####
for i in first_names[:]:
    blds[i] = count          

### add a number if there is an occurance ###

for z in blds:
    dup.append(i)
    print(dup)
    for x in dup[:]: 

        if i == x:               ### check first occurence of word in list ### 
            count = count + 1
            blds[i] = count      ### efrem:1 ###
  
        if  i in blds:        ### why am i interating this? ###        
            #print('i =',i)   ### i = efrem 
            #print('blds = ',blds) = efrem:1
            blds[i] = count   ### ??? ###
            print('second blds =', blds)
            #dup.remove(x)
            time.sleep(10)
        else:
                count = count + 1
                blds[i] = count 
                #print(blds)
print(blds) 
