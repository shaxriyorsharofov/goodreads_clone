from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import BookReviewForms
from .models import Book, BookReview
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class BookListView(View):
    def get(self, request):
        books = Book.objects.all()

        search_query = request.GET.get('q')
        if search_query:
            books = books.filter(title__icontains=search_query)
        return render(request, 'books/book_list.html', {'books': books})




class BookDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        book_form = BookReviewForms()

        return render(request, 'books/book_detail.html', {'book': book, 'book_review': book_form})

class AddBookReviewView(LoginRequiredMixin, View):
    def post(self, request, pk):
        book = Book.objects.get(pk=pk)
        book_form = BookReviewForms(data=request.POST)

        if book_form.is_valid():
            BookReview.objects.create(
                book2=book,
                user=request.user,
                star_given=book_form.cleaned_data['star_given'],
                comentary=book_form.cleaned_data['comentary']
            )

            return redirect(reverse('book:detail', kwargs={'pk': book.pk}))
        return redirect(request, 'books/book_detail.html', {'book': book, 'book_review': book_form})


def home_page(request):
    book_reviews = BookReview.objects.all().order_by('-created_at')

    return render(request, 'home_page.html', {'book_reviews': book_reviews})



class EditReviewView(LoginRequiredMixin, View):
    def get(self, request, book_pk, review_pk):
        book = Book.objects.get(pk=book_pk)
        review = BookReview.objects.get(pk=review_pk)
        review_form = BookReviewForms(instance=review)
        return render(request, 'books/edit_review.html', {'book': book, 'review': review, 'review_form': review_form})

    def post(self, request, book_pk, review_pk):
        book = Book.objects.get(pk=book_pk)
        review = BookReview.objects.get(pk=review_pk)
        review_form = BookReviewForms(instance=review, data=request.POST)

        if review_form.is_valid():
            review_form.save()
            return redirect(reverse('book:detail', kwargs={'pk': book.pk}))


        return render(request, 'books/edit_review.html', {'book': book, 'review': review, 'review_form': review_form})


class ConfirmReviewDeleteView(LoginRequiredMixin, View):
    def get(self, request, book_pk, review_pk):
        book = Book.objects.get(pk=book_pk)
        review = BookReview.objects.get(pk=review_pk)
        return render(request, 'books/confirm_delete_review.html', {'book': book, 'review': review})


class DeleteReviewView(LoginRequiredMixin, View):
    def get(self, request, book_pk, review_pk):
        book = Book.objects.get(pk=book_pk)
        review = BookReview.objects.get(pk=review_pk)
        review.delete()
        messages.success(request, 'You successfully delete this review')
        return redirect(reverse('book:detail', kwargs={'pk': book.pk}))


