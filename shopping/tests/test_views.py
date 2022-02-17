from pprint import pprint
from django.contrib.auth import get_user_model
from django.urls.base import reverse

from shopping.models import ShoppingItem, Category
import pytest


@pytest.fixture
def some_user(client):
    user = get_user_model().objects.filter(email='wendell.gee@example.com')
    if user:
        user = user[0]
    else:
        user = get_user_model().objects.create_user(
            email='wendell.gee@example.com',
            password='topsecret',
            username='geewendell'
        )

    credentials = {
        'login': 'wendell.gee@example.com',
        'password': 'topsecret'
    }
    
    return user


@pytest.mark.django_db
def test_users_can_delete_items(client, some_user):
    client.force_login(some_user)
    
    my_item = ShoppingItem.objects.create(description='cola', quantity=3)

    client.post(reverse('shopping_item_delete', args=[my_item.slug]), follow=True)

    response = client.get(reverse('shopping_items'))
    assert response.status_code == 200
    assert len(response.context['shoppingItem']) == 0


@pytest.mark.django_db
def test_users_can_add_items(client, some_user):
    client.force_login(some_user)
    form_object = {
        'description': 'no dice',
        'quantity': 12,
        'category': ''
    }
    
    response = client.post(reverse('shopping_item_create'), data=form_object, follow=True)

    assert response.status_code == 200
    assert len(response.context['shoppingItem']) == 1
    assert response.context['shoppingItem'][0].description == 'no dice'


@pytest.mark.django_db
def test_users_can_see_items(client, some_user):
    client.force_login(some_user)

    ShoppingItem.objects.create(description='cola', quantity=3)
    ShoppingItem.objects.create(description='pepsi', quantity=3)
  
    url = reverse('shopping_items')
    response = client.get(url)

    assert len(response.context['shoppingItem']) == 2
    assert response.context['shoppingItem'][0].description == 'cola'


@pytest.mark.django_db
def test_users_can_update_items(client, some_user):
    client.force_login(some_user)
    form_object = {
        'description': 'no dice',
        'quantity': 12,
        'category': ''
    }
    
    response = client.post(reverse('shopping_item_create'), data=form_object, follow=True)

    edited_form_object = {
        'description': 'yes dice',
        'quantity': 1,
        'category': ''
    }

    response = client.post(
        reverse('shopping_item_update', args=[response.context['shoppingItem'][0].slug]), 
        data=edited_form_object,
        follow=True
    )

    assert response.status_code == 200
    assert len(response.context['shoppingItem']) == 1
    assert response.context['shoppingItem'][0].description == 'yes dice'


@pytest.mark.django_db
def test_users_can_delete_categories(client, some_user):
    client.force_login(some_user)
    
    my_item = Category.objects.create(name='name', category_type='D')

    client.post(reverse('category_delete', args=[my_item.slug]), follow=True)

   
    assert Category.objects.count() == 0


@pytest.mark.django_db
def test_users_can_add_categories(client, some_user):
    client.force_login(some_user)
    form_object = {
        'name': 'department',
        'category_type': 'D',  
    }
    
    response = client.post(reverse('category_create'), data=form_object, follow=True)

    assert Category.objects.count() == 1
    assert Category.objects.filter(name='department').exists() is True


@pytest.mark.django_db
def test_users_can_update_categories(client, some_user):
    client.force_login(some_user)
    form_object = {
        'name': 'department',
        'category_type': 'D',  
    }
    
    response = client.post(reverse('category_create'), data=form_object, follow=True)

    edited_form_object = {
        'name': 'department',
        'category_type': 'I',  
    }

    response = client.post(reverse(
        'category_update',
        args=[Category.objects.filter(name='department').first().slug]),
        data=edited_form_object,
        follow=True
    )

    assert response.status_code == 200

    assert Category.objects.filter(name='department').first().category_type == 'I'


@pytest.mark.django_db
def test_users_can_view_category(client, some_user):
    client.force_login(some_user)
    form_object = {
        'name': 'department',
        'category_type': 'D',  
    }
    
    client.post(reverse('category_create'), data=form_object, follow=True)

    response = client.get(
        reverse('category_detail', args=[Category.objects.filter(name='department').first().slug]), 
        follow=True
    )

    assert response.status_code == 200
    assert response.context['category'].name == form_object['name']
    assert response.context['category'].category_type == form_object['category_type']
