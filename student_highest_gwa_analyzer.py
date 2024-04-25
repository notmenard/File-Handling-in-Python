# Open the file containing student data and read all lines
with open("student_record.txt", "r") as students_data:
    lines = students_data.readlines()

# Initialize variables to keep track of the student's highest GWA
highest_gwa = float("inf")
highest_student_name = ""

# Finding for the highest student's GWA
for line in lines:
    name, gwa = line.strip().split(",")
    gwa = float(gwa)

    # Checking for the highest student's GWA
    if gwa < highest_gwa:
        highest_gwa = gwa
        highest_student_name = name

# Displaying the student who had the highest GWA
intro = " Student With The Highest GWA "
intro = intro.center(48, "-")
print(intro)
print(f"Name: {highest_student_name}")
print(f"GWA: {highest_gwa}")
