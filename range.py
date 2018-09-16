import random
def randnumber():
    l=[0 for i in range(0,20)]
    for i in range(1,20):
         a=random.randint(0,100)
         l[i]=a
    return l
	
tt = randnumber()
print(tt)
