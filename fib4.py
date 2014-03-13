def f():
    a=0
    b=1
    c=1
    for i in range(100):
        print(c)
        c=a+b
        a=b
        b=c
print(f())
