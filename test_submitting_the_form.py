from selene import browser, be, have, command
import os

#Заполнение и отправка формы

def test_positive_submitting_the_form(browser_options):
    browser.open('/automation-practice-form')

    browser.element('#firstName').should(be.visible).type('Luna')
    browser.element('#lastName').should(be.visible).type('Lovegood')
    browser.element('#userEmail').should(be.visible).type('luna_love@test.com')

    browser.element('[for="gender-radio-2"]').should(be.clickable).click()

    browser.element('#userNumber').should(be.visible).type('7924763817')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('[value="11"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="1994"]').click()
    browser.element('.react-datepicker__day--016').click()

    browser.element('#subjectsInput').perform(
        command.js.scroll_into_view).should(be.visible).type('History').press_enter()

    browser.element('[for="hobbies-checkbox-3"]').should(be.clickable).click()

    browser.element('#uploadPicture').set_value(os.path.abspath('image.png'))

    browser.element('#currentAddress').should(be.visible).type('1234 Elm Street, Springfield, Illinois, 62704, USA')
    browser.element('#react-select-3-input').set_value('NCR').press_enter()
    browser.element('#react-select-4-input').set_value('Noida').press_enter()

    browser.element('#submit').should(be.clickable).click()

    #Проверка результатов отправки формы

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
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
    browser.element('#closeLargeModal').should(be.enabled)












