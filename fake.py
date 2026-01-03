from faker import Faker

fake = Faker('en_IN')

for i in range(5):
    print(fake.name())
    print(fake.email())
    print(fake.address())
    print(fake.phone_number())
    print(fake.job())
    print('-'*20)