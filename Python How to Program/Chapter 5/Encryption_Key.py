import string


def get_key(my_input):
    exclude = set(string.punctuation)
    new_string = ''.join(ch for ch in my_input if ch not in exclude)
    new_string = new_string.replace(" ", "")
    new_string = list(set(new_string) and set(string.ascii_lowercase))
    return list(new_string)
