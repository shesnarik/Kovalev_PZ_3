
def uppercase_generator(input_string):
    for char in input_string:
        if char.islower():
            yield char.upper()
        else:
            yield char
input_str = "Hello, World!"
result = ''.join(uppercase_generator(input_str))

print(result)
