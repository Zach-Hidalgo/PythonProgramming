"""
Programmer: Zach Hidalgo
Program: numbersType
Program Version: 3.10.2
Created On: 9/26/2022 08:11:00
Last Modified: 9/30/2022 08:11:00

"""
print("Welcome to Mathematical Operations\n")
print("1 Odd Numbers\n"
      "2 Even Numbers\n"
      "3 Prime Numbers\n"
      "4 Perfect Numbers\n"
      "5 Palindrome\n")
choice = int(input("Select an Operation by Entering a Number:\t"))
if choice == 1:
      print("Printing Odd Numbers from the First 100 Natural Numbers\n")
      for i in range(0,101):
            if (i%2 != 0):
                  print(i,end= " ")

elif choice == 2:
      print("Printing Even Numbers from the First 100 Natural Numbers\n")
      for i in range(0,101):
            if(i%2 == 0):
                  print(i,end=" ")

elif choice == 3:
      print("Printing Prime Numbers from the First 100 Natural Numbers")
      counter = 0 #initializing counter variable to 0
      n = 100
      for n in range(1, 101): #checking number of divisors for a number
            for i in range(2, int(n/2+1)): #iterating for numbers between 2 and n/2
                  if n%i == 0: #check for remainder is 0
                        counter = counter+1 #increase the counter if you find a divisor
            if counter == 0: #decision to see if counter is 0 i.e. no divisors
                  print(n,end=" ") #printing the number is prime
            counter = 0

elif choice == 4:
    print("Perfect Numbers from First 100 Natural Numbers")
    sum = 0
    check = 0
    n = 100
    for n in range(1, 101):
        for i in range(1, int(n/2+1)):
            check = n % i
            if (check == 0):
                sum = sum + i
        if sum == n:
            print(n,end=" ")
        sum = 0

elif choice == 5:
    print("Palindrome Numbers\n")
    number = int(input("Please Enter your Number:\t"))
    reverse = 0
    originalNumber = number
    while number>0:
        remainder = int(number%10)
        reverse = int(reverse*10+remainder)
        number = int(number/10)
    if originalNumber == reverse:
        print(originalNumber, "Is a Palindrome Number")
    else:
        print(originalNumber, "Is not a Palindrome Number")



