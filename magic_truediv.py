class specialstr:
    def __init__(self, cont):
        self.cont = cont
    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = specialstr("spam")
hello = specialstr("Hello World!")
print(spam/hello)