def showInstructions():
    # print the main menu instructions
    print('Neanderthal Text Adventure game')
    print('Collect all 7 Items and defeat the mammoth boss at the end to win.')
    print('Movement commands: go South, go North, go East, go West')
    print("To add item to inventory: get 'item name'")
    print('To fight the boss type: "Fight Mammoth"')
    print('You can choose to restart the game at any time by typing "restart" or "Restart"')


# defines a function to restart the game after you lose or win
def restart():
    restartGame = input("Would you like to play again (yes or y/no or n)? ")
    if restartGame == "yes" or restartGame == "y":
        main()
    if restartGame == "n" or restartGame == "no":
        print("Thank you for playing. Goodbye.")
        exit()
    restart()


# Sets the player status and is called from the main function
def playerStatus(currentRoom, Inventory, rooms):
    print('   -------------------------------------------')
    print('You are in the {}'.format(currentRoom))
    print('You see an item in the room', rooms[currentRoom].get('Item'))
    print('Inventory:', Inventory)
    print('   -------------------------------------------')


# Sets the currentRoom to an empty string
currentRoom = ''
# define the player inventory which starts empty.
Inventory = set()


def main():
    rooms = {
        'Grasslands': {'go South': 'Caves', 'go North': 'Beach', 'go East': 'Icy Forest', 'go West': 'Forest',
                       'Item': 'None'},
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
    # Sets the player in the starter room
    currentRoom = 'Grasslands'

    # Show player the game instructions
    showInstructions()

    # loop forever
    while True:
        # Lets the player know the status of the game
        playerStatus(currentRoom, Inventory, rooms)
        # Gets input from the player for movement, getting items, or fighting the boss
        playerMove = input('Enter your move: ')
        # Checks if the player input is exit to exit the program
        if playerMove in ['Exit', 'exit']:
            currentRoom = 'Exit'
            print('Play again soon!')
            exit()
        # Allows the player to restart the program at any time
        if playerMove in ['Restart', 'restart']:
            Inventory.clear()
            main()
        # Get the item present, or None if there isn't one
        item = rooms[currentRoom].get('Item')
        # Gets input from playerMovement to get an item if there is an item in the room
        # also tells you if you already have the item
        if item != 'None' and playerMove == 'get ' + item:
            if item in Inventory:
                print('You already have this item in your inventory!')
            else:
                Inventory.add(item)
        # Gets input from playerMovement to fight the boss and checks if the player
        # has enough items to win or lose
        if item == 'Mammoth' and playerMove == 'Fight ' + item:
            if item == 7:
                print('You have beaten the great mammoth. Your people thank you.')
                print('Thank you for playing')
                restart()
            else:
                print('The mammoth has beaten you. It heads towards your camp.')
                print('Thank you for playing.')
                restart()
        # Gets input for movement, items, or to fight the boss
        try:
            currentRoom = rooms[currentRoom][playerMove]
        except KeyError:
            print("You can not go that way")
            continue


main()
