class Person:
    pass
class Bird:
    pass
class Student(Person):
    pass

p, s = Person(), Student()
b=Bird()

print("p is instance of Person: ", isinstance(p, Person))
print("s is instance of Person: ", isinstance(s, Person))
print("p is instance of Object: ", isinstance(p, object))
print("p is instance of Bird: ", isinstance(p, Bird))
print("b is instance of Bird: ", isinstance(b, Bird))
print("int is instance of Object: ", isinstance(int, object))