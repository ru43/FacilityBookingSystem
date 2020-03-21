from django.urls import path
from obsapp import views
urlpatterns=[
    path('',views.home,name="home"),
    path('cse/',views.cse,name="cse"),
    path('login/',views.login_page,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.logoutPage,name='logout'),
    path('adminp/',views.adminPage,name='adminp'),
    path('userd/',views.userDetails,name='userd'),
    path('book/',views.bookfacility,name='book'),
    path('delete/<str:pk>/',views.deleteBooked,name='delete'),
    path('bookings/',views.bookings,name='bookings'),

]
