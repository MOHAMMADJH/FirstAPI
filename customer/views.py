from django.contrib.auth.models import User
from django.http import JsonResponse, Http404
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

# Create your views here.
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Customer
from .serializers import EngineerSerializer  ,CustomerSerializer

@api_view(['GET', 'OPTIONS'])
def ping_pong(request):

    return JsonResponse({'message': 'PONG'},
                        status=status.HTTP_200_OK)

@api_view(['POST' , 'OPTIONS'])
def add_engineer(request):
    serializer = EngineerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Status": "Added"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class CustomerDetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Customer.objects.get(id=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = CustomerSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = CustomerSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.isActive = False
        snippet.save()
        return Response(status=status.HTTP_204_NO_CONTENT)





class CustomerList(APIView):



    def get(self, request, format=None):
        snippets = Customer.objects.all()
        serializer = CustomerSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(dict(request.data))
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(id=dict(request.data)['userName'][0])
            token = Token.objects.create(user=user)
            print(token.key)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LargeResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 2


class CustomersView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = LargeResultsSetPagination

