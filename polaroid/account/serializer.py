from rest_framework import serializers

from account.model import Account 

class RegisterSerializer(serializers.ModelSerializer):

    #in his example he adds a password2
    password2 = serializers.Charfield(style = {'input_type': 'password'}, write_only = True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
                'password': {'write_only': True}
        }
    
    def save(self):
        account = Account(
                        email = self.validated_date['email']
                        username = self.validated_date['username']
            )
        password = self.validated_date['password']
        password2 = self.validated_date['password2']
        
        if password != password2
            raise serializers.ValidationError({'password': 'Password must match.'})
        account.set_password(password)
        account.save()
        return account