#This is a python code to generate random values of names, address,email, phone number etc.

import random

first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']

last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']

fake_cities = ['Metropolis', 'Dragonstone', "King's Landing", 'Hogwarts', 'Pandora', 'Gotham', 'Atlantis', 'Mordor', 'Olympus', 'Meluha', 'Rivendell', 'Gotham', 'Lilliput', 'Narnia', 'Smalltown', 'The Shire', 'Malgudi', 'Asgard', 'Westworld', 'Neverland', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos‎', 'Central Perk']

for num in range(10):
    first = random.choice(first_names)
    last = random.choice(last_names)

    phone = f'{random.randint(666, 999)}-{random.randint(100,999)}-{random.randint(1000,9999)}'

    address = random.choice(fake_cities) 

    pincode = random.randint(100000,999999)

    email = first.lower() + last.lower() + '@hotmail.com'

    print(f'{first} {last}\n{phone}\n{address}, {pincode}\n{email}\n')
