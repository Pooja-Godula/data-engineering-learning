def add(a,b):
    return a+b
def is_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"

a=10
b=5
addition = add (a,b)
print("Addition is:",addition)
number = 34
result = is_even_odd(number)
print(f"Number {result}")