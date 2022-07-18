# Create 4 classes: User, Administrator or Admin, Redactor and Post --> DONE
# User class has to have name, surname, email, date of birth, gender, it has possibility to change own email, create, edit, delete own posts --> DONE
# Redactor class has all functions that User class has and has possibility to edit all posts --> DONE
# Admin class can edit everything, attributes of classes User and Redactor and can edit all posts --> DONE
# Post has content, date of creation and modification, Author, can be edited via method, by User with proper permissions, --> DONE
# date of modification should be created and updated automatically --> DONE

# User classes can be compared with each other with logical operators, Admin > Redactor > User --> DONE
# Classes Admin, Redactor, and User should be able to compare with == operator, it returns True if object is this same class and name+surname attrs are this same --> DONE
# Classes Admin, Redactor, and User should be able to be used as keys in dict --> DONE
# It should be possible to determine which Post class is bigger (have longer content) --> ~ DONE

# Use Abstract classes to provide solution --> DONE???
# Simulate this same functionality with one class and permissions system, where Admin can elevate permissions of other users -->
from abc import ABC, abstractmethod, abstractproperty
from datetime import date


class AbstractUser(ABC):
    def __init__(self, name, surname, email, date_of_birth, gender):
        # TODO some data validation
        self.name = name
        self.surname = surname
        self.email = email
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.posts = []

    @abstractproperty
    def importance(self):
        pass

    # Should be compatible with __hash__ - objects that are equivalent should hash the same
    def __eq__(self, other):
        return (
            type(self) == type(other)
            and self.name == other.name
            and self.surname == other.surname
        )

    def __hash__(self):
        return hash((type(self), self.name, self.surname))

    # Comparisons
    def __lt__(self, other):
        return self.importance > other.importance

    def create_post(self, content):
        self.posts.append(Post(self, content))

    def change_email(self, new_email):
        self.email = new_email

    @abstractmethod
    def edit_post(self, post):
        pass

    def delete_post(self, post):
        if post.author == self:
            post.delete()
        else:
            print("Permission denied")


class User(AbstractUser):
    importance = 3

    def edit_post(self, post, new_content):
        if post.author == self:
            post.edit(self, new_content)
        else:
            print("Permission denied")


class Admin(AbstractUser):
    importance = 1

    def edit_post(self, post, new_content):
        post.edit(self, new_content)

    def delete_post(self, post):
        post.delete()

    def edit_user_name(user, new_name):
        user.name = new_name

    def edit_user_surname(user, new_surname):
        user.surname = new_surname

    def edit_user_email(user, new_email):
        user.email = new_email

    def edit_user_date_of_birth(self, new_date):
        user.date_of_birth = new_date

    def edit_user_gender(self, new_gender):
        user.gender = new_gender


class Redactor(AbstractUser):
    importance = 2

    def edit_post(self, post, new_content):
        post.edit(self, new_content)

    def delete_post(self, post):
        if post.author == self:
            post.delete()
        else:
            print("Permission denied")


class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.date_created = (
            date.today()
        )  # could also do datetime here to record precise time
        self.date_modified = self.date_created

    # Maybe try using @functools.total_ordering
    def __lt__(self, other):
        if isinstance(other, Post):
            return len(self.content) < len(other.content)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Post):
            return len(self.content) < len(other.content)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Post):
            return len(self.content) == len(other.content)
        return NotImplemented

    def edit(self, new_content):
        self.content = new_content
        self.date_modified = date.today()

    def delete(self):
        self.author.posts.remove(self)
