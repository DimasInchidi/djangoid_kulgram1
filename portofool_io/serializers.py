from django.contrib.auth.models import User
from rest_framework import serializers

from portofool_io.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = '__all__'

    def update(self, instance, validated_data):
        print(validated_data)
        user_data = validated_data.pop('user')
        instance.about = validated_data.get('about', instance.about)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()

        instance.user.username = user_data.get('username', instance.user.username)
        instance.user.first_name = user_data.get('first_name', instance.user.first_name)
        instance.user.last_name = user_data.get('last_name', instance.user.last_name)
        instance.user.email = user_data.get('email', instance.user.email)
        instance.user.save()
        return instance

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(is_active=True, **user_data)
        customer = UserProfile.objects.create(user=user, **validated_data)
        return customer
