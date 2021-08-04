def ones_str(x):
    if x == 0:
        digit_str = ""
    if x == 1:
        digit_str = "one"
    if x == 2:
        digit_str = "two"
    if x == 3:
        digit_str = "three"
    if x == 4:
        digit_str = "four"
    if x == 5:
        digit_str = "five"
    if x == 6:
        digit_str = "six"
    if x == 7:
        digit_str = "seven"
    if x == 8:
        digit_str = "eight"
    if x == 9:
        digit_str = "nine"
    return digit_str


def tens_str(x):
    if x == 0:
        digit_str = ""
    if x == 1:
        if digit1 == 0:
            digit_str = "ten"
        if digit1 == 1:
            digit_str = "eleven"
        if digit1 == 2:
            digit_str = "twelve"
        if digit1 == 3:
            digit_str = "thirteen"
        if digit1 == 4:
            digit_str = "fourteen"
        if digit1 == 5:
            digit_str = "fifteen"
        if digit1 == 6:
            digit_str = "sixteen"
        if digit1 == 7:
            digit_str = "seventeen"
        if digit1 == 8:
            digit_str = "eighteen"
        if digit1 == 9:
            digit_str = "nineteen"
    if x == 2:
        digit_str = "twenty"
    if x == 3:
        digit_str = "thity"
    if x == 4:
        digit_str = "forty"
    if x == 5:
        digit_str = "fifty"
    if x == 6:
        digit_str = "sixty"
    if x == 7:
        digit_str = "seventy"
    if x == 8:
        digit_str = "eighty"
    if x == 9:
        digit_str = "ninety"
    return digit_str


def hundreds_str(x):
    if x == 0:
        digit_str = ""
    if x == 1:
        digit_str = "one hundred"
    if x == 2:
        digit_str = "two hundred"
    if x == 3:
        digit_str = "three hundred"
    if x == 4:
        digit_str = "four hundred"
    if x == 5:
        digit_str = "five hundred"
    if x == 6:
        digit_str = "six hundred"
    if x == 7:
        digit_str = "seven hundred"
    if x == 8:
        digit_str = "eight hundred"
    if x == 9:
        digit_str = "nine hundred"
    return digit_str


def thousands_str(x):
    if x == 0:
        digit_str = ""
    if x == 1:
        digit_str = "one thousand"
    if x == 2:
        digit_str = "two thousand"
    if x == 3:
        digit_str = "three thousand"
    if x == 4:
        digit_str = "four thousand"
    if x == 5:
        digit_str = "five thousand"
    if x == 6:
        digit_str = "six thousand"
    if x == 7:
        digit_str = "seven thousand"
    if x == 8:
        digit_str = "eight thousand"
    if x == 9:
        digit_str = "nine thousand"
    return digit_str


given_number_str = input("enter a number : ")
given_number = int(given_number_str)
original_number = given_number

digit1 = given_number % 10

given_number = given_number // 10
digit2 = given_number % 10

given_number = given_number // 10
digit3 = given_number % 10

given_number = given_number // 10
digit4 = given_number % 10


if original_number < 10:
        if digit1 < 1:
                print("zero")
        else:
                print(ones_str(digit1))

elif original_number < 100:
        if digit2 < 2:
                print(tens_str(digit2))
        elif digit1 == 0:
                print(tens_str(digit2))
        else:
                print(tens_str(digit2) + " " + ones_str(digit1))

elif original_number < 1000:
        if digit1 == digit2 == 0:
                print(hundreds_str(digit3))
        elif digit2 == 0:
                print(hundreds_str(digit3) + " and " + ones_str(digit1))
        elif digit2 < 2 and digit2 > 0:
                print(hundreds_str(digit3) + " and " + tens_str(digit2))
        else:
                if digit1 == 0:
                        print(hundreds_str(digit3) + " and " + tens_str(digit2))
                else:
                        print(hundreds_str(digit3) + " and " + tens_str(digit2) + " " + ones_str(digit1))

elif original_number < 10000:
        if digit1 == digit2 == digit3 == 0:
                print(thousands_str(digit4))
        elif digit2 == digit3 == 0:
                print(thousands_str(digit4) + " and " + ones_str(digit1))
        elif digit3 == 0:
                if digit2 < 2 or digit1 == 0:
                        print(thousands_str(digit4) + " and " + tens_str(digit2))
                else:
                        print(thousands_str(digit4) + " and " + tens_str(digit2) + " " + ones_str(digit1))
        elif digit1 == digit2 == 0:
                print(thousands_str(digit4) + " and " + hundreds_str(digit3))
        elif digit2 == 0:
                print(thousands_str(digit4) + " and " + hundreds_str(digit3) + " and " + ones_str(digit1))
        else:
                if digit2 < 2 or digit1 == 0:
                        print(thousands_str(digit4) + " and " + hundreds_str(digit3) + " and " + tens_str(digit2))
                else:
                        print(thousands_str(digit4) + " and " + hundreds_str(digit3) + " and " + tens_str(digit2) + " " + ones_str(digit1))
