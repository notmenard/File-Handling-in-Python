# Open the file in append mode
with open("mylife.txt", "a") as my_file:

    # Setting up a variable to hold the user's response.
    more_lines = "y"
    # Loop until the user confirms that there are no more lines
    while more_lines == "y":
        # Collecting the user's input
        line = input("Enter line:")
        my_file.write(line + "\n")
        # Displaying the program's output
        more_lines = input("Are there more lines (y/n)? ").lower()
        if more_lines != "y":
            break
