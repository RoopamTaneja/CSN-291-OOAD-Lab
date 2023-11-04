from rest_framework import serializers
from .models import myUser, credential
from encrypt_hash import *

    
class CredentialSerializer(serializers.ModelSerializer):
    user_name = (
        serializers.SerializerMethodField()
    )  # The SerializerMethodField allows you to customize the representation of a field in a serializer
    #uncomment these***
    #hash_pwd = serializers.CharField(write_only=True)
    # strength = serializers.CharField(write_only=True)
    #pin=serializers.CharField(write_only=True)
    #password= serializers.SerializerMethodField()

    class Meta:
        model = credential
        fields = ["id", "user_name", "title", "website", "hash_pwd","website_username","strength"]
        read_only_fields = ["user_name"]

    def get_user_name(self, obj):
        return obj.user.username
    
    # def get_password(self, obj):
    #     hash_pwd = obj.hash_pwd
    #     pin = self.context.get("pin", None)
    #     key=SHA256_hash(pin)
        
    #     return decrypt_password(key, hash_pwd, decode=True)   



class CredentialVisibleSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    password = serializers.SerializerMethodField()
    hash_pwd = serializers.CharField(write_only=True)

    class Meta:
        model = credential
        fields = [
            "id",
            "user_name",
            "title",
            "website",
            "password",
            "hash_pwd",
            "strength",
        ]
        read_only_fields = ["user_name", "password"]

    def get_user_name(self, obj):
        return obj.user.username

    # def get_password(self, obj):
    #     data = obj.hash_pwd
    #     # will contain decryption logic
    #     return data


class UserListSerializer(serializers.ModelSerializer):
   
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    #hashed_pin = serializers.CharField(write_only=True)
    #remove this afterwards
    class Meta:
        model = myUser
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "hashed_pin",
            "session_token"
        ]


class UserDetailSerializer(serializers.ModelSerializer):
    credentials = serializers.SerializerMethodField()
    """ This field doesn't correspond to a direct attribute of the
     myUser model but allows you to customize the representation of
     credentials for a user"""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = myUser
        fields = [
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "credentials",
        ]
        read_only_fields = ["credentials"]

    def get_credentials(self, obj):
        credentials = (
            obj.credential_set.all()
        )  # The credential_set is a reverse relation automatically generated by Django for ForeignKey
        # relationships.Allows you to retrieve all related credential objects associated with a particular myUser.
        return [
            {"id": credential.id, "title": credential.title}
            for credential in credentials
        ]  # returning the list of titles of every credential in the set

# class PinAuthenticationSerializer(serializers.Serializer):
    # pin = serializers.CharField(max_length=200, required=True)
