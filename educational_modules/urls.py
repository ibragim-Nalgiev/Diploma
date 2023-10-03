from django.urls import path

from .views import ModulesCreateAPIView, ModulesListAPIView, ModulesRetrieveAPIView, ModulesUpdateAPIView, \
    ModulesDestroyAPIView, ModulesPublishedListAPIView

app_name = 'educational_modules'

urlpatterns = [
    path('create/', ModulesCreateAPIView.as_view(), name='modules_create'),
    path('', ModulesPublishedListAPIView.as_view(), name='modules'),
    path('all/', ModulesListAPIView.as_view(), name='modules'),
    path('<int:pk>/', ModulesRetrieveAPIView.as_view(), name='module'),
    path('update/<int:pk>/', ModulesUpdateAPIView.as_view(), name='modules_update'),
    path('delete/<int:pk>/', ModulesDestroyAPIView.as_view(), name='modules_delete'),
]
