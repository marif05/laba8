def reverse_number(number):
    return int(str(number)[::-1])

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def process_numbers(numbers):
    for number in numbers:
        reversed_number = reverse_number(number)
        print(f"Original: {number}, Reversed: {reversed_number}")
        if is_palindrome(number):
            print(f"{number} is a palindrome")

numbers = [121, 456, 789, 101]
process_numbers(numbers)
