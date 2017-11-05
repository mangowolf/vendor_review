# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Company
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")
        self.company_name = "Write world class code"
        self.website = "http://www.stuff.com"
        self.headquarters = "San Francisco"
        self.industry = "Technology"
        self.revenue = 100
        self.size = 10
        self.founded = "1999-11-01"
        self.summary = "Filler"
        #specify owner of bucketlist
        self.company = Company(company_name=self.company_name, owner=user) 
            #website=self.website, headquarters=self.headquarters,
            #industry = self.industry, revenue=self.revenue, size=self.size, founded=self.founded, summary=self.summary)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")

        #Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        #Since user model instance is not serializable, use its Id/PK
        self.company_data = {'company_name': 'Go to Ibiza', 'owner': user.id}
        self.response = self.client.post(
            reverse('create'),
            self.company_data,
            format="json")

    def test_api_can_create_a_company(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        res = new_client.get('/api/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_can_get_a_company(self):
        """Test the api can get a given company"""
        company = Company.objects.get(id=2)
        response = self.client.get('/api/',
            kwargs={'pk': company.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, company)

    def test_api_can_update_a_company(self):
        """Test the api can update a given company"""
        company = Company.objects.get()
        change_company = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk':company.id}),
            change_company, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_company(self):
        """Test the api can delete a bucketlist."""
        company = Company.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': company.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)



