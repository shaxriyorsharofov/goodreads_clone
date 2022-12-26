from django.core.validators import MinValueValidator, MaxValueValidator

from users.models import CustomUser
from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=89)
    description = models.TextField()
    isbn = models.CharField(max_length=18)
    book_picture = models.ImageField(default='book_default.jpg', upload_to='book/')

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    bio = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} !!! "

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} by {self.author.first_name} {self.author.last_name} "

class BookReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book2 = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_review')
    comentary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    star_given = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return f"{self.user} {self.book2.title}"






