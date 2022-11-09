from math import sqrt


def max_length(length, heigths):
    if 1 < length < 100 and len(heigths) < 50:
        if len(heigths) == 1:
            return 0 
        first = heigths[0]
        heigths.pop(0)
        return sqrt(((first - heigths[0]) * (-1)) * ((first - heigths[0]) * (-1)) + length ** 2) + max_length(length, heigths)




















def get_wire_length(pillars, length):
    if len(pillars) == 1:
        return 0
    first = pillars[0]
    pillars.pop(0)
    return sqrt(((first - pillars[0]) * (-1)) * ((first - pillars[0]) * (-1)) +length ** 2) + get_wire_length(pillars, length)


print("{:.2f}".format(max_length(2, [3, 1 , 3])))