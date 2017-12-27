from rest_framework import generics, permissions

from portofool_io.models import UserProfile
from portofool_io.serializers import UserProfileSerializer


class RegisterAPIView(generics.CreateAPIView):
    """
    API endpoint untuk melakukan registrasi
    """
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.AllowAny,)


class UserProfilesAPIView(generics.ListAPIView):
    """
    API endpoint untuk melihat semua user terdaftar beserta profilenya
    """
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = UserProfile.objects.filter(user__is_staff=False, user__is_superuser=False)


class SingleUserProfileAPIView(generics.RetrieveUpdateAPIView):
    """
    API endpoint untuk melihat, dan mengupdate/mengganti data profile milik pribadi
    """
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)
