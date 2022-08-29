# Python_Intro
# Problem Set 5
#A series of exercises for CS50 hands-on projects
"""
This one"s my approach to the "Fuel Gauge" problem
updated for this problem
"""
def main():
    fraction = input("Fraction: ")
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
    print(output)

def convert(fraction):
    while True:
        try:
            numerator, denominator =fraction.split("/")
            new_numerator = int (numerator)
            new_denominator = int(denominator)
            f = new_numerator / new_denominator
            if f <= 1:
                p = int(f * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError,ZeroDivisionError):
                raise

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()
