from django.test import TestCase
from django.contrib.auth import get_user_model




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