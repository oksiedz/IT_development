alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(inputtext, inputshift):
    encrypted = ''
    for letter in inputtext:
        new_letter = ''
        alphabet.index(letter)
        if alphabet.index(letter) + inputshift > alphabet.index('z'):
            new_letter = alphabet[(alphabet.index(letter) + inputshift) - alphabet.index('z') - 1]
        else:
            new_letter = alphabet[alphabet.index(letter) + inputshift]
        encrypted += new_letter
    print(f"Message {inputtext} was encrypted to {encrypted}")


def decrypt(inputtext, inputshift):
    decrypted = ""
    for letter in inputtext:
        new_letter = ""
        letter_index = alphabet.index(letter)
        if alphabet.index(letter) - inputshift < 0:
            new_letter = alphabet[(alphabet.index(letter) - inputshift)]
        else:
            new_letter = alphabet[alphabet.index(letter) - inputshift]
        decrypted += new_letter
    print(f"Message {inputtext} was decrypted to {decrypted}")


if direction == "encode":
    encrypt(text, shift)
if direction == "decode":
    decrypt(text, shift)

