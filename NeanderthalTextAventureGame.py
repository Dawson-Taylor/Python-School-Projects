def showInstructions():
    # print the main menu instructions
    print('Neanderthal Text Adventure game')
    print('Collect all 7 Items and defeat the mammoth boss at the end to win.')
    print('Movement commands: go South, go North, go East, go West')
    print("To add item to inventory: get 'item name'")
    print('To fight the boss type: "Fight Mammoth"')
    print('You can choose to restart the game at any time by typing "restart" or "Restart"')


def restart():

    restartGame = input("Would you like to play again (yes or y/no or n)? ")
    if restartGame == "yes" or restartGame == "y":
        main()
    if restartGame == "n" or restartGame == "no":
        print("Thank you for playing. Goodbye.")
        exit()
    restart()


def playerStatus(currentRoom, Inventory, rooms):
    print('   -------------------------------------------')
    print('You are in the {}'.format(currentRoom))
    print('You see an item in the room', rooms[currentRoom].get('Item'))
    print('Inventory:', Inventory)
    print('   -------------------------------------------')


currentRoom = ''
# define the player inventory which starts empty.
Inventory = set()


def main():
    rooms = {
        'Grasslands': {'go South': 'Caves', 'go North': 'Beach', 'go East': 'Icy Forest', 'go West': 'Forest', 'Item': 'None'},
        'Caves': {'go North': 'Grasslands', 'go West': 'Rocky Plateau', 'Item': 'Cave Moss Helmet'},
        'Beach': {'go South': 'Grasslands', 'go East': 'Camp', 'go West': 'Mountains', 'Item': 'Seashell Boots'},
        'Icy Forest': {'go North': 'Camp', 'go East': 'Mammoth Fields', 'go West': 'Grasslands', 'Item': 'Icy Shield'},
        'Forest': {'go North': 'Mountains', 'go East': 'Grasslands', 'go South': 'Rocky Plateau',
                   'Item': 'Leafy Chestplate'},
        'Mountains': {'go South': 'Forest', 'go East': 'Beach', 'Item': 'Rock Club'},
        'Rocky Plateau': {'go North': 'Forest', 'go East': 'Caves', 'Item': 'Rocky Leggings'},
        'Camp': {'go West': 'Beach', 'go South': 'Icy Forest', 'Item': 'Fire Stick'},
        'Mammoth Fields': {'go West': 'Icy Forest', 'Item': 'Mammoth'}
    }
    currentRoom = 'Grasslands'

    # Show player the game instructions
    showInstructions()

    # loop forever
    while True:

        playerStatus(currentRoom, Inventory, rooms)
        playerMove = input('Enter your move: ')
        if playerMove in ['Exit', 'exit']:
            currentRoom = 'Exit'
            print('Play again soon!')
            exit()

        item = rooms[currentRoom].get('Item')  # get the item present, or None if there isn't one
        if item != 'None' and playerMove == 'get ' + item:
            if item in Inventory:
                print('You already have this item in your inventory!')
            else:
                Inventory.add(item)
        if item == 'Mammoth' and playerMove == 'Fight ' + item:
            if item == 7:
                print('You have beaten the great mammoth. Your people thank you.')
                print('Thank you for playing')
                restart()
            else:
                print('The mammoth has beaten you. It heads towards your camp.')
                print('Thank you for playing.')
                restart()
        if playerMove == 'Restart' or 'restart':
            main()
        else:
            continue

        try:
            currentRoom = rooms[currentRoom][playerMove]
        except KeyError:
            print("You can not go that way")
            continue


main()
