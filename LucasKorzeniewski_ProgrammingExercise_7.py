# Import the regular expression module.
import re

# Create a constant that stores the sentence pattern. The pattern finds a sentence that ends with a period, question mark, or exclamation point. The look-ahead ensures the next sentence may begin with a capital letter, a number, or the end of the paragraph.
SENTENCE_PATTERN = (
    r"[A-Z0-9].*?[.!?](?=\s+[A-Z0-9]|\s*$)"
)


# Prompt the user to enter a paragraph.
def get_paragraph():
    # Ask the user for a paragraph.
    paragraph = input("Enter a paragraph: ")

    return paragraph


# Find and display each sentence in the paragraph.
def display_sentences(paragraph):
    # Find all sentences that match the pattern.
    sentences = re.findall(SENTENCE_PATTERN, paragraph)

    # Display each sentence.
    print("\nIndividual Sentences:")

    for count, sentence in enumerate(sentences, start = 1):
        print(f"{count}. {sentence.strip()}")

    return len(sentences)


# Display the total number of sentences found.
def display_sentence_count(sentence_count):
    # Display the total sentence count.
    print(f"\nTotal number of sentences: {sentence_count}")


# Control the flow of the program.
def main():
    # Get the paragraph from the user.
    paragraph = get_paragraph()

    # Display the sentences and save the count.
    sentence_count = display_sentences(paragraph)

    # Display the total number of sentences.
    display_sentence_count(sentence_count)


# Start the program.
main()