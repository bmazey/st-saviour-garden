

if __name__ == '__main__':

    # print without a line break using this function
    print('🌷', end='')
    plant = "🌸"

    print("SOLID PATTERN")
    for i in range(11): 
        for j in range (11):
            print(plant, end= "")
        print('')

    print("\nHoRIZONTAL PATTERN")
    for i in range (11):
        for j in range (11):
            if i % 2 == 0:
                print(plant, end="")
            else:
                print('🌻', end="")
        print('')

    print("\VERTICAL PATTERN")
    for i in range (11):
        for j in range (11):
            if j % 2 == 0: 
                print(plant, end="")
            else: 
                print("🌺", end="")
        print()

    print('diagonal')
    for i in range (11):
        for j in range (11): 
            if i % 2 == 0 and j % 2 == 0:
                print (plant ,end="") 
            elif i % 2 == 1 and j % 2 == 1:
                print(plant , end= "")
            else:print ("🍀",end="")
                 