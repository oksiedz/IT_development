alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cesar_cipher(input_text, input_shift, input_direction):
    output_word = ""
    for letter in input_text:
        new_letter = ""
        if input_direction == "encode":
            if alphabet.index(letter) + input_shift > alphabet.index("z"):
                new_letter = alphabet[(alphabet.index(letter) + input_shift) - alphabet.index('z') - 1]
            else:
                new_letter = alphabet[alphabet.index(letter) + input_shift]
        else:
            if alphabet.index(letter) - input_shift < alphabet.index("a"):
                new_letter = alphabet[(alphabet.index(letter) - input_shift)]
            else:
                new_letter = alphabet[alphabet.index(letter) - input_shift]
        output_word += new_letter
    print(f"Message {input_text} was {input_direction}d to {output_word}")


direction = ""

while direction not in ["encode", "decode"]:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if direction in ["encode", "decode"]:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cesar_cipher(input_text=text, input_shift=shift, input_direction=direction)
