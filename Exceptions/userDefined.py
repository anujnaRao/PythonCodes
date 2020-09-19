class Error(Exception):
    """ Base class """
    pass

class ValueIsTooSmallError(Error):
    """ Smaller than actual value """
    pass

class ValueIsTooLargeError(Error):
    """ Larger than actual value """
    pass

number = 20
while True:
    try:
        num = int(input("Guess the number:"))
        if num < number:
            raise ValueIsTooSmallError
        elif num > number:
            raise ValueIsTooLargeError
        break

    except ValueIsTooSmallError:
        print("Value is lesser than the actual")


    except ValueIsTooLargeError:
        print("Value is greater than the actual")

print("Yayy! You guesses the right number")
