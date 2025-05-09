from selene import browser, be, have, command
from model import resource
from model.data.users import User


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[name="gender"]')
        self.mobile = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.all('.custom-checkbox')
        self.picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#state')
        self.city = browser.element('#city')
        self.submit_button = browser.element('#submit')

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        self.first_name.should(be.blank).type(value)
        return self


    def fill_last_name(self, value):
        self.last_name.should(be.blank).type(value)
        return self

    def fill_email(self, value):
        self.email.should(be.blank).type(value)
        return self

    def fill_gender(self, value):
        self.gender.element_by(have.value(value)).element('..').click()
        return self

    def fill_number(self, value):
        self.mobile.should(be.blank).type(value)
        return self

    def fill_date(self, date):
        self.date_of_birth.click()
        browser.element('.react-datepicker__month-select').click().element(f'[value="{date.month - 1}"]').click()
        browser.element('.react-datepicker__year-select').click().element(f'[value="{date.year}"]').click()
        browser.all('.react-datepicker__day').element_by(have.exact_text(str(date.day))).click()
        return self

    def fill_subjects(self, value):
        self.subjects.should(be.blank).type(value).press_enter()
        return self

    def fill_hobbies(self, value):
        self.hobbies.element_by(have.exact_text(value)).click()
        return self

    def upload_img(self, filename):
        self.picture.set_value(resource.path(filename))
        return self

    def fill_current_address(self, value):
        self.current_address.should(be.blank).type(value)
        return self

    def fill_state(self, value):
        self.state.click()
        browser.element('#react-select-3-input').set_value(value).press_tab()
        return self

    def fill_city(self, value):
        self.city.click()
        browser.element('#react-select-4-input').set_value(value).press_enter()
        return self

    def submit(self):
        self.submit_button.click()
        return self

    def should_have_title(self, value):
        browser.element('#example-modal-sizes-title-lg').should(
            have.exact_text(value))
        return self

    def register(self, student: User):
        return (self.fill_first_name(student.first_name)
        .fill_last_name(student.last_name)
        .fill_email(student.email)
        .fill_gender(student.gender)
        .fill_number(student.mobile)
        .fill_date(student.date_of_birth)
        .fill_subjects(student.subjects)
        .fill_hobbies(student.hobbies)
        .upload_img(student.picture)
        .fill_current_address(student.current_address)
        .fill_state(student.state)
        .fill_city(student.city)
        .submit())


    def should_have_data(self, student: User):
        full_date = student.date_of_birth.strftime('%d %B,%Y')

        browser.element('.table').all('tr').should(
            have.exact_texts(
                'Label Values',
                f'Student Name {student.first_name} {student.last_name}',
                f'Student Email {student.email}',
                f'Gender {student.gender}',
                f'Mobile {student.mobile}',
                f'Date of Birth {full_date}',
                f'Subjects {student.subjects}',
                f'Hobbies {student.hobbies}',
                f'Picture {student.picture}',
                f'Address {student.current_address}',
                f'State and City {student.state} {student.city}'
            )
        )
        return self

















