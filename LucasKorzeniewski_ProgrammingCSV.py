import csv

# Define the output file name as a constant.
FILE_NAME = "grades.csv"


def create_grades_file():
    """Create a CSV file containing student grades."""

    # Ask the instructor how many student records to enter.
    student_count = int(input("How many students would you like to enter? "))

    # Open the CSV file for writing.
    # The newline argument prevents blank lines in the output file.
    with open(FILE_NAME, "w", newline="") as csv_file:

        # Create a CSV writer object.
        writer = csv.writer(csv_file)

        # Write the header row so the file has column names.
        writer.writerow([
            "First Name",
            "Last Name",
            "Exam 1",
            "Exam 2",
            "Exam 3"
        ])

        # Repeat once for each student so every student has one record.
        for _ in range(student_count):

            # Collect the student's identifying information.
            first_name = input("Enter the student's first name: ")
            last_name = input("Enter the student's last name: ")

            # Collect the student's exam grades.
            exam_1 = int(input("Enter Exam 1 grade: "))
            exam_2 = int(input("Enter Exam 2 grade: "))
            exam_3 = int(input("Enter Exam 3 grade: "))

            # Write the student's information as one row in the CSV file.
            writer.writerow([
                first_name,
                last_name,
                exam_1,
                exam_2,
                exam_3
            ])

    # Let the instructor know the file has been created.
    print("\nThe grades.csv file has been created successfully.")


def main():
    """Run the program."""

    create_grades_file()


main()