

""" this is functions file"""

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        return "Error"
    else:
        return a/b

print(__name__)
if __name__ == '__main__': # למנוע הרצה מרחוק של הקוד . רק לוקאלי!!!
    print(__name__)
    print(add(6,6))
    print(div(12,3))