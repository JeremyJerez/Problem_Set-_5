# Python_Intro
# Problem Set 5
#A series of exercises for CS50 hands-on projects
"""
This one's my approach to the "Home Federal Savings Bank" problem
updated for this test
"""
def main():
     greeting = input("Greeting: ")
     cost = value(greeting)
     print(f"${cost}")
 
def value(greeting):
    greeting = greeting.lower().strip()
    if "hello" in greeting:
       return 0
    elif "h" == greeting[0]:
       return 20
    else:
       return 100

if __name__ == "__main__":
    main()
