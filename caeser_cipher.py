#caeser cipher is shifting of letters by 3 units
#a->d , b->e, and so on. x->a, y->b, z->c

import string

def create_caeser_dict():
    l = string.ascii_lowercase
    l=list(l)
    d = {}
    for i in range(len(l)):
        d[l[i]] = l[(i+3)%26]
    return d    
        
d = create_caeser_dict() 
  
f = open('temp.txt','r')
g = open('encrypted_text.txt','w')

c = f.read(1)
while(c != ''):
    g.write(d[c])
    c = f.read(1)
    
f.close()
g.close()



    