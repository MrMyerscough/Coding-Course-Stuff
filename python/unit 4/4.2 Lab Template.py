import random

def create_list_from_file(filename='data.txt'):
    collection = []
    with open(filename, 'r') as my_file:
        lines = my_file.readlines()
        for line in lines:
            collection.append(line.strip())
    return collection


def print_list(collection):
    for item in collection:
        print(item)

def shuffle_list(collection):
    new_collection = collection.copy()
    random.shuffle(new_collection)
    return new_collection

def sort_alphabetical(collection):
    new_collection = collection.copy()
    new_collection.sort()
    return new_collection

def random_item(collection):
    return random.choice(collection)

songs = create_list_from_file('songs.txt')

done = False

while not done:
    print('1 - see')
    print('2 - random')
    print('3 - alphabet')
    print('4 - random 1')
    choice = input('Pick an option. ')

    if choice == '1':
        print_list(songs)
    elif choice == '2':
        random_order = shuffle_list(songs)
        print_list(random_order)
    elif choice == '3':
        alphabetical = sort_alphabetical(songs)
        print_list(alphabetical)
    elif choice == '4':
        random_song = random_item(songs)
        print(random_song)
    else:
        print('Not a valid option. \n')