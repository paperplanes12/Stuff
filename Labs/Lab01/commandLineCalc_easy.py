def calculate(s):
    
    for c in s:
        if c.isalpha(): 
            return None
    else:
        return eval(s)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

