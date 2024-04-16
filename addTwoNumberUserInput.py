
# store input number
num1 = float(input("write firstt number:")) 
num2 = float(input("write secound number:")) 
# add two numbers
num1 = "{:.2f}".format(num1)
num2 = "{:.2f}".format(num2)
sum = float(num1) + float(num2)
# Display the sum
print("The sum of {0} and {1} is {2}".format(num1,num2,sum))