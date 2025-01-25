import random
import string

def generate_long_string(min_length=121):
    characters = string.ascii_letters + string.digits + string.punctuation
    length = random.randint(min_length, min_length * 2)
    return ''.join(random.choice(characters) for _ in range(length))