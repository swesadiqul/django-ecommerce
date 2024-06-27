from django.urls import path
from users import views


urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('forgot-password', views.forgot_password, name='forgot_password'),
    path('user/dashboard', views.user_dashboard, name='user_dashboard'),
    path('user/profile/update', views.update_profile, name='update_profile'),
]

