def handle_number(num_1, num_2, num_3):
    counter = 0
    for num in range(num_1, num_2+1):
        if num / num_3 == num // num_3:
            counter += 1
    return counter


def handle_string(value):
    letters = 0
    digits = 0
    for val in value:
        if val.isalpha():
            letters += 1
        elif val.isdigit():
            digits += 1
    return letters, digits


def handle_list_of_tuples_1(list_of_tuples):
    return sorted(list_of_tuples)
