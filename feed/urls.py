from django.urls import path
from .views import *



urlpatterns = [
    path('quran_ayah/', quran_ayah_list),
    path('quran_ayah/<int:pk>/', quran_ayah_item),
    path('hadith_of_day/', hadith_of_day_list),
    path('hadith_of_day/<int:pk>/', hadith_of_day_item),
    path('inspiring_picture/', inspiring_picture_list),
    path('inspiring_picture/<int:pk>/', inspiring_picture_item),
    path('youtube_video/', youtube_video_list),
    path('youtube_video/<int:pk>/', youtube_video_item),
    path('dhikr_by_user/', dhikr_by_user_list),
    path('dhikr_by_user/<int:pk>/', dhikr_by_user_item),
]
