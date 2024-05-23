from django.urls import path

from home.views import (
    index_view,
    LoginView
)

urlpatterns = [
    path('', index_view, name="index"),
    path(route='login/',view=LoginView.as_view(),name='login')
    ]