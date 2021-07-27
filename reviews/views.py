from .serializers import ReviewSerializer, ShopSerializer, UserReviewSerializer
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from .models import ReviewModel, ShopModel
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.db.models import Count, Avg
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class ReviewViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Reviews
    """
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ShopView(ListAPIView):
    queryset = ShopModel.objects.annotate(review_count=Count('reviews'), avg_rating=Avg('reviews__rating'))
    serializer_class = ShopSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['review_count', 'avg_rating']
    ordering = ['avg_rating']
    search_fields = ['domain']


class UserReviewView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserReviewSerializer
