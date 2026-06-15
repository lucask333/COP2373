# List of common words and phrases found in spam messages
SPAM_KEYWORDS = [
    "free",
    "winner",
    "cash",
    "act now",
    "buy now",
    "limited time",
    "risk free",
    "guaranteed",
    "click here",
    "earn money",
    "make money",
    "double your income",
    "free gift",
    "congratulations",
    "claim now",
    "exclusive offer",
    "discount",
    "credit card",
    "no obligation",
    "no credit check",
    "urgent",
    "money back",
    "prize",
    "bonus",
    "extra income",
    "cheap",
    "special promotion",
    "offer expires",
    "apply now",
    "financial freedom"
]


def CalculateSpamScore(EmailMessage):
    """
    Calculate the spam score by checking the email for spam words.
    Return the score and a list of detected spam words.
    """

    # Convert the email to lowercase to make searching easier.
    EmailMessage = EmailMessage.lower()

    # Store the total spam score.
    SpamScore = 0

    # Store all spam words found in the message.
    FoundWords = []

    # Check each spam keyword against the email message.
    for Keyword in SPAM_KEYWORDS:

        # Count how many times the keyword appears.
        Occurrences = EmailMessage.count(Keyword)

        # Add one point for each occurrence found.
        if Occurrences > 0:
            SpamScore = SpamScore + Occurrences

            # Save the keyword that caused spam points.
            FoundWords.append(
                f"{Keyword} ({Occurrences} occurrence(s))"
            )

    return SpamScore, FoundWords


def DetermineSpamLikelihood(SpamScore):
    """
    Determine the likelihood that the email is spam based on
    the calculated spam score.
    """

    # Assign a rating based on the score range.
    if SpamScore == 0:
        return "Very Low"
    elif SpamScore <= 3:
        return "Low"
    elif SpamScore <= 6:
        return "Moderate"
    elif SpamScore <= 10:
        return "High"
    else:
        return "Very High"


def Main():
    """
    Gather an email message from the user and display the spam
    analysis results.
    """

    # Ask the user to enter an email message.
    EmailMessage = input(
        "Please enter an email message to analyze: "
    )

    print()

    # Calculate the spam score and detected words.
    SpamScore, FoundWords = CalculateSpamScore(EmailMessage)

    # Determine the spam likelihood rating.
    Likelihood = DetermineSpamLikelihood(SpamScore)

    # Display the spam analysis results.
    print("Spam Analysis Results")
    print("---------------------")
    print(f"Spam Score: {SpamScore}")
    print(f"Likelihood of Spam: {Likelihood}")

    print()

    # Display the words that contributed to the spam score.
    if len(FoundWords) > 0:
        print("Spam Words/Phrases Found:")

        for Word in FoundWords:
            print(f"- {Word}")
    else:
        print("No spam words or phrases were detected.")


# Run the program.
Main()