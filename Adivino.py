min= int(input("Quin és el mínim:"))
max= int(input("Quin és el màxim:"))
num= (min+max)//2
print(num)
intents=1
valor= str(input("És major (>), menor (<) o he endivinat (S)?"))
while valor != "S" and valor!="s":
    if valor == ">":
        min=num
    else:
        max=num
    num= (min+max)//2
    print(num)
    intents +=1
    valor= str(input("És major, menor o he endivinat (S)?"))
print ("He endivinat")
print ("Ho he fet en", intents, "intents")
