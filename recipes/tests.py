from django.test import TestCase
from django.urls import resolve, reverse


class RecipeURLsTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_detail_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')


class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func.__name__, 'home')

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func.__name__, 'category')

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func.__name__, 'recipe')


class ModelsTest(TestCase):
    def test_recipe_model_str_method(self):
        from .models import Recipe
        recipe = Recipe(title='Test Recipe')
        self.assertEqual(str(recipe), 'Test Recipe')

    def test_category_model_str_method(self):
        from .models import Category
        category = Category(name='Test Category')
        self.assertEqual(str(category), 'Test Category')

    def test_ingredient_model_str_method(self):
        from .models import Ingredient
        ingredient = Ingredient(name='Test Ingredient')
        self.assertEqual(str(ingredient), 'Test Ingredient')

    def test_step_model_str_method(self):
        from .models import Step
        step = Step(description='Test Step')
        self.assertEqual(str(step), 'Test Step')
