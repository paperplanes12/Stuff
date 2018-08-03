'''
 Exercise 3:
 Given a paragraph of text, 
 1. count the number of times each character occurs in the text, 
   and print out each character and its count (in any order).
 2. do it now in a case-insensitive manner for the alphabets
 3. extension: print in the descending order of the count
'''


def count_char(text):
    pass
    # add your code here
    
    while len(text) != 0:
        char = text[0]
        print(char, text.count(char))
        text = text.replace(char, "")

def count_char_insensitive(text):
    pass
    # add your code here

    text = text.lower()
    
    count_char(text)

# bonus task:
def count_char_ordered(text):
    pass
    
    text = text.lower()
    
    string = ""
    
    while len(text) != 0:
        num = len(text)
        most_repeated = text[0]
        for x in range(1, num):
            char = text[x]
            if text.count(char) > text.count(most_repeated):
                most_repeated = char
            x += 1
        #add this character on to end of string
        string = string + text.count(most_repeated)*most_repeated
        #delete character from text string
        text = text.replace(most_repeated, "")  
    
    count_char(string)
    
    # add your code here 

text1 = 'I felt happy because I saw the others were happy and because I knew I should feel happy but I wasn’t really happy' # Robert Bolano
text2 = 'HellO, WorLd!'

# testing exercise 2
count_char(text2)
count_char_insensitive(text2)
count_char_ordered(text2)

