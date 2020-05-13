import random

while True:
    print ("Do you want to roll the dice? \n type 'no' to stop \n any digit to roll again")
    a = input().lower()
    if a == 'no':
        import sys
        sys.exit()
    else:
        i = random.randint(1,7)
        if i==1:
            print(r'''
         ___________
        |           |
        |           |
        |     ●     |
        |           |
        |___________|
        ''')
        elif i==2:
            print(r'''
         ___________
        |           |
        |     ●     |
        |           |
        |     ●     |
        |___________|
        ''')
        elif i==3:
            print(r'''
         ___________
        |           |
        |           |
        |   ● ● ●   |
        |           |
        |___________|
        ''')
        elif i==4:
            print(r'''
         ___________
        |           |
        |     ●     |
        |   ●   ●   |
        |     ●     |
        |___________|
        ''')
        elif i==5:
            print(r'''
         ___________
        |           |
        |     ●     |
        |   ● ● ●   |
        |     ●     |
        |___________|

        ''')
        elif i==6:
            print(print(r'''
         ___________
        |           |
        |   ● ● ●   |
        |           |
        |   ● ● ●   |
        |___________|

        '''))
