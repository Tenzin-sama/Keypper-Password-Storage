import unittest
import backend.sqlpass # file name

class UnitTesting(unittest.TestCase):

     def test_login(self):
         """ test if the login function works on table 'users' """
         data = backend.sqlpass.data()
         actual_res = data.check_pass('Apple', 'bee')
         self.assertTrue(actual_res)

     def test_userexists(self):
         """ test if the function to check the existence of a user works"""
         data = backend.sqlpass.data()
         actual_res = data.check_user('Apple')
         self.assertTrue(actual_res)

     def test_adduser(self):
         """ test if new users can be added"""
         data = backend.sqlpass.data()
         actual_res = data.add_user('Tester1', 'pass1')
         self.assertTrue(actual_res)

     def test_datainsert(self):
         """ test if data can be added to table 'data' """
         data = backend.sqlpass.data()
         actual_res = data.add_data('Apple', 'Github', 'apple@mail.com', 'appgit', 'gitpass')
         self.assertTrue(actual_res)

     def test_datadelete(self):
         """ test if data can be deleted from table 'data'"""
         data = backend.sqlpass.data()
         actual_res = data.add_data('Apple', 'Github', 'apple@mail.com', 'appgit', 'gitpass')
         self.assertTrue(actual_res)