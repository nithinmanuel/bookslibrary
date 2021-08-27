from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from .views import SignupPageView



class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        new_user = User.objects.create_user(username ='nithin', 
        email = 'cappanmatt@gmail.com' , password = 'mankindtoday' )

        self.assertEqual(new_user.username ,'nithin')
        self.assertEqual(new_user.email , 'cappanmatt@gmail.com')
        self.assertTrue(new_user.is_active)
        self.assertFalse(new_user.is_staff)
        self.assertFalse(new_user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(username = 'superadmin',
         email = 'superadmin@email.com', password = 'testpass123')

        self.assertEqual(admin_user.username ,'superadmin' )  
        self.assertEqual(admin_user.email , 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)






    class SignupTests(TestCase):
        username = 'newuser'
        email = 'newuser@email.com'

        def SetUp(self):
            url = reverse('account_signup')
            self.response = self.client.get(url)

        def test_signup_template(self):
            self.assertEqual(self.response.status_code, 200)
            self.assertTemplateUsed(self.response , 'account/signup.html')
            self.assertTemplateContains(self.response, 'Sign Up')
            self.assertTemplateNotContains(self.response, 'Hi there! I should not be on the page.')

        def test_signup_form(self):
            new_user = get_user_model().objects.create_user(self.username, self.email) 
            self.assertEqual(get_user_model().objects.all().count(), 1)
            self.assertEqual(get_user_model().objects.all()[0].username, self.username)
            self.assertEqual(get_user_model().objects.all()[0].email, self.email)



    





 # username lsd
 # password lsdkittiyo99
 # nith@email.com  
"""
class SignupPageTest(SimpleTestCase):


    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)


    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_homepage_url_template(self):
        self.assertTemplateUsed(self.response, 'signup.html')
    
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Sign Up')
    
    def test_homepage_contains_incorrect_html(self):
        self.assertNotContains(self.response, 'is it here')
"""
        

           







# Create your tests here.
