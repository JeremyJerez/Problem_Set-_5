# Python_Intro
# Problem Set 5
#A series of exercises for CS50 hands-on projects
"""
This one's my approach to the "Testing my twttr" problem
"""
#import from twttr
from twttr import shorten

def main():
 
    test_upper_lower_cases()
    test_numbers()
    test_punctuation()

def test_upper_lower_cases():
     assert shorten('twitter') == 'twttr'
     assert shorten('TWITTER') == 'TWTTR'
     assert shorten('TwItTeR') == 'TwtTR'

def test_numbers():
    assert shorten("1234567890") == "1234567890"

def test_punctuation():
    assert shorten("!?;:,.") == "!?;:,."

if __name__ == "__main__":
    main()
