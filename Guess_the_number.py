import random
usr_input=input("Enter Your Name : ")
rnd_num=random.randint(1,20)
for x in range(1,7):
    ent_numb=int(input("Enter Your Number :"))
    if ent_numb==rnd_num:
        print("Hi!",usr_input,", your guess matched.")
        break
    elif ent_numb >= rnd_num:
        print("Your Number is too large")
    else:
        print("Your Number is too small")
else:
    print("You are out of Attempts.Thanks!!")