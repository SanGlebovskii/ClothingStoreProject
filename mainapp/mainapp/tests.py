from django.test import TestCase, Client
from .forms import ReviewForm
from decimal import Decimal
from django.test import TestCase
from .models import Shoes, Category
from django.contrib.auth.models import User
from django.urls import reverse


class ReviewFormTest(TestCase):
    def test_review_rate(self):
        form_data = {'text': 'Test review', 'rate': 6}
        form = ReviewForm(form_data)
        self.assertFalse(form.is_valid())

class ShoesModelTest(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username='testuser', password='password')
        self.category = Category.objects.create(name='Обувь')
        self.product = Shoes.objects.create(
            category=self.category,
            title='Test shoes',
            slug='test123',
            description='description',
            price=Decimal('1000.00'),
            composition='something',
            fastener_type='something_type',
            lining_material='something_material',
            insole_material='something_insole',
            type_of_heel='something_heel',
            country_of_origin='testBelarus',
            gender='men'

        )

    def test_product(self):
        self.assertEqual(self.product.title, 'Test shoes')
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(self.product.slug, 'test123')
        self.assertEqual(self.product.description, 'description')
        self.assertEqual(self.product.price, Decimal('1000.00'))
        self.assertEqual(self.product.composition, 'something')
        self.assertEqual(self.product.fastener_type, 'something_type')
        self.assertEqual(self.product.lining_material, 'something_material')
        self.assertEqual(self.product.insole_material, 'something_insole')
        self.assertEqual(self.product.type_of_heel, 'something_heel')
        self.assertEqual(self.product.country_of_origin, 'testBelarus')
        self.assertEqual(self.product.gender, 'men')


    def test_category(self):
        self.assertEqual(self.category.name, 'Обувь')

    def test_user(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.password, 'password')

    def test_product_title_max_length(self):
        max_length = self.product._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.category_list = reverse('mainapp:base')

    def test_category_list(self):

        response = self.client.get(self.category_list)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

