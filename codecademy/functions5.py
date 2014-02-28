def cube(n):
    return n**3

def by_three(n):
    if n%3 == 0:
        return cube(n)
    else:
        return False
