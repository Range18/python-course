def long_division(dividend, divider):
    '''
    Вернёт строку с процедурой деления «уголком» чисел dividend и divider.
    '''

    quotient = dividend // divider
    remainder = dividend % divider
    dividend_str = str(dividend)
    quotient_str = str(quotient)
    long_division_text = [f"{dividend}|{divider}"]

    last_remainder = 0
    next_num_ind = 0

    if divider > dividend:
        long_division_text.append(dividend_str + "|0")
        return '\n'.join(long_division_text)

    if divider == 1:
        for i in range(len(quotient_str)):
            partial_quotient = int(quotient_str[i]) * divider
            partial_quotient_str = str(partial_quotient)

            if partial_quotient == 0:
                partial_dividend = int(
                    f"{last_remainder}" + dividend_str[next_num_ind])
                last_remainder = partial_dividend
                next_num_ind += 1
                continue

            if i == 0:
                long_division_text.append(
                    f"{partial_quotient}" + ' ' * (len(dividend_str) - len(
                        partial_quotient_str)) + f"|{quotient_str}")
                last_remainder = int(
                    dividend_str[
                    :len(partial_quotient_str)]) - partial_quotient
                next_num_ind = len(partial_quotient_str)
            else:
                partial_dividend = int(
                    f"{last_remainder}" + dividend_str[next_num_ind])
                long_division_text.append(
                    ' ' * (next_num_ind - len(str(last_remainder)) + 1) + str(
                        partial_dividend))
                long_division_text.append(' ' * (next_num_ind - len(
                    str(last_remainder)) + 1) + partial_quotient_str)
                last_remainder = partial_dividend - partial_quotient
                next_num_ind += 1

        long_division_text.append(
            ' ' * (len(dividend_str) - len(str(remainder))) + '0')
        return '\n'.join(long_division_text)

    for i in range(len(quotient_str)):
        partial_quotient = int(quotient_str[i]) * divider
        partial_quotient_str = str(partial_quotient)

        if partial_quotient == 0:
            partial_dividend = int(
                f"{last_remainder}" + dividend_str[next_num_ind])
            last_remainder = partial_dividend
            next_num_ind += 1
            continue

        if i == 0:
            long_division_text.append(
                f"{partial_quotient}" + ' ' * (len(dividend_str) - len(
                    partial_quotient_str)) + f"|{quotient_str}")
            last_remainder = int(
                dividend_str[:len(partial_quotient_str)]) - partial_quotient
            next_num_ind = len(partial_quotient_str)
        else:
            partial_dividend = int(
                f"{last_remainder}" + dividend_str[next_num_ind])
            long_division_text.append(
                ' ' * (next_num_ind - len(str(last_remainder))) + str(
                    partial_dividend))
            long_division_text.append(' ' * (next_num_ind - len(
                str(last_remainder))) + partial_quotient_str)
            last_remainder = partial_dividend - partial_quotient
            next_num_ind += 1

    if len(long_division_text) > 2:
        long_division_text.append(
            ' ' * (len(long_division_text[-1]) - len(str(remainder))) + str(
                remainder))
    elif remainder == 0:
        long_division_text.append(
            ' ' * (len(str(
                int(long_division_text[-1].split("|")[0]))) - 1) + str(
                remainder))
    else:
        long_division_text.append(
            ' ' * (len(long_division_text[0].split('|')[0]) - 1) + str(
                remainder))
    return '\n'.join(long_division_text)


def main():
    print(long_division(123, 123))
    print()
    print(long_division(1, 1))
    print()
    print(long_division(15, 3))
    print()
    print(long_division(3, 15))
    print()
    print(long_division(12345, 25))
    print()
    print(long_division(1234, 1423))
    print()
    print(long_division(87654532, 1))
    print()
    print(long_division(24600, 123))
    print()
    print(long_division(4567, 1234567))
    print()
    print(long_division(246001, 123))
    print()
    print(long_division(123456789, 531))
    print()
    print(long_division(425934261694251, 12345678))
    print()
    print(long_division(100000, 50))


if __name__ == '__main__':
    main()
