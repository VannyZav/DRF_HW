from rest_framework import serializers, validators

from api.models import ApiUser, Warehouse, Product


# class UserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = ApiUser
#         fields = ['username', 'email', 'password', "user_type"]
#         # extra_kwargs = {"password": {"write_only": True}}
#

class WareHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {"id": {"read_only": True}}


class UserSerializer(serializers.Serializer):
    user_type = serializers.ChoiceField
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def update(self, instance, validated_data):
        if user_type := validated_data.get('user_type'):
            instance.user_type = user_type
            instance.save(update_fields=['user_type'])
        if email := validated_data.get('email'):
            instance.email = email
            instance.save(update_fields=['email'])
        if password := validated_data.get('password'):
            instance.password = password
            instance.save(update_fields=['password'])
        return instance

    def create(self, validated_data):
        user = ApiUser.objects.create(
            user_type=validated_data['user_type'],
            email=validated_data['email'],
            username=validated_data['username'],
        )

        user.set_password(validated_data['password'])
        user.save(update_fields=['password'])
        return user
