from selene import be, have
from selene.support.shared import browser


def test_search_with_results(browser_setup):
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in'))


def test_search_with_no_results(browser_setup):
    browser.open('https://google.com/ncr')
    test_string = '&*GEdf9c8eorfghbewfvweq98'
    browser.element('[name="q"]').should(be.blank).type(test_string).press_enter()
    browser.element('[id="botstuff"]').should(
        (have.text(f'Your search - {test_string} - did not match any documents.')))
