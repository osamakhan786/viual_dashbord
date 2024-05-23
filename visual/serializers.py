from dataclasses import field, fields
from rest_framework import serializers

from visual.models import Visaul


class VisualSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visaul
        fields = "__all__"