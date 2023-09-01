# I am defining the dictionary with all characters and their Morse code values
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '
}

# I am creating a reverse dictionary that will convert Morse code to characters
reverse_morse_code_dict = {value: key for key, value in morse_code_dict.items()}


# This function converts text into Morse code
def morse_code_converter(text):
    text_to_morse_code = []
    # Ensure all letters are capitalized
    for char in text.upper():
        if char in morse_code_dict:
            text_to_morse_code.append(morse_code_dict[char])
        else:
            text_to_morse_code.append(' ')
    return ' '.join(text_to_morse_code)


# Function that converts Morse code into text
def morse_code_to_text(morse):
    words = morse.split('  ')  # Splits Morse code into words
    text = []
    for word in words:
        characters = word.split(' ')  # Splits words into characters
        for char in characters:
            if char in reverse_morse_code_dict:
                text.append(reverse_morse_code_dict[char])
            else:
                text.append(' ')
        text.append(' ')  # Adds space between words
    return ''.join(text)


# Function that gets a valid user choice
def get_user_choice():
    while True:
        choice = input("Please select an option (encode/decode/end): ").lower()
        if choice in ('encode', 'decode', 'end'):
            return choice
        else:
            print("Invalid choice. Please choose 'encode', 'decode', or 'end'.")
            return choice


# This will run our program until user enters "end"
while True:
    choice = get_user_choice()

    if choice == 'encode':
        input_text = input("Enter something: ")
        morse_code = morse_code_converter(input_text)
        print("Morse Code for the text you entered is:", morse_code)
    elif choice == 'decode':
        input_morse_code = input("Enter Morse code: ")
        decoded_text = morse_code_to_text(input_morse_code)
        print("Decoded text from Morse code is:", decoded_text)
    elif choice == 'end':
        print("Thank you for using my Morse Code Converter !!!")
        break  # Exits the program
