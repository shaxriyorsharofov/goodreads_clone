from rest_framework import serializers

from book.models import Book, BookReview
from users.models import CustomUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('pk', 'title', 'description', 'isbn')

# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=89)
#     description = serializers.CharField(max_length=200)
#     isbn = serializers.CharField(max_length=17)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('pk', 'first_name', 'last_name', 'username', 'email')




class BookReviewSerializer(serializers.ModelSerializer):
    book2 = BookSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    book2_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = BookReview
        fields = ('pk', 'star_given', 'comentary', 'book2', 'user', 'book2_id', 'user_id')


