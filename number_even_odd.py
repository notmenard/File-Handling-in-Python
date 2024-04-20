# Reading the integers from "number.txt" file
with open("numbers.txt", "r") as new_file:
    numbers = new_file.read().split()
# Separating the integers into even and odd number lists
# Writing the even number list to "even.txt"
# Writing the odd number list to "odd.txt"
# Displaying that the program is executed
