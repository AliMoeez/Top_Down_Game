def func(x,y):
    return x+y, x,y


def func_2():
    return func(2,3)

def func_3():
    x=func_2()[1:]
    print(x[1])



func_3()