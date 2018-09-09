"""
Module documentation
Words Go Here
"""

spam = 40

def square(x):

    """这是一个测试"""
    a = 10
    return x ** 2


class Employee:
    "class documentation"
    pass

if __name__=="__main__":
    print(square(4))
    print(square.__doc__)
    import sys
    print(sys.__doc__)