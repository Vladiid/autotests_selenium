from data.data import Person
from faker import Faker

faker = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker.first_name() + " " + faker.last_name() + " " + faker.middle_name(),
        email=faker.email(),
        current_address=faker.address(),
        permanent_address=faker.address()
    )
