#!/usr/bin/env python

passAttempt = input("Enter Password: ")
if len(passAttempt) != 17:
    print("Are You Even Trying?")
    exit(1)


passwd = [82, 144, 207, 181, 80, 176, 81, 240, 240, 78, 181, 144, 207, 176, 241, 212, 209]
passwdArr=[]
for char in passAttempt:
    passwdArr.append( (((ord(char) << 5) | (ord(char) >> 3)) ^ 127) & 255) 
arr2=[]
for i in passwdArr:
    arr2.append( ((i + 10) - 25 ) + ((17*4)-3) //5  )
   
   
if (arr2 == passwd):
    print("That's your flag!")
else:
    print("Sorry, no dice!")






    
   








