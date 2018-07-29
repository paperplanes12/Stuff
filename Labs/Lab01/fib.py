def produceFibsList(n):
    
    a = int(1)
    
    if n == 0:
        print()
    elif n == 1:
        print(a)
    elif n > 1:
        while n >= 0:
            print(produceFibsList(n) + ProduceFibsList(n-1))
        n =-1
    
    pass
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
