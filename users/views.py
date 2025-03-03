from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.models import AuthToken
from .serializers import RegisterSerializer

# Helper function to create a consistent authentication response
def create_auth_response(user):
    """Generate a consistent response format for authenticated users."""
    _, token = AuthToken.objects.create(user)  # Create a Knox token for the user
    return {
        'user_info': {
            'id': user.id,
            'username': user.username,
            'email': user.email
        },
        'token': token  # Include the Knox token in the response
    }

# Login API
@api_view(['POST'])
def login_api(request):
    """
    Authenticate a user and return their details along with a Knox token.
    """
    serializer = AuthTokenSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']  # Get the authenticated user
        return Response(create_auth_response(user))  # Use the helper function
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

# Get User Data API
@api_view(['GET'])
def get_user_data(request):
    """
    Return the authenticated user's data if they are logged in.
    """
    user = request.user
    if user.is_authenticated:
        return Response({
            'user_info': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        })
    return Response({'error': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

# Register API
@api_view(['POST'])
def register_api(request):
    """
    Register a new user and return their details along with a Knox token.
    """
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()  # Save the new user
        return Response(create_auth_response(user), status=status.HTTP_201_CREATED)  # Use the helper function
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)