import csv

# Define the input file name as a constant.
FILE_NAME = "grades.csv"


def display_grades():
    """Read the CSV file and display the student records."""

    # Open the CSV file for reading.
    with open(FILE_NAME, "r", newline="") as csv_file:

        # Create a CSV reader object.
        reader = csv.reader(csv_file)

        # Read the first row so it can be displayed as column headings.
        header = next(reader)

        # Display the column headings in aligned columns.
        print(
            f"{header[0]:<15}"
            f"{header[1]:<15}"
            f"{header[2]:<10}"
            f"{header[3]:<10}"
            f"{header[4]:<10}"
        )

        # Display a separator to improve readability.
        print("-" * 60)

        # Display each student's information in table format.
        for row in reader:
            print(
                f"{row[0]:<15}"
                f"{row[1]:<15}"
                f"{row[2]:<10}"
                f"{row[3]:<10}"
                f"{row[4]:<10}"
            )


def main():
    """Run the program."""

    display_grades()


main()