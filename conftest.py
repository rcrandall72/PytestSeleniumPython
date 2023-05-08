import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Specify chrome, firefox or safari"
    )


@pytest.fixture()
def browser(pytestconfig):
    return pytestconfig.getoption("browser")
