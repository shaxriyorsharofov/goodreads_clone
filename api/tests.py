from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from book.models import Book, BookReview
from users.models import CustomUser


# Create your tests here.

class BookReviewApiTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='user1', first_name='Shaxriyor')
        self.user.set_password('somepass')
        self.user.save()

    def test_book_review_detail(self):
        book2 = Book.objects.create(title='book1', description='description1', isbn='12345')
        br = BookReview.objects.create(book2=book2, user=self.user, star_given='1', comentary='Very good')


        response = self.client.get(reverse('api:review_detail', kwargs={'pk':id}))

        self.assertEqual(response.status_code, 200)

        self.assertEqual()
