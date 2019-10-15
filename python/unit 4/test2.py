def function(arg_one, arg_two, arg_three, arg_four, arg_five):
    print(arg_one)
    print(arg_two)
    print(arg_three)
    print(arg_four)
    print(arg_five)
    return

# function(12, 67, 324, 7, 34)

# function(12, arg_three=12, arg_four=7, arg_five=34, arg_two=67)

def list_printer(collection:list):
    for item in collection:
        print(item)




def argument_counter(*args):
    length = len(args)
    print(f'there are {length} arguments.')
    print('the first argument is', args[0])
    print('here are the rest:')
    for arg in args[1:]:
        print(arg)


def add(number, number2):
    """Return the sum of two numbers.
    
    Keyword arguments:
    number -- the first number to total
    number2 -- the second number to total
    """
    return number + number2

def arb(arg1, list, *arb):
    print(arg1)
    print(arb)

def double(collection):
    for index in range(len(collection)):
        collection[index] = collection[index] * 2
    return collection

x = [1,2,3]

y = double(x)


def alphabetize(collection:list, capitalize=False, reverse_alphabetize=False):
    """Return an alphabetized list given an unordered one."""
    new_collection = collection.copy()

    if capitalize:
        for item in range(len(new_collection)):
            new_collection[item] = new_collection[item].capitalize()
            
    new_collection.sort()

    if reverse_alphabetize:
        new_collection.reverse()

    return new_collection

x = ['dog', 'cat', 'tiger', 'hamster', 'otter']

y = alphabetize(x, reverse_alphabetize=True)

print(y)