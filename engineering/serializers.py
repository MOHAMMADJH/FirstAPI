from rest_framework import serializers
from .models import *

class DesignTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignType
        fields = '__all__'


class ProjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectType
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    # customerName = serializers.CharField(source=Customer.firstName, required=False)
    # projectName = serializers.CharField(source=Contract.projectName, required=False)
    # priceWithTax = serializers.FloatField(source=Contract.priceInNumber , required=False)

    #my_field = serializers.SerializerMethodField('get_final_price_with_tax')

    def get_final_price_with_tax(self):
        # get price from contract

        # get manicapul confirmation  >> check true

        # multiply by 0.15 and add to price


        return 100


    class Meta:
        model = Project
        fields = '__all__'
        # extra_fields = ['customerName' , ]


class ItemsTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsTable
        fields = '__all__'


class MoodBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodBoard
        fields = '__all__'

class StyleMoodBoardPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = StyleMoodBoardPart
        fields = '__all__'


class MoodBoardPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodBoardPart
        fields = '__all__'

class MoodBoardPartImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodBoardPartImages
        fields = '__all__'


# ItemsTable MoodBoard  MoodBoardPartImages