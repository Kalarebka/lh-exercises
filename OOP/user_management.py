# Create 4 classes: User, Administrator or Admin, Redactor and Post
# User class has to have name, surname, email, date of birth, gender, it has possibility to change own email, create, edit, delete own posts
# Redactor class has all functions that User class has and has possibility to edit all posts
# Admin class can edit everything, attributes of classes User and Redactor and can edit all posts
# Post has content, date of creation and modification, Author, can be edited via method, by User with proper permissions,
# date of modification should be created and updated automatically

# User classes can be compared with each other with logical operators, Admin > Redactor > User
# Classes Admin, Redactor, and User should be able to compare with == operator, it returns True if object is this same class and name+surname attrs are this same
# Classes Admin, Redactor, and User should be able to be used as keys in dict
# It should be possible to determine which Post class is bigger (have longer content)

# Use Abstract classes to provide solution
# Simulate this same functionality with one class and permissions system, where Admin can elevate permissions of other users
from abc import ABC, abstractmethod
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

    # Should be compatible with __hash__ - objects that are equivalent should hash the same
    def __eq__(self, other):
        return type(self) == type(other) and self.name == other.name and self.surname == other.surname

    def __hash__(self):
        return hash((type(self), self.name, self.surname))

    # Not sure about this one, there should be a better way to do it/ or just put it in child classes
    def __lt__(self, other):
        return isinstance(self, User) and (isinstance(other, Redactor) or isinstance(other, Admin))
               or isinstance(self, Redactor) and isinstance(other, Admin)

    def create_post(self, content):
        self.posts.append(Post(self, content))

    def change_email(self, new_email):
        self.email = new_email

    @abstractmethod
    def edit_post(self, post):
        pass

    @abstractmethod
    def delete_post(self, post):
        pass

    
class User(AbstractUser):
    def edit_post(self, post, new_content):
        if post.author == self:
            post.edit(self, new_content)
        else:
            print("Permission denied")

    def delete_post(self, post):
        if post.author == self:
            post.delete()
        else:
            print("Permission denied")


class Admin(AbstractUser):
    def edit_post(self, post, new_content):
        post.edit(self, new_content)

    def delete_post(self, post):
        post.delete()


class Redactor(AbstractUser):
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
        self.date_created = date.today() # could also do datetime here to record precise time
        self.date_modified = self.date_created

    # TODO comparisons of posts by content length

    def edit(self, new_content):
        self.content = new_content
        self.date_modified = date.today()

    def delete(self):
        pass

