from dataclasses import dataclass
from datetime import date

@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth: date
    subjects: str
    hobbies: str
    picture: str
    current_address: str
    state: str
    city: str

student = User(
    first_name='Luna',
    last_name='Lovegood',
    email='luna_love@test.com',
    gender='Female',
    mobile='7924763817',
    date_of_birth=date(1994, 12, 16),
    subjects='History',
    hobbies='Music',
    picture='image.png',
    current_address='1234 Elm Street, Springfield, Illinois, 62704, USA',
    state='NCR',
    city='Noida'
)