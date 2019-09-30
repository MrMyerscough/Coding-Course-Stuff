def which_vehicle(number_people):
    if number_people <= 5:
        return 'car'
    elif number_people <= 7:
        return 'van'
    elif number_people <= 30:
        return 'bus'
    else: 
        return 'train'

print( f'you should take a {which_vehicle(48)}' )