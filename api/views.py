from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import BookReviewSerializer
from book.models import BookReview
from rest_framework import generics
from rest_framework import viewsets
# Create your views here.



class BookReviewViewSets(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookReviewSerializer
    queryset = BookReview.objects.all().order_by('-created_at')
    lookup_field = 'pk'


# class BookReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = BookReviewSerializer
#     queryset = BookReview.objects.all()
#     lookup_field = 'pk'
#

    # def get(self, request, pk):
    #     book_review = BookReview.objects.get(pk=pk)
    #     serializer = BookReviewSerializer(book_review)
    #     return Response(data=serializer.data)

    # def delete(self, request, pk):
    #     book_review = BookReview.objects.get(pk=pk)
    #     book_review.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    #
    # def put(self, request, pk):
    #     book_review = BookReview.abjects.get(pk=pk)
    #     serializer = BookReviewSerializer(instance=book_review, data=request.data)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data, status=status.HTTP_200_OK)
    #     return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)
    #
    # def patch(self, request, pk):
    #     book_review = BookReview.objects.get(pk=pk)
    #     serializer = BookReviewSerializer(instance=book_review, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data, status=status.HTTP_200_OK)
    #     return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)





# class BookReviewDetailAPIView(View):
#     def get(self, request, pk):
#         book_review = BookReview.objects.get(pk=pk)
#
#         json_response = {
#             'pk': book_review.pk,
#             'star_given': book_review.star_given,
#             'comment': book_review.comentary,
#             'user':{
#                 'pk': book_review.user.pk,
#                 'first_name': book_review.user.first_name,
#                 'last_name': book_review.user.last_name,
#                 'username': book_review.user.username,
#             },
#             'book': {
#                 'pk': book_review.book2.pk,
#                 'title': book_review.book2.title,
#                 'description': book_review.book2.description,
#                 'isbn': book_review.book2.isbn
#             }
#         }
#         return JsonResponse(json_response)




# class BookReviewListAIPView(generics.ListCreateAPIView):
#     serializer_class = BookReviewSerializer
#     queryset = BookReview.objects.all().order_by('-created_at')
#     permission_classes = [IsAuthenticated]


    def get(self, request):
        book_review = BookReview.objects.all().order_by('-created_at')
        pagination = PageNumberPagination()
        page_obj = pagination.paginate_queryset(book_review, request)
        serializer = BookReviewSerializer(page_obj, many=True)
        return pagination.get_paginated_response(serializer.data)
    #
    # def post(self, request):
    #     serializer = BookReviewSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)

















