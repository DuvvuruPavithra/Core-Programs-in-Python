def prime_fact(number):
    # storing the values in prime factors
    prime_factors = []
    # prime numbers starting value is 2
    divisor = 2
    # Longest value of the device that is less than or equal to number
    while divisor <= number:
        # value of number is modulo by divisor values that is equals to zero
        if number%divisor == 0:
            # we can add the values in prime factors
            prime_factors.append(divisor)
            number = number/divisor
        else:
            divisor += 1
    return prime_factors

if __name__ == "__main__":
    number = int(input("Enter the Number: "))
    print(prime_fact(number))






