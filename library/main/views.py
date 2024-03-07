from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Book, Order
from main.serializers import BookSerializer, OrderSerializer


@api_view(['GET'])
def books_list(request):
    books = Book.objects.all()
    ser = BookSerializer(books, many=True)
    return Response(ser.data)


class CreateBookView(APIView):
    def get(request,pk):
        books = Book.objects.all()
        ser = BookSerializer(books, many=True)
        return Response(ser.data)
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Книга успешно создана') # возвращаем ответ об этом


class BookDetailsView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteView(DestroyAPIView):
    def get(self, request, pk):
        books = Book.objects.get(id=pk)
        ser = BookSerializer(books)
        return Response(ser.data)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer