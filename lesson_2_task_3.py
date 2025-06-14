import math
def square(side):
    area = side * side
    return math.ceil(area) if not isinstance(side, int) else area
print(square(3.2))