import pytest

from api.user_api import UserApi
from utils.browser_factory import BrowserFactory


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    driver = BrowserFactory.create_driver(request.param)

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def test_user():
    api = UserApi()
    user = api.create_user()

    yield user

    api.delete_user(user["access_token"])