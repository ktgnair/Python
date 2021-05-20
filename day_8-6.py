# Caesar Cipher
# Step 4 : User experience iimprovement and Final Touches
# ToDo 1: Import and print the logo from art.py when the program starts.

# ToDo 2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
# Hint: Think about how you can use the modulus (%). 

# ToDo 3: What happens if the user enters a number/symbol/space?
# Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
# e.g. start_text = "meet me 4 at 3"
# end_text = "•••• •• •• 3"
# hello g 8 y
# mjqqt y 8 u

# ToDo 4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

import art
print(art.logo)

# Here in alphabet a-z is written twice so that if the word has a letter z then it should again start from a
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(input_text, no_of_shifts, cipher_direction):
    cipher_text = []
    if cipher_direction == "decode":
            no_of_shifts *= -1
    for i in input_text:
        if i in alphabet:
            final_shift = alphabet.index(i) + no_of_shifts
            single_letter = alphabet[final_shift]
            cipher_text.append(single_letter)
        else:
            cipher_text.append(i)
    
    print(f"The {cipher_direction}d text is  {''.join(cipher_text)}")


flag = True
while  flag:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # If the shift is entered greater than 26
    shift %= 26
    caesar(input_text = text, no_of_shifts = shift, cipher_direction = direction)

    rerun = input("Enter yes to run again else type no: ").lower()
    if rerun == "no":
        print("GoodBye")
        flag = False