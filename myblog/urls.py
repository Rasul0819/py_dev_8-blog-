from django.urls import path
from .views import *
urlpatterns = [
    path('',homepage,name='home'),
    path('reg/',registration,name='reg'),
    path('login/',sing_in,name='login'),
    path('logout/',log_out,name='logout'),
    path('detail/<int:id>',detail,name='detail'),

]
#     path('')
# ]