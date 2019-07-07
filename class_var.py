class data:
    integer = "integer"
    string = "string"
    _integer = "_integer"
    _string = "_string"
    __integer = "__integer"
    __string = "__string"
print(data().integer)
print(data()._integer)
print(data().string)
print(data()._string)
try:
    print(data().__integer)
except:
    print("error print __integer")
try:
    print(data().__string)
except:
    print("error print __string")