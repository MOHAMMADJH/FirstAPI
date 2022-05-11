from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from marketing.models import MarketingMeeting, MeetingType
from marketing.serializers import MarketingMeetingSerializer, MeetingTypeSerializer


class MarketingMeetingDetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return MarketingMeeting.objects.get(id=pk)
        except MarketingMeeting.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = MarketingMeetingSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = MarketingMeetingSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class MeetingTypeDetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return MeetingType.objects.get(id=pk)
        except MeetingType.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = MeetingTypeSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = MeetingTypeSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class MarketingMeetingPagination(generics.ListAPIView):
    queryset = MarketingMeeting.objects.all()
    serializer_class = MarketingMeetingSerializer
    pagination_class = LargeResultsSetPagination



class MarketingMeetingList(APIView):
    def get(self, request, format=None):
        snippets = MarketingMeeting.objects.all()
        serializer = MarketingMeetingSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(dict(request.data))
        serializer = MarketingMeetingSerializer(data=request.data)
        if serializer.is_valid():
            # user = User.objects.get(id=dict(request.data)['userName'][0])
            # token = Token.objects.create(user=user)
            # print(token.key)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class MeetingTypeList(APIView):
    def get(self, request, format=None):
        snippets = MeetingType.objects.all()
        serializer = MeetingTypeSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(dict(request.data))
        serializer = MeetingTypeSerializer(data=request.data)
        if serializer.is_valid():

            # user = User.objects.get(id=dict(request.data)['userName'][0])
            # token = Token.objects.create(user=user).save()
            # print(token.key)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

