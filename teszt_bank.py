# Python_Intro
# Problem Set 5
#A series of exercises for CS50 hands-on projects
"""
This one's my approach to the "Back to the Bank" problem
"""
from bank import value

def main():
    test_return_zero()
    test_return_20()
    test_return_100()

# Test return 0
def test_return_zero():
     assert value("hello Jeremy") == 0
     assert value("Hello") == 0
     assert value("Hello World") == 0
# Test return 20
def test_return_20():
    assert value("Hi") == 20
    assert value("hey") == 20
# Test return 100
def test_return_100():
     assert value("what's up?") == 100
     assert value("good morning") == 100

if __name__ == "__main__":
    main()
