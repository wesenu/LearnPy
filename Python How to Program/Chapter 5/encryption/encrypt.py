import encryption_methods
import encryption_key    

user_input = input('Enter your string: ')

user_encryption_key = encryption_key.get_key(user_input.lower())
encrypted_data = encryption_methods.encrypt(user_input.lower(), user_encryption_key)
decrypted_data = encryption_methods.decrypt(encrypted_data, user_encryption_key)