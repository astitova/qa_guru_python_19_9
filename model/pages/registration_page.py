from selene import browser, be, have, command

from model import resource

class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.visible).type('Luna')
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.visible).type('Lovegood')
        return self

    def fill_email(self, value):
        browser.element('#userEmail').should(be.visible).type('luna_love@test.com')
        return self

    def select_gender(self, gender):
        browser.element('[for="gender-radio-2"]').should(be.clickable).click()
        return self

    def fill_mobile(self, value):
        browser.element('#userNumber').should(be.visible).type('7924763817')
        return self

    def fill_date_of_birth(self, month, year, date):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element('[value="11"]').click()
        browser.element('.react-datepicker__year-select').click().element('[value="1994"]').click()
        browser.element('.react-datepicker__day--016').click()
        return self

    def select_subject(self, value):
        browser.element('#subjectsInput').perform(
            command.js.scroll_into_view).should(be.visible).type('History').press_enter()
        return self

    def select_hobbies(self, value):
        browser.element('[for="hobbies-checkbox-3"]').should(be.clickable).click()
        return self

    def select_picture(self, value):
        browser.element('#uploadPicture').set_value(resource.path('image.png'))
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').should(be.visible).type('1234 Elm Street, Springfield, Illinois, 62704, USA')
        return self

    def select_state(self, value):
        browser.element('#react-select-3-input').set_value('NCR').press_enter()
        return self

    def select_city(self, value):
        browser.element('#react-select-4-input').set_value('Noida').press_enter()
        return self

    def click_submit(self):
        browser.element('#submit').should(be.clickable).click()
        return self

    def should_title_submitting_the_form(self, value):
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))

    def should_have_registered(self, student_name, email, gender, mobile, date_of_birth, subjects, hobbies, picture,
                                    address, state_and_city):
        browser.element('table').all('tr').should(have.exact_texts(
            'Label Values',
            'Student Name Luna Lovegood',
            'Student Email luna_love@test.com',
            'Gender Female',
            'Mobile 7924763817',
            'Date of Birth 16 December,1994',
            'Subjects History',
            'Hobbies Music',
            'Picture image.png',
            'Address 1234 Elm Street, Springfield, Illinois, 62704, USA',
            'State and City NCR Noida')
        )
















