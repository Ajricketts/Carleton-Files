'''
This function will load a text file.

@params             file_name, the name of the file to be loaded
@return             an uppercase string containing the data read from the file
'''
def load_text(file_name):
    file_hndl = open(file_name, "r")
    file_data = file_hndl.read()
    file_hndl.close()
    return file_data.upper()

'''
This function will save data to a text file.

@params             file_name, the name of the file to be saved
                    file_data, the data to be written to the file
@return             none
'''
def save_text(file_name, file_data):
    file_hndl = open(file_name, "w")
    file_hndl.write(file_data)
    file_hndl.close()

'''
This function will encode a string that is passed to it as an argument.

@params             text_to_encode, the string that will be encoded.
                    encode_alphabet, this is the alphabet that will be used to encode the string.
@return             the encoded string

'''
def encode(text_to_encode, encode_alphabet):
    encoded_text = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    list(alphabet)

    for i in list(text_to_encode):
        if not(i.isalpha()):
            encoded_text += i
        for j in range(len(alphabet)):
            if i == alphabet[j]:
                encoded_text += encode_alphabet[j]

    return encoded_text

'''
This function will decode a string that is passed to it as an argument.

@params             text_to_decode, the string that will be decoded.
                    decode_alphabet, the alphabet that was used to endode it.
@return             the decoded string
'''
def decode(text_to_decode, decode_alphabet):
    decoded_text = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    alphabet_list = list(alphabet)
    for i in list(text_to_decode):
        if i not in alphabet_list:
            decoded_text += i
        for j in range(len(alphabet)):
            if i == alphabet[j]:
                decoded_text += alphabet[j]

    return decoded_text

'''
This function will shift the alphabet over a certain number of times.
@params             shift_num, The number of times the alphabet should be shifted.
@return             returns the shfted alphabet
'''

def caesar_cipher_alphabet(shift_num):
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    alphabet_list = list(alphabet)
    new_string = ''
    for i in range(shift_num):
        popped_letter = alphabet_list.pop()
        new_string += popped_letter
    for j in alphabet_list:
        new_string += j
    cipher_output = str(new_string)
    return cipher_output
'''
This function will take a user inputed alphabet and check to make sure its valid.
@params             none
@return             the new alphabet that the user inputed.
'''
def cryptogram_alphabet():
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    user_alphabet = input("Please provide an alphabet you wish to use to encode with: ").upper()
    user_alphabet_list = list(user_alphabet)
    duplicate = False
    for i in user_alphabet_list:
        for j in user_alphabet_list:
            if i != j:
                duplicate = False
            else:
                duplicate = True

    if len(user_alphabet_list) != 26 or duplicate:
        print("Your alphabet did not contain all 26 letters or contains duplicate")
        print("letters, please provide a valid alphabet.")
        print("Such as: ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        return alphabet
    else:
        return user_alphabet



'''
This function will take a user inputed string and put it to the front of the alphabet.
@params             input_string, the string that the user inputs to set in front of the alphabet
@return             returns the new alphabet with the string in front.
'''
def keyword_cipher_alphabet(input_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
    alphabet_list = list(alphabet)
    new_alphabet = ''
    output = ''
    counter = 0
    input_string_list = list(input_string.upper())
    while (counter < (len(input_string))):
        for j in range(len(alphabet) - counter):
            if input_string_list[counter] == alphabet_list[j]:
                new_alphabet += alphabet_list.pop(j)
                break
        counter += 1
    for a in alphabet_list:
        output += a

    output = new_alphabet + output
    return print(output)

'''
This function displays a menu bar.
@params             none
@return             none
'''
def menu_bar():
    print("\t###################################################################")
    print("\t############################  MENU  ###############################")
    print("\t###################################################################\n\n")


'''
This function displays the menu.
@params             none
@return             none
'''
def menu():
    menu_bar()
    print("\nWhat would you like to do?\n")
    print("[1] Load a File")
    print("[2] Save a File")
    print("[3] Encode.")
    print("[4] Decode")
    print("[5] Create a Shifted alphabet.")
    print("[6] Create your own alphabet.")
    print("[7] Create a Keyword alphabet.")

    selection = input("> ")
    return selection



'''
This is the main function, responsible for the user interface.

@params             none
@return             none
'''

def main():
    #print("Current Text: ")
    #encode_alphabet = "fghijklmnopqrstuvwxyzabcde".upper()
    #text_to_encode = "Computers make very fast very, accurate mistakes".upper()
    #decode_alphabet = encode_alphabet
    #encode(text_to_encode, encode_alphabet)
    #decode(text_to_encode, encode_alphabet)
    #caesar_cipher_alphabet(5)
    #cryptogram_alphabet()


    initial = ''
    initial_text = 'Initial Text: ' + initial
    current = ''
    current_text = 'Current Text: ' + current
    current_alphabet = ''

    input_string = input("What would you like the keyword to be?: ")
    keyword_cipher_alphabet(input_string)


    while True:
        selection = menu()
        print(initial_text)
        print(current_text)
        if selection == "1":
            file_name = input("What is the name of the file you wish to load?: ")
            load_text(file_name)

        elif selection == "2":
            file_save = input("What is the name of the file you wish to save?: ")
            save_file(file_save, current_text)
        elif selection == "3":
            if current == '' or current_alphabet == '':
                print("There is no current text to encode, please load a text and try again.")
            else:
                current = encode(current, current_alphabet)

        elif selection == "4":
            if current == '':
                print("There is no current text to decode, please load a text and try again.")
            else:
                current = decode(current, current_alphabet)
        elif selection == "5":
            shift_num = input("How far would you like to shift the alphabet?: ")
            if shift_num > 26 or shift_num < 1:
                print("That is not a valid number to shift the alphabet over")
            else:
                caesar_cipher_alphabet(shift_num)

        elif selection == "6":
            cryptogram_alphabet()
        elif selection == "7":
            input_string = input("Please input a keyword you would like to start the alphabet off with: g")
            keyword_cipher_alphabet(input_string)













    # much of your code will go here

# this is the only line in your code that isn't inside a function definition
main()
