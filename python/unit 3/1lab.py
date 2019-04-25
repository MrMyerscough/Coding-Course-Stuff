names = [
    'John Doe',
    'Phoebe Thomas',
    'Harriet Jones',
    'Zachary Green',
    'Tonya Walsh',
    'Rashid Rahal',
    'Darnell Anthony',
    'Natalie Cross',
    'Beth Potts',
    'Daniel Bush'
]

phones = [
    '(392)102-1693',
    '(102)932-0023',
    '(482)322-1270',
    '(210)934-1822',
    '(102)032-2734',
    '(102)221-9285',
    '(210)784-2312',
    '(304)311-9443',
    '(304)100-3371',
    '(392)018-3473'
]

addresses = [ 
    '12053 Oak St',
    '592 Brooke Rd',
    '3213 9th St',
    '530 Hand Ct',
    '19372 Beverly Ave',
    '47221 Amp Dr',
    '77428 Nancy St',
    '192 Lakeview Blvd',
    '71882 Swan Dr',
    '4800 9th St'
]

emails = [
    'jhd102@email.com',
    'phoebet21@email.net',
    'jopal44@email.com',
    'zeegeegreen@email.edu',
    'supersun004@email.com',
    'rrahal@email.net',
    'darnant5@email.com',
    'neoncross@email.edu',
    'potts99b@email.com',
    'dannyb23@email.net'
]

data = input('enter a name, phone number, address, or email: ')

if data in names:
    index = names.index(data)
    print(names[index])
    print(phones[index])
    print(addresses[index])
    print(emails[index])
elif data in phones:
    index = phones.index(data)
    print(names[index])
    print(phones[index])
    print(addresses[index])
    print(emails[index])
elif data in addresses:
    index = addresses.index(data)
    print(names[index])
    print(phones[index])
    print(addresses[index])
    print(emails[index])
elif data in emails:
    index = emails.index(data)
    print(names[index])
    print(phones[index])
    print(addresses[index])
    print(emails[index])
else:
    print('A contact with that information does not exist.')