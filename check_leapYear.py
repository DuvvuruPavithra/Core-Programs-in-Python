def check_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    year = int(input("Enter a year: "))
    if check_year(year):
        print("{0} is a Leap Year".format(year))
    else:
        print("{0} is not a Leap Year".format(year))
