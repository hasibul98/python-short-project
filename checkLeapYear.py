year = int(input("Enter year"))

if(year % 400 == 0) and (year % 100 == 0):
       print("year {0} is a leap year".format(year))
elif(year % 4 == 0) and (year % 100 != 0):
       print("year {0} is a leap year".format(year))  
else:
       print("year {0} is not a leap year".format(year))            
       
       