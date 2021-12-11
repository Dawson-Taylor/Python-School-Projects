def showInstructions():
    # print the main menu instructions
    print('Neanderthal Text Adventure game')
    print('Collect all 7 Items and defeat the mammoth boss at the end to win.')
    print('Movement commands: go South, go North, go East, go West')
    print("To add item to inventory: get 'item name'")
    print('To fight the boss type: "Fight Boss"')


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
        'Grasslands': {'go South': 'Caves', 'go North': 'Beach', 'go East': 'Icy Forest', 'go West': 'Forest', 'Item': 'None'},
        'Caves': {'go North': 'Grasslands', 'go West': 'Rocky Plateau', 'Item': 'Cave Moss Helmet'},
        'Beach': {'go South': 'Grasslands', 'go East': 'Camp', 'go West': 'Mountains', 'Item': 'Seashell Boots'},
        'Icy Forest': {'go North': 'Camp', 'go East': 'Mammoth Fields', 'go West': 'Grasslands', 'Item': 'Icy Shield'},
        'Forest': {'go North': 'Mountains', 'go East': 'Grasslands', 'go South': 'Rocky Plateau',
                   'Item': 'Leafy Chestplate'},
        'Mountains': {'go South': 'Forest', 'go East': 'Beach', 'Item': 'Rock Club'},
        'Rocky Plateau': {'go North': 'Forest', 'go East': 'Caves', 'Item': 'Rocky Leggings'},
        'Camp': {'go West': 'Beach', 'go South': 'Icy Forest', 'Item': 'Fire Stick'},
        'Mammoth Fields': {'go West': 'Icy Forest', 'Fight Boss': 'Mammoth'}
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
        try:
            currentRoom = rooms[currentRoom][playerMove]
        except KeyError:
            print("invalid move")
            continue



main()
