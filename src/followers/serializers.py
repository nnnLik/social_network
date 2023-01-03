from rest_framework import serializers
from .models import Follower
from src.profiles.serializers import UserFollowerSerializer


class ListFollowerSerializer(serializers.ModelSerializer):
    """List of Follower"""

    subscriber = UserFollowerSerializer(many=True, readonly=True)
    class Meta:
        model = Follower
        fields = ('')


class CreateFollowerSerializer(serializers.ModelSerializer):
    """Create Follower"""

    class Meta:
        ...