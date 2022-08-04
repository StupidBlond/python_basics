# divide 4 - leap year, divide 100 - not leap year, divide 400 - leap year
program = input("Enter your year:")
year = int(program)
if 1900 < year < 1_000_0000:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
else:
    print("The year does not fit")
