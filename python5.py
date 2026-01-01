#question 1
#num1=int(input('Enter a first number:'))
#num2=int(input('Enter second number:'))
#num3=int(input('Enter third number:'))
#if num1==num2 and num2==num3:
 #   if num3==num1:
  #      print('All numbers are equal.')
   # else: 
    #    print('Two numbers are equal.')
#else:
 #   print('All numbers are different.')

#question2 
#num=int(input('Enter a number:'))
#if num%7==0:
    #print('The number is divisible by 7.')
#else:
 #   print('The number is not divisible by 7.')


#question3 
#num=int(input('Enter a number: '))
#if num>0:
 #   if num%2==0:
  #      print('It is an even number.')
   # else:
    #    print('It is an odd number.')
#elif num<0:
 #   print('The number is negative.')
#else:
 #   print("the number is zero.")

#question4
#num=int(input('Enter the floor you want to go:'))
#if num<5:
 #   print('The lift should go down.')
#elif num>5:
 #   print('The lift should go up.')
#else:
 #   print('The lift should stay.')

#question5
#num=int(input('Enter a nunber:'))
#if num%3==0  and num%5==0:
    #print('Fizz buzz')
#elif num%3==0 and num%5!=0:
 #   print('Fizz')
#elif num%3!=0 and num%5==0:
 #   print('Buzz')
#else: 
 #   print('Usual')

#question6
#import random
#result=random.randint(0,5)
#if result==0:
 #   print('Flamingos turn pink from eating shrimp.')
#elif result==1:
 #   print('The only food that doesnt spoil is honey.')
#elif result==2:
 #   print('Shrimp can only swim backwards.')
#elif result==3:
 #   print('A taste buds life span is about 10 days.')
#elif result==4:
 #   print('It is impossible to sneeze while sleeping.')
#else:
 #   print('It is illegal to sing off-key in North Carolina. ')


#question7
#amount=int(input("Enter total purchase:"))
#customer=input("is Member (True/False):").lower()
#if amount>1000 and customer=='true':
    #print("Discount is 20%")
    #final_amount=amount-0.2*amount
    #print(f"Total amount={final_amount}")
#elif amount>1000 and customer=="false":
    #print("Discount is 10%")
    #final_amount=amount-0.1*amount
    #print(f"Total amount={final_amount}")
#else:
    #print("No Discount")
    #print(f"Total amount={amount}")

#question 8
#weight=float(input("Enter a earth weight:"))
#number=int(input("Enter a planet number:"))
#if number==1:
    #print("Planet: Mercury")
    #destination= weight*0.38
    #print(f"Destination Weight= {destination}")
#elif number==2:
    #print("Planet: Venus")
    #destination= weight*0.91
    #print(f"Destination Weight= {destination}")
#elif number==3:
    #print("Planet: Mars")
    #destination= weight*0.38
    #print(f"Destination Weight= {destination}")
#elif number==4:
 #   print("Planet: Jupitur")
  #  destination= weight*2.53
   # print(f"Destination Weight= {destination}")
#elif number==5:
 #   print("Planet: Saturn")
  #  destination= weight*1.07
   # print(f"Destination Weight= {destination}")
#elif number==6:
    #print("Planet: Uranus")
    #destination= weight*0.89
    #print(f"Destination Weight= {destination}")
#elif number==7:
 #   print("Planet: Neptune")
  #  destination= weight*1.14
   # print(f"Destination Weight= {destination}")
#else:
 #   print("Invalid Planet Number")


#question 9
#n1=int(input('Enter the marks of computer: '))
#n2=int(input('Enter the marks of nepali: '))
#n3=int(input('Enter the marks of maths: '))
#n4=int(input('Enter the marks in science: '))
#total=n1+n2+n3+n4
#per=(total/400)*100
#print(f'The total marks is: {total} ')
#print(f'The percentage is: {per} ')
#if per>=70:
 #   print('Distinction')
#elif per>=60:
 #   print('First Division')
#elif per>=40:
  #  print('Pass')
#else:
 #   print('Fail')


#question 10
cp=int(input('Enter the cost price: '))
if cp>100000:
    print('The road tax to be paid is 15%.')
elif cp>50000 and cp<=100000:
    print('The road tax to be paid is 10%.')
else:
    print('The road tax to be paid is 5%. ')


#question 11
time=int(input('Enter the time period of service (in years): '))
if time>10:
    print('The bouns is 10%.')
elif time>=6 and time<=10:
    print('The bonus is 8%.')
else:
    print('The bonus is 5%.')


#question 12
age=int(input('Enter the age: '))
gender=(input('Enter the gender (M,F):'))
day=int(input('Enter the number of day you have worked: '))
if age>=18 and age<30:
        if gender=='M':
            wage=700*day
        elif gender=='F':
            wage=750*day
elif age>=30 and age<=40:
        if gender=='M':
             wage=800*day 
        elif gender=='F':
            wage=850*day
else:
        print('The age and gender is not valid.')
print('Total wages=',wage)

#question 13
is_valid=True
balance= 'RS 5000'
correct_pin=123
if is_valid:
    pin=int(input('Enter the PIN:')) 
    if pin==correct_pin:
        print('1. Withdraw' \
        '2. Check Balance' \
        '3. Exit')
        num=int(input('Enter the action you want:'))
        if num==1:
            amount=int(input('Enter the amount you want to withdraw:'))
            balance=balance-amount
            print('Please collect your cash.')
            print(f'The remaining balance:{balance}')
        elif num==2:
            print(f'The balance is {balance}')
        elif num==3:
            print('Thankyou for visiting!!')
        else:
            print('The action is invalid.')
    else:
        print('The PIN is incorect.')
else:
    print('Invalid card')

#question 14
print("Welcome to the Magic Forest")

direction = input("Do you want to go north or south? ")

if direction == "south":
    print("Game Over")

elif direction == "north":
    choose = input("Do you want to cross the river or follow the path? ")

    if choose == "cross the river":
        print("Game Over")

    elif choose == "follow the path":
        choice2 = input("Choose fairy, ogre, or elf: ")

        if choice2 == "elf":
            print("You Win")
        else:
            print("Game Over")
