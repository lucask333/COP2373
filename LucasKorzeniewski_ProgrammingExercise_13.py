import sqlite3
import random
import matplotlib.pyplot as plt

# Database file name
DATABASE_NAME = "population_LK.db"

# Starting year for the recorded population data
START_YEAR = 2023

# Number of years to simulate after the starting year
YEARS_TO_SIMULATE = 20

# Ten Florida cities with their real approximate 2023 populations,
# used as the seed data for the simulation
STARTING_CITIES = {
    "Jacksonville": 971319,
    "Miami": 442241,
    "Tampa": 398173,
    "Orlando": 316081,
    "St. Petersburg": 258308,
    "Hialeah": 220832,
    "Port St. Lucie": 231622,
    "Tallahassee": 201731,
    "Cape Coral": 216992,
    "Fort Lauderdale": 183342,
}


def create_database():
    """
    Create the database, create the population table,
    and insert the 2023 starting data for each Florida city.
    """

    # Connect to (or create) the database file on disk
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Drop the table first so this function can be re-run safely
    cursor.execute("DROP TABLE IF EXISTS population")

    # Create the population table with the three required fields
    cursor.execute(
        """
        CREATE TABLE population (
            city TEXT NOT NULL,
            year INTEGER NOT NULL,
            population INTEGER NOT NULL
        )
        """
    )

    # Insert the seed (2023) population value for every city
    for city, population in STARTING_CITIES.items():
        cursor.execute(
            "INSERT INTO population (city, year, population) "
            "VALUES (?, ?, ?)",
            (city, START_YEAR, population),
        )

    # Save the changes and close the connection
    connection.commit()
    connection.close()

    # Let the user know the setup step finished successfully
    print("Database and starting 2023 data created successfully.")


def simulate_population_growth():
    """
    Simulate 20 years of population growth or decline for each city
    using a random yearly rate, then insert the results into the
    population table.
    """

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    # Track the current population for each city as we move
    # forward year by year
    currentPopulations = dict(STARTING_CITIES)

    # Repeat the simulation for each of the 20 future years
    for yearOffset in range(1, YEARS_TO_SIMULATE + 1):
        simulationYear = START_YEAR + yearOffset

        # Apply a different random rate to each city so that some
        # cities grow while others may shrink, just like real life
        for city in currentPopulations:

            # Choose a random growth rate between -2% and +4% to
            # represent realistic yearly population change
            growthRate = random.uniform(-0.02, 0.04)

            # Apply the rate to the city's current population
            newPopulation = currentPopulations[city] * (1 + growthRate)

            # Round to a whole number since people cannot be
            # fractional
            currentPopulations[city] = round(newPopulation)

            # Insert this year's simulated population into the table
            cursor.execute(
                "INSERT INTO population (city, year, population) "
                "VALUES (?, ?, ?)",
                (city, simulationYear, currentPopulations[city]),
            )

    # Save the simulated data and close the connection
    connection.commit()
    connection.close()

    # Confirm to the user that the simulation is complete
    print("Population growth simulation for 20 years is complete.")


def plot_population_growth():
    """
    Ask the user to choose one of the 10 Florida cities and display
    a line chart of that city's simulated population from 2023
    through 2043 using matplotlib.
    """

    # Build a numbered list so the user can pick a city by number
    cityList = list(STARTING_CITIES.keys())

    # Show the available cities to the user
    print("\nAvailable cities:")
    for index, city in enumerate(cityList, start=1):
        print(f"{index}. {city}")

    # Keep asking until the user enters a valid city number
    chosenCity = None
    while chosenCity is None:

        # Prompt the user for their selection
        userInput = input(
            "\nEnter the number of the city you would like to see: "
        )

        # Validate that the input is a number within the valid range
        if userInput.isdigit() and 1 <= int(userInput) <= len(cityList):
            chosenCity = cityList[int(userInput) - 1]
        else:
            print("That was not a valid choice. Please try again.")

    # Retrieve the chosen city's data from the database
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    cursor.execute(
        "SELECT year, population FROM population "
        "WHERE city = ? ORDER BY year",
        (chosenCity,),
    )
    rows = cursor.fetchall()
    connection.close()

    # Split the query results into separate lists for plotting
    years = [row[0] for row in rows]
    populations = [row[1] for row in rows]

    # Plot the population trend as a line chart
    plt.figure(figsize=(10, 6))
    plt.plot(years, populations, marker="o", color="steelblue")

    # Label the chart so it is clear what is being shown
    plt.title(f"Population Growth for {chosenCity} ({START_YEAR}-"
              f"{START_YEAR + YEARS_TO_SIMULATE})")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)

    # Display the finished chart to the user
    plt.tight_layout()
    plt.show()


def main():
    """
    Run the full program: set up the database, simulate growth,
    and let the user visualize a city's population trend.
    """

    # Step 1: build the database and insert the 2023 starting data
    create_database()

    # Step 2: simulate 20 years of growth and decline
    simulate_population_growth()

    # Step 3: let the user pick a city and view its trend
    plot_population_growth()


# Only run the program if this file is executed directly
if __name__ == "__main__":
    main()