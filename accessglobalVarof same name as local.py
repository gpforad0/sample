x=13

def fun():
    x=26
    y= globals()['x']
    return x+y

result=fun()
print(result)
