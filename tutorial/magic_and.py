class vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __and__(self, other):
        return vector2d(self.x & other.x, self.y & other.y)

first = vector2d(True, False)
print(first.x, first.y)
second = vector2d(True, True)
print(second.x, second.y)
result = first & second
print(result.x, result.y)