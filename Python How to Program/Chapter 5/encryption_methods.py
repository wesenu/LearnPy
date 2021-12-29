import string

def encrypt(user_input, encryption_key):
    encrypted_string = ''

    for i in user_input:
        try:
            char_index = string.ascii_lowercase.index(i)
            if(char_index == ' '):
                encrypted_string += ' '
            
            encrypted_string += encryption_key[char_index]    
        except ValueError:
            print(f'{i} not found in the search space.')

    print(encrypted_string)
    return encrypted_string

def decrypt(user_input, encryption_key):
    decrypted_string = ''
    
    for i in user_input:
        decrypted_char = encryption_key.index(i)
        decrypted_string += string.ascii_lowercase[decrypted_char]
    
    print(decrypted_string)
    return decrypted_string