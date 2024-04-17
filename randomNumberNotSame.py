import random

prev_result = None

while True:
       result = random.randint(0,10)
       if result != prev_result:
              print(result)
              prev_result = result
              break
              
while True:
       result= random.randrange(1,10)
        
       if result != prev_result:
              print(result)
              prev_result = result    
              break  
              