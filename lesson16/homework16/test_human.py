from unittest.mock import Mock

import pytest


# mocks also should be since I can change mock object in fixture for other tests
def test_check_age(human):
    """
        Check age attribute of created example
    """
    assert human.age == 35


# mocks also should be since I can change mock object in fixture for other tests
def test_check_gender(human):
    """
        Check gender attribute of created example\
    """
    assert human.gender == "female"


def test_check_grow(human, monkeypatch):
    """
        Check grow method for age < 100
    """

    def mock_alive():
        return True

    monkeypatch.setattr(human, "_Human__is_alive", mock_alive)
    human.grow()
    assert human.age == 36


def test_check_grow_for_human_with_age_99(human, monkeypatch):
    """
        Check grow method for age == 99
    """

    def mock_alive():
        return True

    monkeypatch.setattr(human, "_Human__is_alive", mock_alive)
    monkeypatch.setattr(human, "_Human__age", 99)
    human.grow()
    assert human._Human__status == "alive"


def test_check_grow_for_human_with_age_100(human, monkeypatch):
    """
        Check grow method for age == 100
    """

    def mock_alive():
        return True

    monkeypatch.setattr(human, "_Human__is_alive", mock_alive)
    monkeypatch.setattr(human, "_Human__age", 100)
    human.grow()
    assert human._Human__status == "dead"


def test_check_grow_if_human_is_dead(human, monkeypatch):
    def mock_alive():
        raise Exception(f"{human._Human__name} is already dead...")

    monkeypatch.setattr(human, "_Human__is_alive", mock_alive)
    with pytest.raises(Exception, match=f"{human._Human__name} is already " f"dead..."):
        human.grow()


def test_check_is_alive(human):
    """
        Check if is_alive function returns True in case human is alive
    """
    human._Human__is_alive()
    assert True


def test_check_is_alive_error(human, monkeypatch):
    """
        Check if exception is returned in case human is dead
    """
    monkeypatch.setattr(human, "_Human__status", "dead")
    with pytest.raises(Exception, match=f"{human._Human__name} is already " f"dead..."):
        human._Human__is_alive()


@pytest.mark.parametrize(
    "change_gender,gender,expected",
    [("female", "male", "male"), ("male", "female", "female")],
    ids=["change_to_male", "change_to_female"],
)
def test_check_change_gender(human, change_gender, gender, expected, monkeypatch):
    """
        Checks the gender change
    """

    def mock_alive():
        return True

    def mock_validate_gender(*args):
        return None

    monkeypatch.setattr(human, "_Human__is_alive", mock_alive)
    monkeypatch.setattr(human, "_Human__validate_gender", mock_validate_gender)
    monkeypatch.setattr(human, "_Human__gender", change_gender)
    human.change_gender(gender)
    assert human.gender == expected


@pytest.mark.parametrize(
    "change_gender,gender",
    [("female", "female"), ("male", "male")],
    ids=["change_female_to_female", "change_male_to_male"],
)
def test_check_change_gender_if_gender_is_same(
    human, change_gender, gender, monkeypatch
):
    """
        Checks the error if the gender is same
    """

    monkeypatch.setattr(human, "_Human__is_alive", Mock(return_value=True))
    monkeypatch.setattr(human, "_Human__validate_gender", Mock())
    monkeypatch.setattr(human, "_Human__gender", change_gender)
    with pytest.raises(
        Exception,
        match=f"{human._Human__name} already has gender '{human._Human__gender}'",
    ):
        human.change_gender(gender)


def test_change_gender_if_is_alive_returns_error(human, monkeypatch):
    """
        Check the change gender function if is_alive returns exception
    """

    monkeypatch.setattr(
        human,
        "_Human__is_alive",
        Mock(side_effect=Exception(f"{human._Human__name} is already dead...")),
    )
    monkeypatch.setattr(human, "_Human__validate_gender", Mock())

    with pytest.raises(Exception, match=f"{human._Human__name} is already dead..."):
        human.grow()


def test_change_gender_if_validate_gender_returns_error(human, monkeypatch):
    """
        Check change gender function if validate_gender returns exception
    """

    monkeypatch.setattr(human, "_Human__is_alive", Mock(return_value=True))
    monkeypatch.setattr(
        human,
        "_Human__validate_gender",
        Mock(side_effect=Exception("Not correct name of gender")),
    )

    with pytest.raises(Exception, match="Not correct name of gender"):
        human._Human__validate_gender("test")


def test_check_validate_gender_error(human):
    """
        Check validation error for non-existent gender
    """
    with pytest.raises(Exception, match="Not correct name of gender"):
        human._Human__validate_gender("test")


@pytest.mark.parametrize(
    "gender,expected", [("male", None), ("female", None)], ids=["male", "female"]
)
def test_check_validate_gender_for_gender_in_list(human, gender, expected):
    """
        Check validation for existing gender
    """
    assert human._Human__validate_gender(gender) == expected
