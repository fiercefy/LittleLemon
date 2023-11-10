from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('menu/', views.MenuItemsView.as_view()),
    path('menu_item/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
]