def showInstructions():
    # print the main menu instructions
    print('Neanderthal Text Adventure game')
    print('Collect all 7 Items and defeat the mammoth boss at the end to win.')
    print('Movement commands: go South, go North, go East, go West')
    print("To add item to inventory: get 'item name'")
    print('To fight the boss type: "Fight Mammoth"')


def restart():

    restartGame = input("Would you like to play again?")
    if restartGame == "yes" or restartGame == "y":
        main()
    if restartGame == "n" or restartGame == "no":
        print("Thank you for playing. Goodbye.")
        exit()
    restart()


def player_stat(currentRoom, Inventory, rooms):
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
        'Grasslands': {'South': 'Caves', 'North': 'Beach', 'East': 'Icy Forest', 'West': 'Forest', 'Item': 'None'},
        'Caves': {'North': 'Grasslands', 'West': 'Rocky Plateau', 'Item': 'Cave Moss Helmet'},
        'Beach': {'South': 'Grasslands', 'East': 'Camp', 'West': 'Mountains', 'Item': 'Seashell Boots'},
        'Icy Forest': {'North': 'Camp', 'East': 'Mammoth Fields', 'West': 'Grasslands', 'Item': 'Icy Shield'},
        'Forest': {'North': 'Mountains', 'East': 'Grasslands', 'South': 'Rocky Plateau',
                   'Item': 'Leafy Chestplate'},
        'Mountains': {'South': 'Forest', 'East': 'Beach', 'Item': 'Rock Club'},
        'Rocky Plateau': {'North': 'Forest', 'East': 'Caves', 'Item': 'Rocky Leggings'},
        'Camp': {'West': 'Beach', 'South': 'Icy Forest', 'Item': 'Fire Stick'},
        'Mammoth Fields': {'West': 'Icy Forest', 'Item': 'Mammoth'}
    }
    currentRoom = 'Grasslands'

    # Show player the game instructions
    showInstructions()

    # loop forever
    while True:

        player_stat(currentRoom, Inventory, rooms)
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

        try:
            currentRoom = rooms[currentRoom][playerMove]
        except KeyError:
            print("You can not go that way")
            continue


main()
