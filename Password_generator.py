import random as r
alphas='qwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+QWERTYUIOPASDFGHJKLZXCVBNM7894561230. '
while 1:
    length=int(input("Enter the length of password :"))
    passcount=int(input("Number of password required :"))
    for i in range(0,passcount):
        passwd=""
        for j in range(0,length):
            passchar=r.choice(alphas)
            passwd+=passchar
        print("The passwords are :",passwd)