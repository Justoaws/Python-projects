# Write a python program using function, to create an English to French translator program
# The program takes a word from the user as an input and translates it using 
# a dictionary data type as a vocabulary. Please add the translation of "prune" in your
# project. If word is not in the code vocabulary, print ({word}) is not in my memory

def translator_english_to_french(): 
    translator = input('Please enter the word you want to translate:\n')

    word_translated = {
    "prune": "Le pruneau est le fruit séché d'une variété de prunier cultivé",
    "mango": "La mangue",
    "pineapple": "L'ananas"
    }

    if translator in word_translated:
     print(f"The translation of {translator} in French is: {word_translated[translator]}")
    else:
     print(f"{translator} is not in my memory")

translator_english_to_french()
