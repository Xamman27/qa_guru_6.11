from selene import browser, be, have
import os

def test_registration():
    browser.open('/')
    browser.element('#firstName').should(be.blank).type('Valery')
    browser.element('#lastName').should(be.blank).type('Maksimov')
    browser.element('#userEmail').should(be.blank).type('valery@mail.com')
    browser.element("[value='Male']+label").should(be.clickable).click()
    browser.element('#userNumber').should(be.blank).type('8900100000')

    browser.element('#dateOfBirthInput').should(be.clickable).click()
    browser.element("[value='4']").should(be.clickable).click()
    browser.element("[value='1989']").should(be.clickable).click()
    browser.element("[value='1989']").should(be.clickable).click()
    browser.element("[aria-label='Choose Monday, May 1st, 1989']").should(be.clickable).click()

    browser.element('#subjectsInput').should(be.blank).type('Eng').press_enter()
    browser.element('[for=hobbies-checkbox-1][class="custom-control-label"]').should(be.clickable).click()
    browser.element('#uploadPicture').set_value(os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'resources/image.jpeg')))

    browser.execute_script("window.scrollBy(0, 500)")
    browser.element('#currentAddress').should(be.blank).type('SPB')
    browser.element('#react-select-3-input').should(be.blank).type('ncr').press_enter()
    browser.element('#react-select-4-input').should(be.blank).type('Delhi').press_enter().press_enter()

    browser.element('//tbody/tr[1]/td[2]').should(have.text('Valery Maksimov'))
    browser.element('//tbody/tr[2]/td[2]').should(have.text('valery@mail.com'))
    browser.element('//tbody/tr[3]/td[2]').should(have.text('Male'))
    browser.element('//tbody/tr[4]/td[2]').should(have.text('8900100000'))
    browser.element('//tbody/tr[5]/td[2]').should(have.text('1 May,1989'))
    browser.element('//tbody/tr[6]/td[2]').should(have.text('English'))
    browser.element('//tbody/tr[7]/td[2]').should(have.text('Sports'))
    browser.element('//tbody/tr[8]/td[2]').should(have.text('image.jpeg'))
    browser.element('//tbody/tr[9]/td[2]').should(have.text('SPB'))
    browser.element('//tbody/tr[10]/td[2]').should(have.text('NCR Delhi'))


