from django.urls import path

# views authenticate
######################################################
from .views.authenticate.login import UserLoginView
from .views.authenticate.logout import UserLogoutView
######################################################


# views admin process
######################################################
from .views.admin.user import UserAPIView
from .views.admin.promo import PromoAPIView
######################################################

# views client process
######################################################
from .views.client.promo import ClientAPIView
######################################################


app_name = "users"


urlpatterns = [


    # urls authenticate
    ####################################################
    path('auth/login', UserLoginView.as_view()),
    path('auth/logout', UserLogoutView.as_view()),
    ####################################################

    # urls admin process
    ####################################################

    # admin/user/create | admin/user/retrieve otherwise raise an error
    path('admin/user/<type>', UserAPIView.as_view()),

    # admin/promo/create |
    # admin/user/retrieve |
    # admin/user/update?id=number |
    # admin/user/delete?id=number otherwise raise an error
    path('admin/promo/<type>', PromoAPIView.as_view()),
    ####################################################

    # urls client process
    ####################################################

    # user/retrieve |
    # user/retrieve?id=number |
    # user/submit?id=number otherwise raise an error

    path('user/<type>', ClientAPIView.as_view()),
    ####################################################

]