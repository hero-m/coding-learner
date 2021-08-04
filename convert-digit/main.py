ones_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
eleventy_list = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens_list = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def ones_str(x):
    return ones_list[x]


def eleventy_str(x):
    return eleventy_list[x]


def tens_str(x):
    digit2 = x // 10
    digit1 = x % 10

    if digit2 == 0:
        digit_str = ones_str(digit1)
    elif digit2 == 1:
        digit_str = eleventy_str(digit1)
    else:
        digit_str = tens_list[digit2]

        if digit1 != 0:
            digit_str = digit_str + " " + ones_str(digit1)

    return digit_str


def hundreds_str(x):
    digit3 = x // 100
    rest = x % 100

    if digit3 == 0:
        digit_str = tens_str(rest)
    else:
        digit_str = ones_list[digit3] + " hundred"

        if rest != 0:
            digit_str = digit_str + " and " + tens_str(rest)

    return digit_str


def thousands_str(x):
    digit4 = x // 1000
    rest = x % 1000

    if digit4 == 0:
        digit_str = hundreds_str(rest)
    else:
        digit_str = ones_list[digit4] + " thousand"

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
