from functools import reduce

# Define a constant to control how many expenses are entered.
NUMBER_OF_EXPENSES = 5


def get_expenses():
    # Create a list to store expense information entered by the user.
    expenses = []

    # Ask the user for several expenses so they can build a monthly list.
    for count in range(NUMBER_OF_EXPENSES):

        # Prompt for the expense type so the expense can be identified later.
        expense_type = input(
            f"Enter expense type #{count + 1}: "
        )

        # Prompt for the amount so calculations can be performed.
        expense_amount = float(
            input(
                f"Enter the amount for {expense_type}: $"
            )
        )

        # Store the expense as a tuple containing the name and amount.
        expenses.append((expense_type, expense_amount))

    # Return the completed list to the calling function.
    return expenses


def calculate_total(expenses):
    # Add all expense amounts together to determine the monthly total.
    total_expense = reduce(
        lambda total, item: total + item[1],
        expenses,
        0
    )

    # Return the total expense amount.
    return total_expense


def calculate_highest(expenses):
    # Compare expense amounts to determine which expense is the largest.
    highest_expense = reduce(
        lambda first, second:
        first if first[1] > second[1] else second,
        expenses
    )

    # Return the expense with the highest amount.
    return highest_expense


def calculate_lowest(expenses):
    # Compare expense amounts to determine which expense is the smallest.
    lowest_expense = reduce(
        lambda first, second:
        first if first[1] < second[1] else second,
        expenses
    )

    # Return the expense with the lowest amount.
    return lowest_expense


def display_results(
    total_expense,
    highest_expense,
    lowest_expense
):
    # Display the total of all monthly expenses.
    print(f"\nTotal Monthly Expenses: ${total_expense:.2f}")

    # Display the expense name and amount with the highest value.
    print(
        f"Highest Expense: {highest_expense[0]} "
        f"(${highest_expense[1]:.2f})"
    )

    # Display the expense name and amount with the lowest value.
    print(
        f"Lowest Expense: {lowest_expense[0]} "
        f"(${lowest_expense[1]:.2f})"
    )


def main():
    # Collect the user's monthly expense information.
    expenses = get_expenses()

    # Calculate the total amount spent.
    total_expense = calculate_total(expenses)

    # Find the expense with the highest amount.
    highest_expense = calculate_highest(expenses)

    # Find the expense with the lowest amount.
    lowest_expense = calculate_lowest(expenses)

    # Display the results to the user.
    display_results(
        total_expense,
        highest_expense,
        lowest_expense
    )


# Call the main function to start the program.
main()