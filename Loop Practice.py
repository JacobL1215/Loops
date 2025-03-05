#3/4/2025
#Jacob Loh
#made to practice loops

print("This code spells hello using loops!")
word = "hello"
for h in word:
    print(h)

print("||||||||||||||||||")

for i in range(2,6): #Loop from 2 to 5 
    print(i)

print("--------------------------------")
for i in range(1): #Loop 1
    print(1+i)

print ("-------------------------------")

for i in range(-2, 10, -2): #Loop 2
    print(i)

print("---------------------------------------------")

number = 1#print("What number do you choose: ")
while number < 5: 
    print(number)
    number += 1

Text = ""
while True:
    Letter = input("What is i don't know:") #set it in its own line
    Text += Letter
    print(Text)
    if Letter == "abcdefghijk":
        break
Symbol = "*"


