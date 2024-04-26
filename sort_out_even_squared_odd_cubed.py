# Opening the source file named "integers.txt" for reading
with open("integers.txt", "r") as my_file:
    # Creating the two output files
    with open("double.txt", "w") as double_file, open("triple.txt", "w") as triple_file:
        # Reading the integers from the source file
        for line in my_file:
            # Converting the line into an integer
            number = int(line)

            # Checking for the integer if even
            if number % 2 == 0:

# Writing the square of the even number to the double.txt file
# Writing the cube of the odd number to triple.txt file
# Displaying that the program is executed
