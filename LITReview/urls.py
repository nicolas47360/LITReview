"""LITReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.contrib import admin
import authentication.views
import books.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='authentication/login.html',
                               redirect_authenticated_user=True)
         , name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('registration', authentication.views.RegistrationPageView.as_view(), name='registration'),
    path('ticket', books.views.CreateTicketView.as_view(), name='ticket'),
    path('delete_ticket', books.views.DeleteTicketView.as_view(), name='delete'),
    path('update_ticket/<int:pk>', books.views.UpdateTicketView.as_view(), name='update'),
    path('home', books.views.HomeView.as_view(), name='home'),
    path('create_review', books.views.CreateReviewView.as_view(), name='create_review'),
    path('update_review', books.views.UpdateReviewView.as_view(), name='update_review'),
    path('delete_review', books.views.DeleteView.as_view(), name='delete_review'),
]

