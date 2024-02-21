import pytest


@pytest.fixture(scope='session')
def browser_context_args(browser_context_args):
    return {
        "viewport": {
            "width": 400,
            "height": 600,
        }
    }


@pytest.fixture(scope='session')
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "storage_state": {
            "cookies": [
                {
                    "name": "stepik",
                    "value": "sd4fFfv!x_cfcstepik",
                    "url": "https://example.com"
                },
            ]
        },
    }
