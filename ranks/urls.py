from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<int:item_id>', create_session_view, name="create_session_view"),
    path('item/<int:item_id>', index),
    path('', home, name='home'),

]
