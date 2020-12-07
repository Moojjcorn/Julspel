import random
while True:
    print('\n\t[1] Start \n\t[2] Avsluta\n')
    Choise = int(input('Choose an option: '))
    if Choise == 2:
        print('Quitting...')
        break
    elif Choise == 1:
        print('Loading...')
        print('\n\tYOU vs SANTACLAUS\n\t Who will win? ')
        Health = 100
        Santa = 100
        print(f"\n\tYour Health {Health} ❤\n\tSantaclaus's Health {Santa} ❤")
    else:
        print('Invalid input, try again')