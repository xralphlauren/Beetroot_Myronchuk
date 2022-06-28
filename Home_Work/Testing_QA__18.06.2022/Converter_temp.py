import doctest


def converter(T):
    '''
    Данная функция предназначена для конвертации температуры из фаренгейт в цельсий и обратно.
    Функции на вход подаётся строка в виде 50T, 115F. По последнему символу функция определяет какая именно темпера -
    тура поступает на вход и изходя из этого подставляет нужную формулу

    >>> converter('99F')
    (37, 'C', '37C')

    >>> converter('37C')
    (99, 'F', '99F')
    '''
    measure = T[-1]
    degree = int(T[:-1])
    if measure.upper() == "C":
        result = int(round((9 * degree) / 5 + 32))
        out_measure = "F"
    elif measure.upper() == "F":
        result = int(round((degree - 32) * 5 / 9))
        out_measure = "C"
    else:
        raise ValueError("Input proper convention")
    return result, out_measure, f'{result}{out_measure}'



