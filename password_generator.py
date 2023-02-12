import random
import string

"""
This script generates a random password of the desired length using a combination of ASCII letters, digits, and punctuation. The use of different character types makes the password strong and unguessable, while the randomness of the password ensures that it is unique and not easily predictable. To increase the strength of the password, you can increase the length of the password or add additional character types to the list of characters used in the password.
"""

def generate_password(length=16, special_chars=True):
    """
    Generates a strong and unguessable password.
    
    Keyword arguments:
    length -- the desired length of the password (default 16)
    """
    # List of characters to be used in the password
    chars = string.ascii_letters + string.digits

    if special_chars:
        chars += string.punctuation
    
    # Generate a random password of the desired length
    password = ''.join(random.choice(chars) for i in range(length))
    
    return password


if __name__ == '__main__':
    # Example usage
    print(generate_password())
    print(generate_password(special_chars=False))

