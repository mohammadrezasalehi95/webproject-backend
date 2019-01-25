from django.contrib import admin
from django.urls import path, include

from webProject.sport.views import GameResults

urlpatterns = [
    path('GameResults/(?P<teamName>\w{0,50})',GameResults.as_view()),
    path('',include('sport.api.urls'))

]