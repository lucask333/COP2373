import csv
import numpy as np


def load_grades(csv_path):
    """
    Load numeric exam grade columns from the CSV file into a numpy array.

    Returns:
        names       -- list of exam/column names (e.g. ['Exam 1', 'Exam 2', 'Exam 3'])
        grades      -- 2D numpy array of shape (num_students, num_exams)
        student_ids -- list of "First Last" names, one per row
    """
    with open(csv_path, newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    # First two columns are First Name / Last Name; the rest are exam scores.
    exam_names = header[2:]
    student_ids = [f"{row[0]} {row[1]}" for row in rows]
    grades = np.array([[float(val) for val in row[2:]] for row in rows])

    return exam_names, grades, student_ids


def print_preview(exam_names, grades, student_ids, num_rows=11):
    """Print the header and the first few rows of the dataset."""
    print("=" * 60)
    print("DATA PREVIEW")
    print("=" * 60)
    header_line = f"{'Student':<15}" + "".join(f"{name:>10}" for name in exam_names)
    print(header_line)
    for i in range(min(num_rows, len(student_ids))):
        row_line = f"{student_ids[i]:<15}" + "".join(f"{grades[i, j]:>10.1f}" for j in range(grades.shape[1]))
        print(row_line)
    print()


def print_per_exam_stats(exam_names, grades):
    """Calculate and print mean, median, std dev, min, and max for each exam."""
    print("=" * 60)
    print("PER-EXAM STATISTICS")
    print("=" * 60)
    for j, name in enumerate(exam_names):
        column = grades[:, j]
        print(f"{name}:")
        print(f"  Mean:               {np.mean(column):.2f}")
        print(f"  Median:             {np.median(column):.2f}")
        print(f"  Standard Deviation: {np.std(column):.2f}")
        print(f"  Minimum:            {np.min(column):.2f}")
        print(f"  Maximum:            {np.max(column):.2f}")
        print()


def print_overall_stats(grades):
    """Calculate and print mean, median, std dev, min, and max across all exams combined."""
    print("=" * 60)
    print("OVERALL STATISTICS (ALL EXAMS COMBINED)")
    print("=" * 60)
    all_grades = grades.flatten()
    print(f"  Mean:               {np.mean(all_grades):.2f}")
    print(f"  Median:             {np.median(all_grades):.2f}")
    print(f"  Standard Deviation: {np.std(all_grades):.2f}")
    print(f"  Minimum:            {np.min(all_grades):.2f}")
    print(f"  Maximum:            {np.max(all_grades):.2f}")
    print()


def print_pass_fail_counts(exam_names, grades, passing_grade=60):
    """Determine and print the number of students who passed/failed each exam."""
    print("=" * 60)
    print(f"PASS/FAIL COUNTS PER EXAM (passing grade = {passing_grade})")
    print("=" * 60)
    for j, name in enumerate(exam_names):
        column = grades[:, j]
        passed = int(np.sum(column >= passing_grade))
        failed = int(np.sum(column < passing_grade))
        print(f"{name}: Passed = {passed}, Failed = {failed}")
    print()


def print_overall_pass_percentage(grades, passing_grade=60):
    """Calculate and print the overall pass percentage across all exams."""
    print("=" * 60)
    print("OVERALL PASS PERCENTAGE (ALL EXAMS COMBINED)")
    print("=" * 60)
    all_grades = grades.flatten()
    total = all_grades.size
    total_passed = int(np.sum(all_grades >= passing_grade))
    pass_percentage = (total_passed / total) * 100
    print(f"  Total grades recorded: {total}")
    print(f"  Total passing grades:  {total_passed}")
    print(f"  Overall pass percentage: {pass_percentage:.2f}%")
    print()


def main():
    csv_path = "grades.csv"

    exam_names, grades, student_ids = load_grades(csv_path)

    print_preview(exam_names, grades, student_ids)
    print_per_exam_stats(exam_names, grades)
    print_overall_stats(grades)
    print_pass_fail_counts(exam_names, grades, passing_grade=60)
    print_overall_pass_percentage(grades, passing_grade=60)


if __name__ == "__main__":
    main()