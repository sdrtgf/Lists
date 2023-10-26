#1
hat = [3,5,6,7,8]
new_middle_digit = int(input('Enter a digit: '))#Prompting the user to input a digit 
hat[2] = new_middle_digit #The digit that the user input is going to replace the original middle number
print(hat)


del(hat[4])#Removing the digits listed in hat
print(hat)


print(len(hat))#finding the length of digits in the list hat