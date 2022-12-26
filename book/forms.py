from django import forms

from book.models import BookReview


class BookReviewForms(forms.ModelForm):
    star_given = forms.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = BookReview
        fields = ('star_given', 'comentary')