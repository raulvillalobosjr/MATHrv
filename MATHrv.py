def count(*args):
    return(len(args))
    
def add(*args):
    sum = 0
    for num in args:
        sum += float(num)
    return sum
    
print(add(3, 3, 33.2, 3.4))