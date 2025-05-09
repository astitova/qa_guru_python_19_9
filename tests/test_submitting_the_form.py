from model.data.users import student
from model.pages.registration_page import RegistrationPage

def test_registration_form(browser_options):
    (
        RegistrationPage()
        .open()
        .register(student)
        .should_have_data(student)
    )



