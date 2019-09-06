l = lambda x: x > 5

print(l(9))


def alter(values, check):
    return [val for val in values if check(val)]


my_list = [1, 2, 3, 4, 5]
another_list = alter(my_list, lambda x: x != 5)


def check_not_five(x):
    return x != 5


third_list = alter(my_list, check_not_five)


def alter_filter(values, check):
    return list(filter(check, values))


def remove_number(value):
    return alter(value, lambda x: x not in [str(n) for n in range(10)])


print(remove_number("Hell56o"))


def skip_letter(value, letter):
    return alter(value, lambda x: x != letter)
