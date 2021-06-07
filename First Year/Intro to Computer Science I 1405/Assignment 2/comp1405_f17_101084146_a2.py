# ============================================================
#
# Student Name (as it appears on cuLearn): Alyxander-Jacob Ricketts
# Student ID (9 digits in angle brackets): <101084146>
# Course Code (for this current semester): COMP1405B
#
# ============================================================


# Import the argv function from sys.
import sys
# Get and store the number the user gave in the terminal. (Step 1)
terminal_num = (sys.argv[1])
num = int(terminal_num)

# This does the math to get the second last digit in the 9 digit number. (Step 2)
new = (num // 10) % 10

# Print the result of Step 2. (Step 3)
print(new)

# This finds the index of the rightmost '1' in the commandline argument (terminal_num). (Step 4)
find_1 = "1"
right_1 = terminal_num.rfind(find_1)

#Print the result of the previous step to the terminal. (Step 5)
print(right_1)
# Finds the sum of step 2 and step 4 and stores it in a new variable. (Step 6)
value = new + right_1
print(value)
# Add 15 to the new variable created in step 6 (the sum). (Step 8)
new_value = value + 15
print(new_value)
# Adds one less than the value of the variable in step 8. (Step 10)
new_value += (new_value - 1)
print(new_value)
# Subtract 12 (Step 12).
new_value -= 12
print(new_value)
# Divide by 2 (Step 14).
new_value = float(new_value / 2)
print(new_value)
# Subtract the value from step 6. (Step 16)
new_value = new_value - value
print(new_value)
# Add 88.5 (Step 18)
new_value = new_value + 88.5
# This changes the integer into its corresponding Unicode charecter (Letter) and makes it uppercase. (Step 19)
letter = (chr(int(new_value)))
letter = letter.upper()
# Final Step (Step 20)
print(letter)
