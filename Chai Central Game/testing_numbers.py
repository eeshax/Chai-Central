import random
def teastuff():
    assam = "cm2"+"pan"+"sink"+"cb"
    masala = "cr"+"cup"+"cm1"+"sink"
    badshah = "pan"+"cup"+"cm2"+"cm1"
    royal = "cr"+"cm2"+"cup"+"sink"
    tulsi = "cb"+"pan"+"sink"+"cm1"
    darjeeling = "cup"+"cr"+"pan"+"sink"
    kashmiri = "cm1"+"cm2"+"sink"+"cup"
    
    tea = [("assam",assam),("masala",masala),("badshah",badshah),("royal",royal),("tulsi",tulsi),("darjeeling",darjeeling),("kashmiri",kashmiri)]
    
    menu1 = random.choice(tea)
    menu2 = random.choice(tea)
    t1, t2 = menu1
    i1, i2 = menu2
    return t1, t2
    return i1, i2

    
t1, t2 = teastuff()
i1, i2 = teastuff()
print(t1, i1)
print(t2+i2)




    

