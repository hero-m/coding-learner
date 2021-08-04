def ones_str(x):
    if x == 0:
        digit_str = "zero"
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


def eleventy_str(x):
    if x == 0:
        digit_str = "ten"
    if x == 1:
        digit_str = "eleven"
    if x == 2:
        digit_str = "twelve"
    if x == 3:
        digit_str = "thirteen"
    if x == 4:
        digit_str = "fourteen"
    if x == 5:
        digit_str = "fifteen"
    if x == 6:
        digit_str = "sixteen"
    if x == 7:
        digit_str = "seventeen"
    if x == 8:
        digit_str = "eighteen"
    if x == 9:
        digit_str = "nineteen"
    return digit_str


def tens_str(x):
    digit2 = x // 10
    digit1 = x % 10

    if digit2 == 0:
        digit_str = ones_str(digit1)
    elif digit2 == 1:
        digit_str = eleventy_str(digit1)
    else:
        if digit2 == 2:
            digit_str = "twenty"
        if digit2 == 3:
            digit_str = "thity"
        if digit2 == 4:
            digit_str = "forty"
        if digit2 == 5:
            digit_str = "fifty"
        if digit2 == 6:
            digit_str = "sixty"
        if digit2 == 7:
            digit_str = "seventy"
        if digit2 == 8:
            digit_str = "eighty"
        if digit2 == 9:
            digit_str = "ninety"

        if digit1 != 0:
            digit_str = digit_str + " " + ones_str(digit1)

    return digit_str


def hundreds_str(x):
    digit3 = x // 100
    rest = x % 100

    if digit3 == 0:
        digit_str = tens_str(rest)
    else:
        if digit3 == 1:
            digit_str = "one hundred"
        if digit3 == 2:
            digit_str = "two hundred"
        if digit3 == 3:
            digit_str = "three hundred"
        if digit3 == 4:
            digit_str = "four hundred"
        if digit3 == 5:
            digit_str = "five hundred"
        if digit3 == 6:
            digit_str = "six hundred"
        if digit3 == 7:
            digit_str = "seven hundred"
        if digit3 == 8:
            digit_str = "eight hundred"
        if digit3 == 9:
            digit_str = "nine hundred"

        if rest != 0:
            digit_str = digit_str + " and " + tens_str(rest)

    return digit_str


def thousands_str(x):
    digit4 = x // 1000
    rest = x % 1000

    if digit4 == 0:
        digit_str = hundreds_str(rest)
    else:
        if digit4 == 1:
            digit_str = "one thousand"
        if digit4 == 2:
            digit_str = "two thousand"
        if digit4 == 3:
            digit_str = "three thousand"
        if digit4 == 4:
            digit_str = "four thousand"
        if digit4 == 5:
            digit_str = "five thousand"
        if digit4 == 6:
            digit_str = "six thousand"
        if digit4 == 7:
            digit_str = "seven thousand"
        if digit4 == 8:
            digit_str = "eight thousand"
        if digit4 == 9:
            digit_str = "nine thousand"

        if rest != 0:
            digit_str = digit_str + " and " + hundreds_str(rest)

    return digit_str


given_number_str = input("enter a number : ")
given_number = int(given_number_str)

print(thousands_str(given_number))
quit()

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
