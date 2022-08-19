from django.urls import path, include
from . import views


urlpatterns=[
	path('home.html', views.home, name='home'),
	path('about.html', views.about, name='About'),
	path('crypto.html', views.crypto, name='Crypto'),
	path('Research.html', views.research, name='Research'),
	path('customize_portfolio.html', views.portfolio, name='My Portfolio'),
	path('rec.html', views.rec, name='Recommended Portfolio'),
	path('profile', views.profile, name="Profile"),



]