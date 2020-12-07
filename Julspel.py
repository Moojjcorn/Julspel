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
        while Health >= 0 and Santa >= 0:
            YourAbility1DMG = random.randint(4,6)
            YourAbility2DMG = random.randint(8,13)
            YourMove = 1
            while YourMove == 1:
                print('\n\t[1] Ability 1: Snowball\n\t[2] Ability 2: Icicle\n')
                YourAbility = int(input('Choose Ability: '))
                if YourAbility == 1:
                    Santa = Santa - YourAbility1DMG
                    print(f'\n\tYou did {YourAbility1DMG} damage to Santa with your Snowball\n\tYou have {Health} ❤\n\tSanta has {Santa} ❤')
                elif YourAbility == 2:
                    Santa = Santa - YourAbility2DMG
                    print(f'\n\tYou did {YourAbility2DMG} damage to Santa with your icicle\n\tYou have {Health} ❤\n\tSanta has {Santa} ❤')
                YourMove - 1
            print('Santas move')            
    else:
        print('Invalid input, try again')