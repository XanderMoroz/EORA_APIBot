import unittest
from util_functions import get_user_state, set_user_state


class TestCatOrBreadBot(unittest.TestCase):
    def setUp(self):
        self.user_state = {123 : '1'}
    def test_get_new_user_state(self):
        """Попытка извлечь 'состояние' нового пользователя"""
        self.assertEqual(get_user_state(123), '0')
    def test_set_user_state(self):
        """Попытка установить новое 'состояние' пользователя"""
        self.assertEqual(set_user_state(123, "1"), True)
# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()

