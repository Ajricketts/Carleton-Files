# ============================================================
#
# Student Name (as it appears on cuLearn): Alyxander-Jacob Ricketts
# Student ID (9 digits in angle brackets): <101084146>
# Course Code (for this current semester): COMP1405B
#
# ============================================================

from comp1405_f17_assistant_a5 import *
#from time import sleep


#  THE FOLLOWING CODE HAS BEEN INCLUDED FOR DEMONSTRATION PURPOSES ONLY
# YOU MUST REPLACE THIS CODE WITH THE SPECIFIC LOOPING CONTROL STRUCTURES
#   THAT WERE ASSIGNED TO YOU BY THE ASSIGNMENT GENERATOR INSTRUCTIONS

# Step One
for x in range(13):
    move_down()

#Step Two
num1 = True

while num1:
    move_right()

    if what_number_am_i_standing_on() == 5:
        num1 = False

# Step Three
while what_number_am_i_standing_on() != 3:
    move_down()

# Step Four
num2 = True

while num2:
    move_left()

    if am_i_standing_on(5):
        num2 = False

# Step Five
for x in range(22):
    move_down()

# Step Six
while True:
    move_right()

    if am_i_standing_on(5):
        break

# Step Seven
while True:
    move_down()

    if what_number_am_i_standing_on() == 3:
        break

# Step Eight
for x in range(30):
    move_left()

# Step Nine
while am_i_standing_on(3) == False:
    move_down()
