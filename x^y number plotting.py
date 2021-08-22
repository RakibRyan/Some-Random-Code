import time
import sys

print("X^Y Number plotting")
print("Plot automatically adjusts to fit in console\n")

base_number = 0
exponent_number = 0

enter = True
while enter:
    base_input = input('Base Number: ')
    exponent_input = input('Exponent Number: ')

    try:
        base_number = int(base_input)
        exponent_number = float(exponent_input)
        enter = False
    except ValueError:
        print('What you entered is not a number')


def number_to_exponent(number, exponent):
    max_value = pow(number, exponent)
    line_per_value = 140 / max_value
    for i in range(number + 1):
        result = pow(i, exponent)
        graph_length = round(line_per_value * result)
        loading_animation = (f'|{i:02}|' + '#' * graph_length + '  ({0:.2f})'.format(result))
        for l in loading_animation:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(0.1)
        print('')
        # print(loading_animation)


number_to_exponent(base_number, exponent_number)
