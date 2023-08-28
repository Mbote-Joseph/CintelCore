from rest_framework import serializers

from core.models import MyUser, Building, Floor, Office, Visitor


class RegisterMyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model =  MyUser
        fields = ['username', 'email', 'password']

class GetMyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        # fields = ['username', 'password', 'email', 'first_name', 'last_name', 'is_superuser', 'is_visitor', 'is_checked_in']
        fields = "__all__"


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = "__all__"

    
class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = "__all__"


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = "__all__"

class VerifyOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.IntegerField()


class ResendOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()


def validate_phone_number(value):
    if not value.startswith('+254') or len(value) != 13:
        raise serializers.ValidationError("Phone number must be in the format +254xxxxxxxxx")

class VisitorSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(validators=[validate_phone_number])

    class Meta:
        model = Visitor
        fields = ['id', 'full_name', 'id_number', 'phone_number']
