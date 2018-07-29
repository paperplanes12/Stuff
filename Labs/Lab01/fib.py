def produceFibsList(n):
    
    result = []
    a, b = 1, 1
    
    if n >= 1:
        result.append(1)
        
    for i in range(n-1):
        tmp = b
        b = a + b
        a = tmp
        result.append(a)
    return result
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
   
