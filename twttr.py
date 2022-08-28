# Python_Intro
# Problem Set 5
#A series of exercises for CS50 hands-on projects
"""
This one's my approach to the "twttr" problem
"""
def main():
    text = input("Input: ")
    message_without_vowels = shorten(text)
    print("Output: " + message_without_vowels)

def shorten (word):
    word_without_vowels = ""
    for character in word:
        if not character.lower() in ['a', 'e', 'i', 'o', 'u']:
                word_without_vowels += character
    return word_without_vowels

if __name__ == "__main__":
    main()
