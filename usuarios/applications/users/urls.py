from applications.users import views

from django.urls import path

#from usuarios.applications.users.views import LoginUser

app_name = "users_app"

urlpatterns = [
    path(
        'register/',
        views.UserRegisterView.as_view(),
        name = 'user-register,'
    ),
    path(
        'login/',
        views.LoginUser.as_view(),
        name = 'user-Login,'
    )
]