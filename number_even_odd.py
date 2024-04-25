# Reading the integers from "number.txt" file
with open("numbers.txt", "r") as new_file:
    numbers = new_file.read().split()

# Separating the integers into even and odd number lists
numbers = (int(num) for num in numbers)

odd_numbers = (num for num in numbers if num % 2 == 1)
even_numbers = (num for num in numbers if num % 2 == 0)

# Writing the even number list to "even.txt"
with open("even.txt", "w") as even_integers_file:
    for num in even_numbers:
        even_integers_file.write(str(num) + "\n")

# Writing the odd number list to "odd.txt"
with open("odd.txt", "w") as odd_integers_file:
    for num in odd_numbers:
        odd_integers_file.write(str(num) + "\n")
        
# Displaying that the program is executed
