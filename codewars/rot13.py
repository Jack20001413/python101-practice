import string

def get_encrypted_character(char, is_lower):
    lowercase_alphabet = list(string.ascii_lowercase)
    uppercase_alphabet = list(string.ascii_uppercase)
    chosen_alphabet = lowercase_alphabet if is_lower else uppercase_alphabet

    cipher_index = chosen_alphabet.index(char) + 13
    if cipher_index >= len(chosen_alphabet):
        cipher_index %= 13
    return chosen_alphabet[cipher_index]

def rot13(plain_text):
    cipher = ''
    for char in plain_text:
        cipher += char if not char.isalpha() else get_encrypted_character(char, char.islower())
    return cipher

def solution2(plain_text):
    alphabet = string.ascii_uppercase
    cipher = ''
    for letter in plain_text:
        if letter in alphabet.lower():
            cipher += alphabet[(alphabet.lower().index(letter) +13) % 26].lower()
        elif letter in alphabet:
            cipher += alphabet[(alphabet.index(letter) +13) % 26]
        else:
            cipher += letter
    return cipher

text = 'Duckj_'
ciphered_text = rot13(text)
print(ciphered_text)
