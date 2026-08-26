from faker import Faker

faker = Faker()
print(faker.password())
print(faker.email())
print(faker.name())
print(faker.last_name())
print(faker.phone_number())
print(faker.sentence())
print(faker.unique.email())

print(faker.unique.numerify("05########"))