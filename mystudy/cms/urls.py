from django.urls import path
from cms import views


app_name = 'cms'
urlpatterns = [
    # 事件
    path('affair/', views.affair_list, name='affair_list'),  # 一覧
    path('affair/<int:affair_id>/', views.affair_detail, name='affair_detail')  # 詳細
]
