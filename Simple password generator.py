import random

def generate_password(nr_letters, nr_symbols, nr_numbers):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!#$%&()*+"

    password_list = (
        [random.choice(letters) for _ in range(nr_letters)] +
        [random.choice(numbers) for _ in range(nr_numbers)] +
        [random.choice(symbols) for _ in range(nr_symbols)]
    )
    
    random.shuffle(password_list)
    return ''.join(password_list)

# Get user input
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Generate password
password = generate_password(nr_letters, nr_symbols, nr_numbers)
print(f"Your random password is: {password}")
