from model.pages.registration_page import RegistrationPage

def test_registration_form(browser_options):
    registration_page = RegistrationPage()
    registration_page.open()
    (
        registration_page
        .fill_first_name('Luna')
        .fill_last_name('Lovegood')
        .fill_email('luna_love@test.com')
        .select_gender('Female')
        .fill_mobile('7924763817')
        .fill_date_of_birth('December', '1994', '16')
        .select_subject('History')
        .select_hobbies('Music')
        .select_picture('image.png')
        .fill_current_address('1234 Elm Street, Springfield, Illinois, 62704, USA')
        .select_state('NCR')
        .select_city('Noida')
        .click_submit()
    )

    registration_page.should_title_submitting_the_form('Thanks for submitting the form')

    registration_page.should_have_registered(
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
















