

if __name__ == '__main__':

    # you can print anything without a line break by using this print function
    # print('🌷', end='')

    print('solid')
    for i in range(11):
        for j in range(11):
            print('🌼', end='')
        print('')

    print('')
    print('horizontal')
    for i in range(11):
        for j in range(11):
            if i % 2 == 0:
                print('🌷', end='')
            else:
                print('🌼', end='')
        print('')

    print('')
    print('vertical')
    for i in range(11):
        for j in range(11):
            if j % 2 == 0:
                print('🌷', end='')
            else:
                print('🌼', end='')
        print('')

    print('')
    print('diagonal')
    for i in range(11):
        for j in range(11):
            if i % 2 == 0 and j % 2 == 0:
                print('🌷', end='')
            elif i % 2 == 1 and j % 2 == 1:
                print('🌷', end='')
            else:
                print('🌼', end='')
        print('')

    print('')
    print('plaid')
    for i in range(11):
        for j in range(11):
            if i % 2 == 0 and j % 2 == 0:
                print('🌷', end='')
            else:
                print('🌼', end='')
        print('')

    print('')
    print('cross')
    for i in range(11):
        for j in range(11):
            # draw the X pattern
            if i == j or j == 11 - i - 1:
                print('🌷', end='')
            else:
                print('🌼', end='')
        print('')
