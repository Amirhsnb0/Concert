from django.urls import path
from .views import profileRegisterView, Login_View, Logout_View, Profile_Edit_View, Profile_view


app_name="accounts"
urlpatterns = [
    path("register/",profileRegisterView,name="create_account"),
    path("login/",Login_View,name="login_account"),
    path("logout/",Logout_View,name="logout_account"),
    path("profile/",Profile_view,name="profile_account"),
    path("profileEdit/",Profile_Edit_View,name="profile_edit_account"),
]
