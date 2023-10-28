'''
Repeat Phrase
Pawelski
10/28/2023
Introduction to Computer Science

Instructions:
Trace the program and predict what it will display.
Then run the program to check your work. Finally,
be prepared to discuss the following questions...
1. Based on this example, can variables be used in
   the range function?
2. Is this a definite or indefinite loop?
'''

phrase = input("Enter a phrase >> ")
times = int(input("Times to repeat >> "))
for i in range(0, times):
    print(phrase)
