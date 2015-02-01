import unittest
import Validator


class TestValidator(unittest.TestCase):

    def test_validator_0(self):
        """
        Test that initialization and check works properly for a variety
        of criteria and targets.
        """
        validator = Validator.Validator(0)

        # Confirm that exactly one parameter is required.
        self.assertRaises(TypeError, validator.check)
        self.assertRaises(TypeError, validator.check, 1, 2)

        # Confirm that checks that should return True, do so.
        self.assertTrue(validator.check(0))
        self.assertTrue(validator.check(False))

        # Confirm that checks that should return False, do so.
        self.assertFalse(validator.check(1))
        self.assertFalse(validator.check(True))
        self.assertFalse(validator.check('a'))
        self.assertFalse(validator.check([]))
        self.assertFalse(validator.check([1, 2, 3]))
        self.assertFalse(validator.check(None))

    def test_validator_1(self):
        """
        Test that initialization and check works properly for a variety
        of criteria and targets.
        """
        validator = Validator.Validator(1)

        # Confirm that exactly one parameter is required.
        self.assertRaises(TypeError, validator.check)
        self.assertRaises(TypeError, validator.check, 1, 2)

        # Confirm that checks that should return True, do so.
        self.assertTrue(validator.check(1))
        self.assertTrue(validator.check(True))

        # Confirm that checks that should return False, do so.
        self.assertFalse(validator.check(None))
        self.assertFalse(validator.check(0))
        self.assertFalse(validator.check('a'))
        self.assertFalse(validator.check([]))
        self.assertFalse(validator.check([1, 2, 3]))
        self.assertFalse(validator.check(False))

    def test_validator_none(self):
        """
        Test that initialization and check works properly for a variety
        of criteria and targets.
        """
        validator = Validator.Validator(None)

        # Confirm that exactly one parameter is required.
        self.assertRaises(TypeError, validator.check)
        self.assertRaises(TypeError, validator.check, 1, 2)

        # Confirm that checks that should return True, do so.
        self.assertTrue(validator.check(None))

        # Confirm that checks that should return False, do so.
        self.assertFalse(validator.check(1))
        self.assertFalse(validator.check(0))
        self.assertFalse(validator.check('a'))
        self.assertFalse(validator.check([]))
        self.assertFalse(validator.check([1, 2, 3]))
        self.assertFalse(validator.check(True))
        self.assertFalse(validator.check(False))


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestValidator)
    unittest.TextTestRunner(verbosity=3).run(suite)
