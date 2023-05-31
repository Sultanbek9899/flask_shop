from django.urls import path

from rest_framework.routers import DefaultRouter

from src.apps.product import views


router = DefaultRouter()

router.register("product", views.ProductViewSet, basename="product")
router.register('category', views.CategoryViewSet, basename="category")


urlpatterns = [
   path('', views.IndexView.as_view()),
   path('product/list/', views.ProductListView.as_view(), name="product_list"),
]


urlpatterns += router.urls  