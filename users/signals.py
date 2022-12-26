# from django.core.mail import send_mail
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from users.models import CustomUser
#
#
# @receiver(post_save, sender=CustomUser)
# def send_welcome_email(sender, instance, created, **kwargs):
#     if created:
#         send_mail(
#             "Welcome to Readbooks site",
#             f"Salom, {instance.username}. Xush kelibsiz",
#             'sh.shaxriyor.sh@gmail.com',
#             [instance.email]
#         )