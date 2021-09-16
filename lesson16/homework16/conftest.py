import pytest

from lesson16.homework16.human import Human


@pytest.fixture
def human() -> Human:
    yield Human("Nancy", 35, "female")
