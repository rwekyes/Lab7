# Part 1

def vigenere_sq(alphabet):
    alph_length = len(alphabet)
    alph_list = []
    print(f"|---|", end="")
    for i in range(alph_length):
        alph_list.append("| " + alphabet[i] + " ")
    for i in alph_list:
        print(f"{i}", end = "")
    print("")
    for _ in range(108):
        print(f"=", end="")
    print("")
    for i in range(alph_length - 1):
        alph_list.extend(alph_list[0])
        alph_list.pop(0)
        print(f"{alph_list[0]}", end="")
        print(f"|", end="")
        print("".join(alph_list))

#vigenere_sq("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Part 2

def letter_to_index(letter, alphabet):
    index = 0
    for character in alphabet:
        if character == letter:
            return index
        index += 1
    print(f"Letter {letter} not found in alphabet {alphabet}")
    return -1

def index_to_letter(index, alphabet):
    return alphabet[index]

def vigenere_index(key_letter, plaintext_letter, alphabet):
    if plaintext_letter == " ":
        return " "
    key_index = letter_to_index(key_letter, alphabet)
    plaintext_index = letter_to_index(plaintext_letter, alphabet)
    return index_to_letter((key_index + plaintext_index) % len(alphabet), alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    key_len = len(key)
    resized_key = []
    ciphertext = []
    for i in range(len(plaintext)):
        resized_key += key[i % key_len]
        ciphertext += vigenere_index(resized_key[i], plaintext[i], alphabet)
    return "".join(ciphertext)

# Part 3

def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    if cipher_letter == " ":
        return " "
    key_index = letter_to_index(key_letter, alphabet)
    cipher_index = letter_to_index(cipher_letter, alphabet)
    return index_to_letter((cipher_index - key_index) % len(alphabet), alphabet)

def decrypt_vigenere(key, cipher_text, alphabet):
    key_len = len(key)
    resized_key = []
    plaintext = []
    for i in range(len(cipher_text)):
        resized_key += key[i % key_len]
        plaintext += undo_vigenere_index(resized_key[i], cipher_text[i], alphabet)
    return "".join(plaintext)

#plaintext = "THE EAGLE HAS LANDED"
#key = "DAVINCI"
#alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#encrypted = encrypt_vigenere(key, plaintext, alphabet)
#decrypted = decrypt_vigenere(key, encrypted, alphabet)

#print(f"Encrypted text: {encrypted}")
#print(f"Decrypted text: {decrypted}")

# Part 4

encrypted_text = []
keys = []
keys_index = 0
quit_selected = False

def encrypt_menu():
    if not keys:
        print(f"You must have at least one key to encrypt something.")
        return
    plaintext = input("Enter your plaintext: ").upper()
    global keys_index
    encrypted_text.append(encrypt_vigenere(keys[keys_index % len(keys)], plaintext, user_alphabet))
    keys_index += 1
    return

def decrypt_menu():
    local_index = 0
    for ciphertext in encrypted_text:
        print(f"{decrypt_vigenere(keys[local_index], ciphertext, user_alphabet)}")
        local_index += 1
    return

def dump_encrypted():
    print("\n".join(encrypted_text))
    return

def key_menu():
    keys.append(input("Enter your new key: ").upper())
    return

def exit_menu():
    global quit_selected
    quit_selected = True
    return

menu = [["1) Encrypt", encrypt_menu], ["2) Decrypt", decrypt_menu], ["3) Dump Encrypted Text", dump_encrypted], ["4) Add Keys", key_menu], ["5) Quit", exit_menu]]

if input("Would you like to use a custom alphabet(Y/N)? ").upper() == "Y":
    user_alphabet = input("Enter your custom alphabet: ").upper()
else:
    user_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
    for item in menu:
        print(item[0])
    selection = input("Select your option: ")
    if selection.isdigit():
        menu[int(selection) - 1][1]()
        if quit_selected:
            break