import sys

def text_analyzer(*args):
    a = len(args)
    if a < 1:
        print('What is the text to analyse ?')
        text = input();
    if a > 1:
        print("ERROR")
        quit()
    text = args[0]
    total = len(text)
    lower = 0
    upper = 0
    space = 0
    punc = 0
    for i in text:
        if (i.islower()) == True :
            lower += 1
        elif (i.isupper()) == True :
            upper += 1
        elif i == ' ':
             space += 1
        elif i == '.' or i == ',':
            punc += 1
    print('The text contains', total, 'characters:')
    if upper != 0:
        print('- ', upper, 'upper letters')
    if lower != 0:
        print('- ',lower, 'lower letters')
    if punc != 0:
        print('- ', punc, 'punctation marks')
    if space != 0:
        print('- ', space, 'spaces')
