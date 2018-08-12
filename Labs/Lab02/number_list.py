def find_reverse(numbers):
    #TODO: find the reverse of the list
    return list(reversed(numbers))
    #pass

def find_max(numbers):
    #TODO: find the maximum of the list
    
    return max(numbers)
    
    #pass

def find_min(numbers):
    #TODO: find the minimum of the list
    
    return min(numbers) 
    
    #pass

def find_sum(numbers):
    #TODO: find the sum of all the numbers in the list
    
    return sum(numbers)
    
    #pass

def find_average(numbers):
    #TODO: find the average of all the numbers in the list
    
    
    return sum(numbers)/len(numbers)
    
    #pass

def find_descending(numbers):
    #TODO: numbers sorted in descending order
    
    numbers.sort(reverse=True)
    
    return numbers
    #pass

def second_smallest(numbers):
    #TODO: find the second smallest
    
    minimum = find_min(numbers)
    
    while minimum in numbers:
        numbers.remove(minimum)
    
    new_minimum = find_min(numbers)
    
    return new_minimum
    
    #pass


'''
 bonus task:
 a function that takes in a list of numbers, and an index 'k' 
 and prints the kth smallest number in the list
'''
def kth_smallest(numbers, k):
    #TODO: find the kth smallest number in the list
    
    for i in range(1, k):
        minimum = min(numbers)
        while minimum in numbers:
            numbers.remove(minimum)
        i += 1    
    
    number = min(numbers)
    
    return number
    
    #pass
