'''
Count Down
1/17/2023
Python I

Instructions:
Trace the program and predict what it will display.
Then run the program to check your work. Finally,
be prepared to discuss the following questions...
1. What is the first number stored in i? How can
   you determine this by looking at the code?
2. What is the last number stored in i? How can
   you determine this by looking at the code?
3. What is added to i after each pass of the loop?
   How can you determine this by looking at the code?
4. What does line 23 do in the program?
'''

import time

for count in range(10, 0, -1):
    print(str(count) + "...")
    time.sleep(1)
print("Blast off!")