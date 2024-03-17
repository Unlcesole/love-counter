import random
a=input("Enter first name:  ")
b=input("Enter second name:  ")
c=random.randint(1,100)
print(f"love between {a} and {b} is",c,("%") )
if c<=10:
    print("looks like you both hate each other")
if c>=10 and c<=40:
    print("looks you dislike each other")    
elif c>= 40 and c<=50:
    print("looks that you both slightly dislike each others")
elif c>=50 and c<=60:
    print("looks like you both slightly love each other")
elif c>=70 and c<=80:
    print("looks like you both love each other")
elif c>=80 and c==100:
    print("you both love each other much and more :)")
else:
    print("")







