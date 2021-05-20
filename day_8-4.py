# Caesar Cipher
# Step 2 : Decryption
# ToDo 1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# ToDo 2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
# ToDo 3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. 
# You should be able to test the code to encrypt *AND* decrypt a message.

# Here in alphabet a-z is written twice so that if the word has a letter z then it should again start from a
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
def encrypt(input_text, no_of_shifts):
    cipher_text = []
    for i in input_text:
        final_shift = alphabet.index(i) + no_of_shifts
        single_letter = alphabet[final_shift]
        cipher_text.append(single_letter)
    print(f"The encoded text is  {''.join(cipher_text)}")
    
# Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
def decrypt(input_text, no_of_shifts):
    cipher_text = []
    for i in input_text:
        final_shift = alphabet.index(i) - no_of_shifts
        single_letter = alphabet[final_shift]
        cipher_text.append(single_letter)
    print(f"The decoded text is  {''.join(cipher_text)}")

if direction == "encode":
    encrypt(input_text = text, no_of_shifts = shift)
elif direction == "decode":
    decrypt(input_text = text, no_of_shifts = shift)