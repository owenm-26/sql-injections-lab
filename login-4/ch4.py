# Source: ChatGPT prompting for how to go from hex to string

def xor_recovery(hash_hex):
    hash_bytes = bytes.fromhex(hash_hex)

    # XOR each byte with 0xa5
    recovered_bytes = bytes(b ^ 0xa5 for b in hash_bytes)

    # return the decoded message as a string
    return recovered_bytes.decode('utf-8', errors='replace')
 
target_hex = "edeaf5f0eaea"
recovered_input = xor_recovery(target_hex)
print("Recovered input:", recovered_input)
