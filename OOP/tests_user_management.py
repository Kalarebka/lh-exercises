import pytest

from datetime import date

from user_management import User, Admin, Redactor, Post


class TestUser:
    def test_create_user(self):
        user = User("Nobby", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown")
        assert user.name == "Nobby"
        assert user.surname == "Nobbs"
        assert user.email == "nobby@nobbs.com"
        assert user.date_of_birth.year == 1990
        assert user.date_of_birth.month == 4
        assert user.date_of_birth.day == 1
        assert user.gender == "unknown"


    def test_compare_users_equal(self):
        user = User("Nobby", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown")
        user2 = User("Nobby", "Nobbs", "nobby2@nobbs.com", date(1990, 1, 1), "unknown")
        user3 = User(
            "Nobbinia", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown"
        )
        assert user == user2
        assert not user == user3

    def compare_users_less_than(self):
        user = User("Nobby", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown")
        redactor = Redactor(
            "Nobby", "Nobbs", "nobby2@nobbs.com", date(1990, 1, 1), "unknown"
        )
        admin = Admin(
            "Nobbinia", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown"
        )
        assert user < redactor
        assert user < admin
        assert redactor < admin
        assert not redactor < user
        assert not admin < user
        assert not admin < redactor

    def test_user_can_create_post(self):
        pass
