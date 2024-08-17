from django.urls import path
from .views import index, get_settings, get_state_instance, send_message, send_file_by_url

urlpatterns = [
    path('', index, name='home'),
    path('getSettings/', get_settings, name='getSettings'),
    path('getStateInstance/', get_state_instance, name='getStateInstance'),
    path('sendMessage/', send_message, name='send_message'),
    path('sendFileByUrl/', send_file_by_url, name='send_file_by_url'),

]
