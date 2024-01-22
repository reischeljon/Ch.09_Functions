'''This function determines the hypotonuse of a rectangle'''


def hyp(leg1, leg2):
    hypo = leg1**2+leg2**2
    return hypo


hypot = hyp(6, 8)
print(hypot)

'''This function determines the mean of 3 number'''


def mean(a, b, c):
    total = a+b+c
    sum = total / 3
    return sum


m = mean(15, 10, 19)
print(m)

'''This function determines the perimeter of a rectangle'''


def perimeter(base, height):
    total_base = base*2
    total_height = height*2
    sum = total_height+total_base
    return sum


base_height = perimeter(8, 9)
print(base_height)