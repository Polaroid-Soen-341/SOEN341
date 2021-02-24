from django.url import path
from account.api.views import(

    registraion_view
)

app_name = "account"



urlpatterns = [
    path('register', registraion_view, name = "register")
] 
#need to add to rest_framework urls