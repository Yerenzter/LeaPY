# LeaPY
# Created by Yerenzter
# Under the Mozilla Public License 2.0

def leap(year):
    if year % 4 == 0 and year % 100 != 1 or year % 400== 0:
        return f"{year} is a leap year.";
    else:
        return f"{year} is not a leap year.";
