from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Company
        fields = ('id', 'company_name', 'owner', 'website', 'headquarters', 'industry', 'revenue','size', 'founded', 'summary')