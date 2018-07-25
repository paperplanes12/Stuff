strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''
flag = False
for x in strings:
    if flag is True:
        sentence += ' '
    sentence += x
    flag = True
print(sentence)
