ones_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
eleventy_list = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens_list = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def tens_str(x):
    digit2 = x // 10
    digit1 = x % 10

    if digit2 == 0:
        digit_str = ones_list[digit1]
    elif digit2 == 1:
        digit_str = eleventy_list[digit1]
    else:
        digit_str = tens_list[digit2]

        if digit1 != 0:
            digit_str = digit_str + " " + ones_list[digit1]

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
