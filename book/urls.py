from django.urls import path
from .views import BookListView, BookDetailView, AddBookReviewView, home_page, EditReviewView, ConfirmReviewDeleteView, DeleteReviewView
app_name = 'book'
urlpatterns = [
    path("", BookListView.as_view(), name='list'),
    path('<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('home/', home_page, name='home'),
    path("<int:pk>/reviews/", AddBookReviewView.as_view(), name='review'),
    path("<int:book_pk>/reviews/<int:review_pk>/edit/", EditReviewView.as_view(), name='edit_review'),
    path("<int:book_pk>/reviews/<int:review_pk>/delete/confirm/", ConfirmReviewDeleteView.as_view(), name='confirm_delete_review'),
    path("<int:book_pk>/reviews/<int:review_pk>/delete/", DeleteReviewView.as_view(), name='delete_review')

]




