from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password  # For securely hashing passwords
from rest_framework import serializers, validators

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is never returned in responses
            'email': {
                'required': True,
                'validators': [
                    validators.UniqueValidator(
                        User.objects.all(), 'A user with that email already exists.'
                    )
                ]
            },
            'username': {
                'validators': [
                    validators.UniqueValidator(
                        User.objects.all(), 'A user with that username already exists.'
                    )
                ]
            }
        }

    def validate_password(self, value):
        """
        Validate and hash the password before saving.
        """
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return make_password(value)  # Hash the password securely

    def create(self, validated_data):
        """
        Create and return a new User instance with the validated data.
        """
        # Extract fields from validated_data
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),  # Optional field
            last_name=validated_data.get('last_name', '')    # Optional field
        )
        # Set the hashed password
        user.set_password(validated_data['password'])
        user.save()
        return user