# from .views import BookReviewDetailAPIView, BookReviewListAIPView
from django.urls import path
from api.views import BookReviewViewSets
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register('reviews', BookReviewViewSets, basename='book_review')
urlpatterns = router.urls


# urlpatterns = [
#     path('review/', BookReviewListAIPView.as_view(), name='review_list'),
#     path('review/<int:pk>/', BookReviewDetailAPIView.as_view(), name='review_detail')
# ]




