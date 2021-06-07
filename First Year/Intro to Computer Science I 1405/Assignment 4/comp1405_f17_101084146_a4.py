# ============================================================
#
# Student Name (as it appears on cuLearn): Alyxander-Jacob Ricketts
# Student ID (9 digits in angle brackets): <101084146>
# Course Code (for this current semester): COMP1405B
#
# ============================================================

from comp1405_f17_assistant_a4 import *

# This assigns all the questions to variables.
glasses_q = "Do you have glasses?: "
hair_q = "Do you have hair?: "
hat_q = "Do you have a hat?: "
pipe_q = "Do you have a pipe?: "
moustache_q = "Do you have a moustache?: "
eye_patch_q = "Do you have an eye patch?: "
earing_q = "Do you have an earing?: "
tie_q = "Do you have a tie?: "
tattoo_q = "Do you have a tattoo?: "

glasses = ask_question(glasses_q).upper()
# This block of code runs if they have glasses.
if glasses == "YES":
    hair = ask_question(hair_q).upper()

    if hair == "YES":
        hat = ask_question(hat_q).upper()

        if hat == "YES":
            pipe = ask_question(pipe_q).upper()

            if pipe == "YES":
                make_a_guess("Emerson")
            else:
                make_a_guess("Frankie")
        else:
            eye_patch = ask_question(eye_patch_q).upper()

            if eye_patch == "YES":
                make_a_guess("Glenn")
            else:
                make_a_guess("Brooklyn")
    else:
        moustache = ask_question(moustache_q).upper()

        if moustache == "YES":
            pipe = ask_question(pipe_q).upper()

            if pipe == "YES":
                make_a_guess("Dakota")
            else:
                make_a_guess("Roan")
        else:
            hat = ask_question(hat_q).upper()

            if hat == "YES":
                make_a_guess("Blaine")
            else:
                make_a_guess("West")
# This block of code runs if they do not have glassses.
else:
    eye_patch = ask_question(eye_patch_q).upper()

    if eye_patch == "YES":
        tattoo = ask_question(tattoo_q).upper()

        if tattoo == "YES":
            pipe = ask_question(pipe_q).upper()

            if pipe == "YES":
                make_a_guess("Lincoln")
            else:
                make_a_guess("Ray")
        else:
            hat = ask_question(hat_q).upper()

            if hat == "YES":
                make_a_guess("James")
            else:
                make_a_guess("Harley")
    else:
        earing = ask_question(earing_q).upper()

        if earing == "YES":
            tie = ask_question(tie_q).upper()

            if tie == "YES":
                make_a_guess("Amari")
            else:
                make_a_guess("Kennedy")
        else:
            hat = ask_question(hat_q).upper()

            if hat == "YES":
                make_a_guess("Landry")
            else:
                make_a_guess("Blaine")
