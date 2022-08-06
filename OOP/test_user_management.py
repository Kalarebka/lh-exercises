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

    def test_user_with_same_data_not_equal(self):
        user = User("Nobby", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown")
        user2 = User("Nobby", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown")
        assert user != user2

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
        user = User("Nobby", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown")
        post = user.create_post("some test title", "some test content")
        assert post.author == user
        assert post.title == "some test title"
        assert post.content == "some test content"

    def test_user_can_edit_own_post(self):
        user = User("Nobby", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown")
        post = user.create_post("some test title", "some test content")
        user.edit_post(post, "new content")
        assert post.content == "new content"

    def test_user_can_change_own_email(self):
        user = User("Nobby", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown")
        user.change_email("nobby.nobbs@gmail.com")
        assert user.email == "nobby.nobbs@gmail.com"

    def test_user_can_delete_own_post(self):
        user = User("Nobby", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown")
        post = user.create_post("some test title", "some test content")
        post2 = user.create_post("title", "post 2")
        assert len(user.posts) == 2
        user.delete_post(post2)
        assert len(user.posts) == 1

    def test_user_cannot_edit_others_post(self):
        user = User("Nobby", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown")
        user2 = User(
            "Carrot",
            "Ironfoundersson",
            "carrot@ankh-morpork.com",
            date(1990, 4, 1),
            "male",
        )
        post = user.create_post("some test title", "old content")
        user2.edit_post(post, "new content")
        assert post.content == "old content"

    def test_user_cannot_delete_others_post(self):
        user = User("Nobby", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown")
        user2 = User(
            "Carrot",
            "Ironfoundersson",
            "carrot@ankh-morpork.com",
            date(1990, 4, 1),
            "male",
        )
        post = user.create_post("some test title", "some test content")
        user2.delete_post(post)
        assert len(user.posts) == 1

    def test_user_cannot_change_others_attributes(self):
        user = User("Nobby", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown")
        user2 = User(
            "Carrot",
            "Ironfoundersson",
            "carrot@ankh-morpork.com",
            date(1990, 4, 1),
            "male",
        )
        user.edit_user_gender(user2, "female")
        user.edit_user_surname(user2, "von Uberwald")
        user.edit_user_name(user2, "Angua")
        user.edit_user_date_of_birth(user2, date(2000, 10, 12))
        user.edit_user_email(user2, "email@email.com")
        assert user2.gender == "male"
        assert user2.surname == "Ironfoundersson"
        assert user2.name == "Carrot"
        assert user2.date_of_birth == date(1990, 4, 1)
        assert user2.email == "carrot@ankh-morpork.com"

    def test_user_can_be_used_as_dict_key(self):
        user = User("Nobby", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown")
        redactor = Redactor(
            "Nobby", "Nobbs", "nobby2@nobbs.com", date(1990, 1, 1), "unknown"
        )
        admin = Admin(
            "Nobbinia", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown"
        )
        ranks = {user: "user", redactor: "redactor", admin: "admin"}
        assert ranks[user] == "user"
        assert ranks[redactor] == "redactor"
        assert ranks[admin] == "admin"


class TestRedactor:
    def test_redactor_can_edit_others_post(self):
        user = User("Nobby", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown")
        redactor = Redactor(
            "Carrot",
            "Ironfoundersson",
            "carrot@ankh-morpork.com",
            date(1990, 4, 1),
            "male",
        )
        post = user.create_post("some test title", "old content")
        redactor.edit_post(post, "new content")
        assert post.content == "new content"

    def test_redactor_cannot_delete_others_post(self):
        user = User("Nobby", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown")
        redactor = Redactor(
            "Carrot",
            "Ironfoundersson",
            "carrot@ankh-morpork.com",
            date(1990, 4, 1),
            "male",
        )
        post = user.create_post("some test title", "old content")
        redactor.delete_post(post)
        assert len(user.posts) == 1

    def test_redactor_cannot_edit_others_attributes(self):
        redactor = Redactor(
            "Nobby", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown"
        )
        user2 = User(
            "Carrot",
            "Ironfoundersson",
            "carrot@ankh-morpork.com",
            date(1990, 4, 1),
            "male",
        )
        redactor.edit_user_gender(user2, "female")
        redactor.edit_user_surname(user2, "von Uberwald")
        redactor.edit_user_name(user2, "Angua")
        redactor.edit_user_date_of_birth(user2, date(2000, 10, 12))
        redactor.edit_user_email(user2, "email@email.com")
        assert user2.gender == "male"
        assert user2.surname == "Ironfoundersson"
        assert user2.name == "Carrot"
        assert user2.date_of_birth == date(1990, 4, 1)
        assert user2.email == "carrot@ankh-morpork.com"


class TestAdmin:
    def test_admin_can_edit_others_post(self):
        user = User("Nobby", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown")
        admin = Admin(
            "Carrot",
            "Ironfoundersson",
            "carrot@ankh-morpork.com",
            date(1990, 4, 1),
            "male",
        )
        post = user.create_post("some test title", "old content")
        admin.edit_post(post, "new content")
        assert post.content == "new content"

    def test_admin_can_delete_others_post(self):
        user = User("Nobby", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown")
        admin = Admin(
            "Carrot",
            "Ironfoundersson",
            "carrot@ankh-morpork.com",
            date(1990, 4, 1),
            "male",
        )
        post = user.create_post("some test title", "old content")
        admin.delete_post(post)
        assert len(user.posts) == 0

    def test_admin_can_edit_others_attributes(self):
        admin = Admin("Nobby", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown")
        user2 = User(
            "Carrot",
            "Ironfoundersson",
            "carrot@ankh-morpork.com",
            date(1990, 4, 1),
            "male",
        )
        admin.edit_user_gender(user2, "female")
        admin.edit_user_surname(user2, "von Uberwald")
        admin.edit_user_name(user2, "Angua")
        admin.edit_user_date_of_birth(user2, date(2000, 10, 12))
        admin.edit_user_email(user2, "email@email.com")
        assert user2.gender == "female"
        assert user2.surname == "von Uberwald"
        assert user2.name == "Angua"
        assert user2.date_of_birth == date(2000, 10, 12)
        assert user2.email == "email@email.com"


class TestPost:
    def test_compare_posts(self):
        user = User("Nobby", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown")
        post = Post(user, "Some title", "some content")
        post2 = Post(user, "title", "some longer content")
        assert post < post2

    def test_create_post(self):
        user = User("Nobby", "Nobbs", "nobby@nobbs.com", date(1990, 4, 1), "unknown")
        post = Post(user, "Some title", "some content")
        assert post.author == user
        assert post.title == "Some title"
        assert post.content == "some content"
