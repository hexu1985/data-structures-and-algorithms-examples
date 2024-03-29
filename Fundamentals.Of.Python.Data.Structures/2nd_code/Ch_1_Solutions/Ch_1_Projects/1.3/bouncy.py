"""
Program: bouncy.py
Project 1.3

This program calculates the total distance a ball travels as it bounces given:
1. the initial height of the ball
2. its bounciness index
3. the number of times the ball is allowed to continue bouncing

"""

height = float(input("Enter the height from which the ball is dropped: "))
bounciness = 0.6
distance = 0
bounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))
for eachPass in range(bounces):
    distance += height
    height *= bounciness
    distance += height
print('\nTotal distance traveled is:', distance, 'units.')

