import pytest

from setup_utilities.driver_factory import DriverFactory


@pytest.fixture(scope="session")
def driver(request, platform):
    print("session_level_setup: Running session level setup.")
    df = DriverFactory(platform)
    driver = df.get_driver_instance()
    yield driver
    print("session_level_setup: Running session level teardown.")
    driver.quit()


@pytest.fixture(scope="session")
def platform(request):
    plat = request.config.getoption("--platform").lower()
    if plat not in ["flutter_ios", "flutter_android", "native_android", "native_ios"]:
        raise ValueError(
            "platform value must be in ['flutter_ios', 'flutter_android', 'native_android', 'native_ios']"
        )
    return plat


def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="browser_stack")