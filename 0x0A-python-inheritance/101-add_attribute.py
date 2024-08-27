#!/usr/bin/python3

def add_attribute(obj, attr1, attr2):
    if hasattr(obj, '__dict__'):
        setattr(obj, attr1, attr2)
    else:
        raise TypeError("can't add new attribute")


class MyClass():
    pass

mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))