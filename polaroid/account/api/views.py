from rest_framework import status
from rest_framework.response import Response 
from rest_framework.decorator import api_view

from account.api import RegistrationSerializer

@api_view(['Post',])
def registraion_view(request):
    
    if request.method == 'POST':
        serializer = RegistrationSerializer(dta=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "successfullly resgistered new user."
            data['email'] = account.email
            data['username'] account.username
        else:
            data = serializer.errors
        return Response(data)