from django.urls import path
from . import views


urlpatterns = [
    path('config_main', views.config_main, name='config_main'),
    path('config_cig', views.config_cig, name='config_cig'),
    path('add_item_cig', views.add_item_cig, name='add_item_cig'),
    path('del_item_cig/<int:id>', views.del_item_cig, name='del_item_cig'),
    path('edit_item_cig/<int:id>', views.edit_item_cig, name='edit_item_cig'),
    path('config_audio_producto', views.config_audio_producto, name='config_audio_producto'),
    path('del_item_audio_producto/<int:id>', views.del_item_audio_producto, name='del_item_audio_producto'),
    path('edit_item_audio_producto/<int:id>', views.edit_item_audio_producto, name='edit_item_audio_producto'),
    path('add_item_audio_producto', views.add_item_audio_producto, name='add_item_audio_producto'),
    path('config_audio_motivo', views.config_audio_motivo, name='config_audio_motivo'),
    path('del_item_audio_motivo/<int:id>', views.del_item_audio_motivo, name='del_item_audio_motivo'),
    path('edit_item_audio_motivo/<int:id>', views.edit_item_audio_motivo, name='edit_item_audio_motivo'),
    path('add_item_audio_motivo', views.add_item_audio_motivo, name='add_item_audio_motivo'),   


]