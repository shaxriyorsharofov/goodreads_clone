from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


# Create your tests here.


class RegisterTestCase(TestCase):
    def test_user_creat(self):
        self.client.post(
            reverse('users:register'),
            # 'users/register.html'
            data={
                'username': 'suhrob',
                'first_name': 'Suhrob',
                'last_name': 'Ergashev',
                'email': 'suhrob@gmail.com',
                'password': 'suhrob2007'
            }
        )
        user = User.objects.get(username='suhrob')

        self.assertEqual(user.first_name,'Suhrob')
        self.assertEqual(user.last_name, 'Ergashev')
        self.assertEqual(user.email, 'suhrob@gmail.com')
        # self.assertNotEqual(user.password, 'suhrob2007')
        self.assertTrue(user.check_password('suhrob2007'))

    def test_redirect_user(self):
        response = self.client.post(
            reverse('users:register'),
            # 'users/register.html',
            data={
                'email': 'suhrob@gmail.comh',
                'first_name': 'Suhrob',

            }
        )

        users_count = User.objects.count()
        self.assertEqual(users_count, 0)
        self.assertFormError(response, 'form', 'username', 'This field is required.')
        self.assertFormError(response, 'form', 'password', 'This field is required.')


    def test_email_redirect(self):
        response = self.client.post(
            reverse('users:register'),
            # 'users/register.html'
            data={
                'username': 'suhrob',
                'first_name': 'Suhrob',
                'last_name': 'Ergashev',
                'email': 'sdjhfh-kjasbdf',
                'password': 'suhrob2007'

            }
        )

        users_count = User.objects.count()
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')


    def test_user_doubl(self):
        user = User.objects.create_user(username='suhrob986', first_name='Suhrob')
        user.set_password('suhrob2007')
        user.save()

        response = self.client.post(
            reverse('users:register'),
            # 'users/register.html'
            data={
                'username': 'suhrob986',
                'first_name': 'Suhrob',
                'last_name': 'Ergashev',
                'password': 'suhrob2007'

            }
        )
        users_count = User.objects.count()
        self.assertEqual(users_count, 1)




