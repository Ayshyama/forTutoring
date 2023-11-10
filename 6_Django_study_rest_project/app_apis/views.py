from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app_bookstore.models import Book
from app_apis.serializers import BookSerializer


class BookListAPIView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        
        return Response(serializer.data)

