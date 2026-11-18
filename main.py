"""
AIXcelerate - Happy or Sad Mood Guesser
Roll-number rule: last digit = 1, so each clue-word list has exactly 1 word.

AI assistance declaration:
This file was prepared with help from ChatGPT. I should explain the code
and make sure I understand every function before submitting it.
"""

import string

# Dataset provided in the AIXcelerate student instructions
train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad"),
]


# Level 1: Count the number of Happy and Sad sentences
def count_moods(data):
    happy_count = 0
    sad_count = 0

    for sentence, mood in data:
        if mood == "Happy":
            happy_count += 1
        elif mood == "Sad":
            sad_count += 1

    return happy_count, sad_count


# Level 2: Each list contains exactly one clue word because the
# last digit of the roll number is 1. Review these choices yourself.
happy_words = ["surprise"]
sad_words = ["upset"]


def guess_mood(sentence):
    # Convert to lowercase and remove punctuation before checking words.
    cleaned_sentence = sentence.lower().translate(
        str.maketrans("", "", string.punctuation)
    )
    sentence_words = cleaned_sentence.split()

    happy_count = 0
    sad_count = 0

    for word in sentence_words:
        if word in happy_words:
            happy_count += 1
        if word in sad_words:
            sad_count += 1

    # Tie rule: choose Happy when both clue-word counts are equal.
    if happy_count >= sad_count:
        return "Happy"
    else:
        return "Sad"


# Level 3: Test the program on the five practice sentences
practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy"),
]


def test_program():
    correct = 0

    for sentence, actual_mood in practice_data:
        predicted_mood = guess_mood(sentence)

        print("Sentence:", sentence)
        print("Predicted mood:", predicted_mood)
        print("Actual mood:", actual_mood)
        print()

        if predicted_mood == actual_mood:
            correct += 1

    accuracy = (correct / len(practice_data)) * 100
    print("Correct answers:", correct, "out of", len(practice_data))
    print("Accuracy:", round(accuracy, 2), "%")


if __name__ == "__main__":
    print("Mood counts:", count_moods(train_data))
    print()
    test_program()
