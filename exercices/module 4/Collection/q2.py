import math

def distance(point):
    x, y = point
    return math.sqrt(x**2 + y**2)

# test
print(distance((3, 4)))  # 5.0