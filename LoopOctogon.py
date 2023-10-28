'''
Loop Octagon
Pawelski
10/28/2023
Introduction to Computer Science

Instructions:
Trace the code and predict what the program will do.
Check your prediction by running the program.
Make sure you understand what EACH line in the
program does before moving on. Finally, consider
the following questions and modifications...
1. Modify the program so that it draws a regular pentagon.
   What did you have to change?
2. How do you know when to use a loop?
3. What does line 28 do in this program? (Hint: You may want
   to print out the value stored in red to see what random
   number is generated!)
4. What does line 31 do in this program? (Hint: If you are
   unsure, check in with Mr. Pawelski!)
'''

import turtle, random

my_turtle = turtle.Turtle()

# This will set the color of the turtle to something random.
red = random.random()
green = random.random()
blue = random.random()
my_turtle.color(red, green, blue)

for sides in range (0, 8):
  my_turtle.forward(100)
  my_turtle.left(45)
