# Caesar Cipher
# Step 3 : Reorganising the Code
# ToDo 1: Combine the encrypt() and decrypt() functions into a single function called caesar().
# ToDo 2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values. 

# Here in alphabet a-z is written twice so that if the word has a letter z then it should again start from a
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(input_text, no_of_shifts, cipher_direction):
    cipher_text = []
    if cipher_direction == "decode":
            no_of_shifts *= -1
    for i in input_text:
        final_shift = alphabet.index(i) + no_of_shifts
        single_letter = alphabet[final_shift]
        cipher_text.append(single_letter)
    print(f"The {cipher_direction}d text is  {''.join(cipher_text)}")

caesar(input_text = text, no_of_shifts = shift, cipher_direction = direction)