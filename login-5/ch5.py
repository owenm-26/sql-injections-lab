#Sources: 
## https://www.w3schools.com/python/ref_random_randrange.asp
## https://www.w3schools.com/python/ref_string_encode.asp
## https://docs.python.org/3/library/hashlib.html

import random
import hashlib

def brute_force(target, salt):
   
    while True:
        password_guess = random.randrange(0, 99999)

        response = hash_and_check(target, password_guess=password_guess, salt=salt)
        if response:
            return response
    


def hash_and_check(target_hash, password_guess, salt):
    password_guess  = str(password_guess)
    salted_guess = password_guess + salt
    salted_guess = salted_guess.encode()
    hash_guess = hashlib.sha256(salted_guess)
    if hash_guess.hexdigest() == target_hash:
        print(f"Success!!! {target_hash}")
        return password_guess

    salted_guess = salt + password_guess
    salted_guess = salted_guess.encode()
    hash_guess = hashlib.sha256(salted_guess)
    if hash_guess.hexdigest() == target_hash:
        print(f"Success!!! {target_hash}")
        return password_guess

    return None

if __name__ == "__main__":
    target = "a3dd5834b69218a6e6e670e8231d4160d88a6353005b9252387b3a19ea12f872"
    salt =  "yv"
    print(brute_force(target=target, salt=salt))