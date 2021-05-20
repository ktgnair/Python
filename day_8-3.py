# Caesar Cipher
# Step 1 : Encryption
# ToDo 1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# ToDo 2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# ToDo 3: Call the encrypt function and pass in the user inputs. 
# You should be able to test the code and encrypt a message.

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
    
if direction == "encode":
    encrypt(input_text = text, no_of_shifts = shift)
elif direction == "decode":
    print("This function will be availabe soon")