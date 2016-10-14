from rest_framework import serializers
from models import Banks,Branches


class BanksSerializer(serializers.ModelSerializer):
    """
    Serializer class for Bank Model
    """
    class Meta:
        model = Banks


class BranchesSerializer(serializers.ModelSerializer):
    """
    Serializer class for Brances Model
    """
    class Meta:
        model = Branches
        field = {'bank_details','branch','address', 'state'}
        read_only_fields = ('branch','address', 'state')
