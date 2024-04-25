# Open the file containing student data and read all lines
with open("student_record.txt", "r") as students_data:
    lines = students_data.readlines()

# Initialize variables to keep track of the student's highest GWA
highest_gwa = float("inf")
highest_student_name = ""

# Checking for the highest student's GWA
# Displaying the student who had the highest GWA
