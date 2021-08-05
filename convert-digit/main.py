ones_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
eleventy_list = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens_list = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def tens_str(x):
    digit2 = x // 10
    digit1 = x % 10

    if digit2 == 0:
        return ones_list[digit1]
    if digit2 == 1:
        return eleventy_list[digit1]
    if digit1 == 0
        return tens_list[digit2]

    return tens_list[digit2] + " " + ones_list[digit1]


def hundreds_str(x):
    digit3 = x // 100
    rest = x % 100

    if digit3 == 0:
        return tens_str(rest)

    if rest == 0:
        return ones_list[digit3] + " hundred"

    return ones_list[digit3] + " hundred and " + tens_str(rest)


def thousands_str(x):
    digit4 = x // 1000
    rest = x % 1000

    if digit4 == 0:
        return hundreds_str(rest)

    if rest == 0:
        return ones_list[digit4] + " thousand"

    return ones_list[digit4] + " thousand and " + hundreds_str(rest)


given_number_str = input("enter a number : ")
given_number = int(given_number_str)

print(thousands_str(given_number))
