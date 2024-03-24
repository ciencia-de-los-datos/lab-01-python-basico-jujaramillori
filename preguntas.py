"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

def read_file(file_csv):
    data = []
    with open(file_csv, newline='') as file:
        for line in file:
            line = line.strip().replace('\t', ' ').split(' ')
            data.append(line)
    return data

file_csv = 'data.csv'
file_csv = read_file(file_csv)
# print(data_csv)


def pregunta_01():
    """
    Retorne la suma de la segunda columna.
   Rta/
    214
    """
    data = read_file(file_csv)
    sum = 0
    for line in data:
        sum += int(line[1])
    return sum

# file_csv = 'data.csv'
# sum_second_column = pregunta_01(file_csv)
# print(sum_second_column)




def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.
    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]
    """
    data= read_file(file_csv)
    letters = {}
    for line in data:
        if line[0] in letters:
            letters[line[0]] += 1
        else:
            letters[line[0]] = 1

    return sorted(letters.items())

# file_csv = 'data.csv'
# letters = pregunta_02(file_csv)
#  print(letters)


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    data= read_file(file_csv)
    sumletters = {}
    for line in data:
        if line[0] in sumletters:
            sumletters[line[0]] += int(line[1])
        else:
            sumletters[line[0]] = int(line[1])
    return sorted(sumletters.items())

# file_csv = 'data.csv'
# sumletters = pregunta_03(file_csv)
# print(sumletters)

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.
    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]
    """
    data= read_file(file_csv)
    months = {}
    for line in data:
        month = line[2].split('-')[1]
        if month in months:
            months[month] += 1
        else:
            months[month] = 1
    return sorted(months.items())

# file_csv = 'data.csv'
# months = pregunta_04(file_csv)
# print(months)


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    data= read_file(file_csv)
    max_min = {}
    for line in data:
        letter = line[0]
        value = int(line[1])
        if letter in max_min:
            if value > max_min[letter][0]:
                max_min[letter] = (value, max_min[letter][1])
            if value < max_min[letter][1]:
                max_min[letter] = (max_min[letter][0], value)
        else:
            max_min[letter] = (value, value)
    return [(k, v[0], v[1]) for k, v in sorted(max_min.items())]

# file_csv = 'data.csv'
# max_min = pregunta_05(file_csv)
# print(max_min)


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    data= read_file(file_csv)
    vmax_min = {}
    for line in data:
        for item in line[4].split(','):
            key, value = item.split(':')
            value = int(value)
            if key in vmax_min:
                if value > vmax_min[key][0]:
                    vmax_min[key] = (value, vmax_min[key][1])
                if value < vmax_min[key][1]:
                    vmax_min[key] = (vmax_min[key][0], value)
            else:
                vmax_min[key] = (value, value)
    return [(k, v[1], v[0]) for k, v in sorted(vmax_min.items())]

# file_csv = 'data.csv'
# vmax_min = pregunta_06(file_csv)
# print(vmax_min)


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.
    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]
    """
    data= read_file(file_csv)
    values = {}
    for line in data:
        key = int(line[1])
        value = line[0]
        if key in values:
            values[key].append(value)
        else:
            values[key] = [value]
    return [(k, v) for k, v in sorted(values.items())]

# file_csv = 'data.csv'
# values = pregunta_07(file_csv)
# print(values)


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.
    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]
    """
    data= read_file(file_csv)
    l_values = {}
    for line in data:
        key = int(line[1])
        value = line[0]
        if key in l_values:
            l_values[key].append(value)
        else:
            l_values[key] = [value]
    return [(k, sorted(list(set(v)))) for k, v in sorted(l_values.items())]

# file_csv = 'data.csv'
# l_values = pregunta_08(file_csv)
# print(l_values)


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.
    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }
    """
    data= read_file(file_csv)
    f_key = {}
    for line in data:
        for item in line[4].split(','):
            key, value = item.split(':')
            if key in f_key:
                f_key[key] += 1
            else:
                f_key[key] = 1
    return dict([(k, v) for k, v in sorted(f_key.items())])

# file_csv = 'data.csv'
# f_key = pregunta_09(file_csv)
# print(f_key)


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.
    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]
    """
    data= read_file(file_csv)
    values_45 = []

    for line in data:
        letter= line[0][0]
        value_4 = len(line[3].split(',')) if len(line) > 3 else 0 
        value_5 = len(line[4].split(',')) if len(line) > 4 else 0
        values_45.append((letter, value_4, value_5))
    return values_45

# file_csv = 'data.csv'
# values_45 = pregunta_10(file_csv)
# print(values_45)


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.
    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    """
    data= read_file(file_csv)
    sum_24 = {}
    for line in data:
        letter_4 = line[3].split(',')
        sum_2 = int(line[1])

        for letter in letter_4:
            if letter in sum_24:
                sum_24[letter] += sum_2
            else:
                sum_24[letter] = sum_2

    return dict(sorted(sum_24.items(), key=lambda x: x[0]))

# file_csv = 'data.csv'
# sum_24 = pregunta_11(file_csv)
# print(sum_24)


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.
    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }
    """
    data= read_file(file_csv)
    sum_15 = {}
    for line in data:
        letter = line[0]
        for item in line[4].split(','):
            key, value = item.split(':')
            value = int(value)
            if letter in sum_15:
                sum_15[letter] += value
            else:
                sum_15[letter] = value
    return dict([(k, v) for k, v in sorted(sum_15.items())])

# file_csv = 'data.csv'
# sum_15 = pregunta_12(file_csv)
# print(sum_15)
