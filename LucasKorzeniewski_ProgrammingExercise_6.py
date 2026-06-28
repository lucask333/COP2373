# Import the regular expression module.
import re


# Define a constant pattern for validating phone numbers.
PHONE_PATTERN = r"^\(\d{3}\)\s\d{3}-\d{4}$"

# Define a constant pattern for validating Social Security numbers.
SSN_PATTERN = r"^\d{3}-\d{2}-\d{4}$"

# Define a constant pattern for validating ZIP codes.
ZIP_PATTERN = r"^\d{5}(-\d{4})?$"


# Determine whether the phone number matches the required format.
def validate_phone(phone_number):
    # Return True if the phone number matches the pattern.
    return re.fullmatch(PHONE_PATTERN, phone_number) is not None


# Determine whether the Social Security number matches the
# required format.
def validate_ssn(ssn):
    # Return True if the Social Security number matches the pattern.
    return re.fullmatch(SSN_PATTERN, ssn) is not None


# Determine whether the ZIP code matches the required format.
def validate_zip(zip_code):
    # Return True if the ZIP code matches the pattern.
    return re.fullmatch(ZIP_PATTERN, zip_code) is not None

# Get user input and display whether each value is valid.
def main():
    # Display instructions for the phone number format.
    print("Enter a phone number in the format (123) 456-7890.")

    # Prompt the user for a phone number.
    phone_number = input("Phone number: ")

    # Determine whether the phone number is valid.
    if validate_phone(phone_number):
        print("The phone number is valid.")
    else:
        print("The phone number is invalid.")

    print()

    # Display instructions for the Social Security number format.
    print("Enter a Social Security number in the format "
          "123-45-6789.")

    # Prompt the user for a Social Security number.
    ssn = input("Social Security number: ")

    # Determine whether the Social Security number is valid.
    if validate_ssn(ssn):
        print("The Social Security number is valid.")
    else:
        print("The Social Security number is invalid.")

    print()

    # Display instructions for the ZIP code format.
    print("Enter a ZIP code in the format 12345 or 12345-6789.")

    # Prompt the user for a ZIP code.
    zip_code = input("ZIP code: ")

    # Determine whether the ZIP code is valid.
    if validate_zip(zip_code):
        print("The ZIP code is valid.")
    else:
        print("The ZIP code is invalid.")

# Start the program only when this file is executed directly.
if __name__ == "__main__":
    main()
