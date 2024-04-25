# Reading the integers from "number.txt" file
with open("numbers.txt", "r") as new_file:
    numbers = new_file.read().split()

# Separating the integers into even and odd number lists

numbers = (int(num) for num in numbers)

odd_numbers = (num for num in numbers if num % 2 == 1)
even_numbers = (num for num in numbers if num % 2 == 0)
# Writing the even number list to "even.txt"
# Writing the odd number list to "odd.txt"
# Displaying that the program is executed
