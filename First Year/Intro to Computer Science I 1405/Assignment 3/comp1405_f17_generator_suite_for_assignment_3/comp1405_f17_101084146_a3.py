# ============================================================
#
# Student Name (as it appears on cuLearn): Alyxander-Jacob Ricketts
# Student ID (9 digits in angle brackets): <101084146>
# Course Code (for this current semester): COMP1405B
#
# ============================================================

from comp1405_f17_assistant_a3 import *

#first_condition = if color_is_red(e) and wrapped_in_a_triangle(e):
	#True
#elif color_is_black(e) and wrapped_in_a_circle(e):
	#True
#else:
	#False

def decision_making_function(e):  # 'e' IS THE SHAPE ARGUMENT YOU MUST PASS TO YOUR PERMITTED FUNCTIONS

	condition_for_sending_down = color_is_red(e) and wrapped_in_a_triangle(e) or color_is_black(e) and wrapped_in_a_circle(e)


	condition_for_sending_left = color_is_blue(e) and wrapped_in_a_diamond(e) and not evenly_divides_by(e, 2) or color_is_green(e) and not wrapped_in_a_triangle(e) and not evenly_divides_by(e, 2)

	condition_for_sending_right = color_is_green(e) and wrapped_in_a_triangle(e) or color_is_blue(e) and not wrapped_in_a_diamond(e) and not evenly_divides_by(e, 2)

	return (condition_for_sending_down, condition_for_sending_left, condition_for_sending_right)


run_the_program(decision_making_function)
