from django.test import TestCase
from rest_framework.test import APITestCase
from .models import ShopModel, ReviewModel
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from .serializers import ReviewSerializer
import tldextract
from django.shortcuts import get_object_or_404
from django.http.response import Http404

TEST_STORE_LINK = 'http://store.com'


class TestReview(APITestCase):
    @classmethod
    def setUpTestData(cls):
        user_model = get_user_model()

        cls.test_user = user_model(username='test_user',
                                   email='test@mail.com',
                                   password='password')
        cls.test_user.save()

    def setUp(self):
        self.client.force_login(self.test_user)
        domain = tldextract.extract(TEST_STORE_LINK).domain
        domain, created = ShopModel.objects.get_or_create(domain=domain)

        self.test_review = ReviewModel(shop_link=TEST_STORE_LINK,
                                       shop=domain,
                                       user=self.test_user,
                                       title='test_title',
                                       description='test_description',
                                       rating=5)
        self.test_review.save()

    def tearDown(self):
        self.test_review.delete()

    def test_review_create(self):
        """
        Ensure we can create a new review
        """
        url = reverse('reviews:reviews-list')
        data = {'shop_link': 'http://store.com',
                'title': 'shop',
                'description': 'i like it!',
                'rating': 5}
        reviews_count = ReviewModel.objects.count()

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ReviewModel.objects.count(), reviews_count+1)
        self.assertEqual(ReviewModel.objects.latest('id').description, 'i like it!')

    def test_review_get_edit(self):
        """
        Ensure we can edit review
        """
        old_review = ReviewModel.objects.get()
        url = reverse('reviews:reviews-detail', args=[old_review.id])

        data = {'description': 'i was wring!',
                'rating': 1}

        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['description'], old_review.description)
        self.assertEqual(ReviewModel.objects.get().description, 'i was wring!')

    def test_review_delete(self):
        """
        Ensure we can delete review
        """
        old_review = ReviewModel.objects.get()
        url = reverse('reviews:reviews-detail', args=[old_review.id])

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
