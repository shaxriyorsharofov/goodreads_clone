# serializer_class = BookReviewSerializer
# queryset = BookReview.objects.all().order_by('-created_at')

# permission_classes = [IsAuthenticated]
# def get(self, request):
#     book_review = BookReview.objects.all().order_by('-created_at')
#
#     paginator = PageNumberPagination()
#     pag_obj = paginator.paginate_queryset(book_review, request)
#     serializer = BookReviewSerializer(pag_obj, many=True)
#
#     return paginator.get_paginated_response(serializer.data)
#
# def post(self, request):
#     serializer = BookReviewSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#
#     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# serializer_class = BookReviewSerializer
# queryset = BookReview.objects.all()
# lookup_field = 'pk'
# permission_classes = [IsAuthenticated]

# def get(self, request, pk):
#     book_review = BookReview.objects.get(pk=pk)
#     serializer = BookReviewSerializer(book_review)
#     return Response(data=serializer.data)

# def delete(self, request, pk):
#     book_review = BookReview.objects.get(pk=pk)
#     book_review.delete()
#
#     return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# def put(self, request, pk):
#     book_review = BookReview.objects.get(pk=pk)
#     serializer = BookReviewSerializer(instance=book_review, data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# def patch(self, request, pk):
#     book_review = BookReview.objects.get(pk=pk)
#     serializer = BookReviewSerializer(instance=book_review, data=request.data, partial=True)
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)





