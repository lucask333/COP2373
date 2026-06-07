# Define the maximum number of tickets that can be sold.
MAX_TICKETS = 10

# Define the maximum number of tickets one buyer can purchase.
MAX_PER_BUYER = 4


# Create a function to display the remaining tickets.
def display_remaining_tickets(remaining_tickets):

    # Display how many tickets are still available.
    print(f"There are {remaining_tickets} tickets remaining.\n")


# Create a function to handle ticket sales.
def sell_tickets():

    # Store the number of tickets remaining.
    remaining_tickets = MAX_TICKETS

    # Store the total number of buyers.
    buyer_count = 0

    # Continue selling tickets until none remain.
    while remaining_tickets > 0:

        # Show the user how many tickets are available.
        display_remaining_tickets(remaining_tickets)

        # Ask the user how many tickets they want to buy.
        tickets_requested = int(
            input("Enter the amount of tickets you would like to purchase. (1 - 4)")
        )

        # Make sure the user enters a valid amount.
        if (
            tickets_requested >= 1
            and tickets_requested <= MAX_PER_BUYER
            and tickets_requested <= remaining_tickets
        ):

            # Subtract the purchased tickets from the total remaining.
            remaining_tickets = (
                remaining_tickets - tickets_requested
            )

            # Add one to the buyer count.
            buyer_count = buyer_count + 1

            # Display a confirmation message.
            print(
                f"You purchased {tickets_requested} ticket(s).\n"
            )

        else:

            # Inform the user their input was invalid.
            print(
                "Invalid number of tickets requested. "
                "Please try again.\n"
            )

    # Display a message when all tickets are sold.
    print("All tickets have been sold.")

    # Display the total number of buyers.
    print(f"Total number of buyers: {buyer_count}")


# Call the function to start selling tickets.
sell_tickets()