from django.urls import path
from django.contrib.auth.views import LoginView

from .views import (
    get_cookie_view,
    set_cookie_view,
    get_session_view,
    set_session_view,
    MyLogoutView,
    AboutMeView,
    RegisterView,
    FooBarView,
    ProfilesListView,
    ProfileDetailView,
    ProfileUpdateView,
    HelloView,
)

app_name = "myauth"

urlpatterns = [
    #path("login/", login_view, name="login")
    path(
        "login/",
        LoginView.as_view(
            template_name="myauth/login.html",
            redirect_authenticated_user=True,
        ),
        name="login"
    ),
    path("hello/", HelloView.as_view(), name="hello"),
    #path("logout/", logout_view, name="logout"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
    path("about-me/", AboutMeView.as_view(), name="about-me"),
    path("register/", RegisterView.as_view(), name="register"),

    path("profiles-list/", ProfilesListView.as_view(), name="profiles_list"),
    path("profile-details/<int:pk>/", ProfileDetailView.as_view(), name="profile_details"),
    path("profile-update/<int:pk>/", ProfileUpdateView.as_view(), name="profile_update"),

    path("cookie/get/", get_cookie_view, name="cookie-get"),
    path("cookie/set/", set_cookie_view, name="cookie-set"),
    path("session/set/", set_session_view, name="session-set"),
    path("session/get/", get_session_view, name="session-get"),

    path("foo-bar/", FooBarView.as_view(), name="foo-bar"),
]