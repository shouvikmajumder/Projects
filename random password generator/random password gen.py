import random

def passwordgenerator(numlength):
    chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",'t',"u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")",";"]
    password = " "
    for i in range(numlength):
        randindex = random.randint(0,len(chars)-1)
        password += chars[randindex]
    return f' Your randomly generated password is : {password}' 

numlength = int(input("How many characters do you want your password to be?: "))

print(passwordgenerator(numlength))

