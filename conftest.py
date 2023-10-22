import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def browser_setup():
    browser.config.window_width = 1600
    browser.config.window_height = 1600

    yield

    browser.quit()
