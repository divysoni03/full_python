# Loops : 

# for :
# while : 
# do while :  Not in Python 
##########################
# for Loop : 
# syntax :
                        # 1.range(intialization , last value(-1))
# for (declare A Variable) in condition:
    # code 


# wap to print 1 to 10 : 

# for i in range(1,10):
#     print(i)

# wap to print 10 to 1 : 
# for i in range(10,0,-1):
#     print(i,end=",")


# prime or Not : 

############################################
# while Loop: 
# intialization
# while condition :
#     code
#     +=,-=,

# wap to print 1 to 10 : 
# i=1
# while i<=10:
#     print(i,end=",")
#     i+=1    # i = i+1
#             #i++  = i =i+1

# Armstrong Number : 

# wap to print 10 to 1 : 
# i=10
# while i>=1:
#     print(i,end=",")
#     i-=1    # i = i+1
#             #i++  = i =i+1




# -> task 1 isPrime using for loop

number = int(input("Enter a number :"))
isPrime = True

for i in range(2, number-1):
    if(number % i == 0):
        isPrime = False


if(isPrime):
    print("Entered number ", number, " is prime number.")
else:
    print("Entered number ", number, "is not prime number.")



# -> Task 2 : is Armstrong number

# number = int(input("Enter 3-digit number : "))

# i = number
# sum = 0
# while i > 0:
#     sum += int((i%10))**3
#     i /= 10

# print(sum, " ", number)

# if(sum == number):
#     print("Entered number ", number ,"is armstrong number")
# else:
#     print("Entered number ", number ," is not a armstrong number.")