import string
import secrets

def generate_secret(n=32, **kwargs):
    """
    Generates an N-length secret string based on optional keyword arguments.
    
    Args:
        n (int): The length of the secret string.
        **kwargs: Optional flags to modify generation.
                  - symbols: If True, adds punctuation to the character pool.
                  - uppercase: If True, adds uppercase letters to the character pool.
    """
    # Default character pool: Alphanumeric (a-z, A-Z, 0-9)
    char_pool = string.ascii_letters + string.digits

    # check if kwargs were passed
    if kwargs:
        # check if we include symbols
        # get is 'safe', it returns the key's value if it exists or returns None (if no default defined, like here)
        if kwargs.get("symbols"): 
            char_pool += string.punctuation
        
        # check if we include uppercase char
        if kwargs.get("uppercase"):
            char_pool += string.ascii_uppercase

    # Generate an n length secret string
    return ''.join(secrets.choice(char_pool) for _ in range(n))

# #
# # Examples:
# #

# N = 32
# STR_WIDTH = 12
# # 1. Default behavior (No kwargs)
# print(f"{'Default:':{STR_WIDTH}s} {generate_secret(N)}") 
# # Output: e.g., "aB3d9Kj2m1"

# # 2. With symbols (Adds punctuation)
# print(f"{'Symbols:':{STR_WIDTH}s} {generate_secret(N, symbols=True)}") 
# # Output: e.g., "aB$d9!j2m1"

# # 3. With uppercase (Uppercase only)
# print(f"{'Uppercase:':{STR_WIDTH}s} {generate_secret(N, uppercase=True)}") 
# # Output: e.g., "ABDEKJM123"

# # 4. With both:
# print(f"{'Both:':{STR_WIDTH}s} {generate_secret(N,symbols=True, uppercase=True)}")