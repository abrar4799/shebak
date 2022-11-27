from django.urls import path 
from .views import quoteRandom

urlpatterns = [
    path('random/', quoteRandom.as_view() , name='random')
]