def harmonic_series(number):
    # Assigning the value is 0 in harmnic
    harmonic = 0

    # loop to apply the formula
    for i in range(1, number + 1):
        harmonic += 1 / i
    return harmonic
# Driver code
if __name__ == "__main__":
    number = int(input("Enter the Number: "))
    print(harmonic_series(number))



