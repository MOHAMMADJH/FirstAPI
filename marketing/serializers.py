from rest_framework import serializers
from .models import MarketingMeeting , MeetingType , ContractType , Contract

class MarketingMeetingSerializer(serializers.ModelSerializer):


    class Meta:
        model = MarketingMeeting
        fields = '__all__'




class MeetingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingType
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class ContractTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractType
        fields = '__all__'
