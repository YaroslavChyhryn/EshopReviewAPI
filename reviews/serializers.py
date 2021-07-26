from rest_framework import serializers
from .models import ReviewModel, ShopModel
import tldextract
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = '__all__'
        read_only_fields = ('shop', 'user')

    def domain_obj_from_shop_link(self, shop_link):
        domain = tldextract.extract(shop_link).domain
        domain, created = ShopModel.objects.get_or_create(domain=domain)
        return domain

    def create(self, validated_data):
        domain = self.domain_obj_from_shop_link(validated_data['shop_link'])
        validated_data['shop'] = domain
        review = ReviewModel.objects.create(**validated_data)
        review.domain = domain
        return review

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.shop_link = validated_data.get('shop_link', instance.shop_link)
        instance.shop = self.domain_obj_from_shop_link(validated_data.get('shop_link', instance.shop_link))

        instance.save()
        return instance


class ShopSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'shop_domain': instance.domain,
            'review_count': instance.review_count,
            'avg_rating': instance.avg_rating,
        }


class UserReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'reviews']
