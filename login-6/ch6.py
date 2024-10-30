# Sources: 
## https://www.geeksforgeeks.org/vigenere-cipher/
## https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher 

all_hashes = ['EAQSZTGHNZ', 
              'EBTDUJYXVILZ', 
              'KGHASTDVCUG',
              'QJGFZMDNNRDLZB']

def decrypt_vigenere(msg, key):
    decrypted_text = []
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)

if __name__ == "__main__":
    # for hash in all_hashes:
    #     print(find_differences(hash))


    admin_hash = "KGHASTDVCUG"
    key = "XTFHXUEVNOR"


    print(decrypt_vigenere(admin_hash, key))
    
