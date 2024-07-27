def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    elif len(str_number) == 1 and number != 0:
        return first
    else:
        return 1


result = get_multiplied_digits(40203)  # 4*(2*(3)))
print(result)

result = get_multiplied_digits(42203950)  # 4*(2*(2*(3*(9*(5)))))
print(result)
