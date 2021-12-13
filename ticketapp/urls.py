from os import name
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import Concert_Edit_View, Concert_View, Detail_Concert_View, Location_View, Time_Concert_View

app_name ='ticketapp'
urlpatterns = [
    path('',Concert_View, name='concert_view'),
    path('location/',Location_View, name='location_concert_view'),
    path('detail/<int:consert_id>',Detail_Concert_View, name='detail_concert_view'),
    path('time/',Time_Concert_View, name='time_concert_view'),
    path('detailedit/<int:consert_id>',Concert_Edit_View, name='edit_concert_view'),
    



]

