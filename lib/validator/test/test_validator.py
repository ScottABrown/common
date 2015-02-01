import unittest
import validator


class TestValidator(unittest.TestCase):

    def test_validator_0(self):
        """
        Test that initialization and check works properly for a variety
        of criteria and targets.
        """
        validator_0 = validator.Validator(0)

        # Confirm that exactly one parameter is required.
        self.assertRaises(TypeError, validator_0.check)
        self.assertRaises(TypeError, validator_0.check, 1, 2)

        # Confirm that checks that should return True, do so.
        self.assertTrue(validator_0.check(0))
        self.assertTrue(validator_0.check(False))

        # Confirm that checks that should return False, do so.
        self.assertFalse(validator_0.check(1))
        self.assertFalse(validator_0.check(True))
        self.assertFalse(validator_0.check('a'))
        self.assertFalse(validator_0.check([]))
        self.assertFalse(validator_0.check([1, 2, 3]))
        self.assertFalse(validator_0.check(None))

    def test_validator_1(self):
        """
        Test that initialization and check works properly for a variety
        of criteria and targets.
        """
        validator_1 = validator.Validator(1)

        # Confirm that exactly one parameter is required.
        self.assertRaises(TypeError, validator_1.check)
        self.assertRaises(TypeError, validator_1.check, 1, 2)

        # Confirm that checks that should return True, do so.
        self.assertTrue(validator_1.check(1))
        self.assertTrue(validator_1.check(True))

        # Confirm that checks that should return False, do so.
        self.assertFalse(validator_1.check(None))
        self.assertFalse(validator_1.check(0))
        self.assertFalse(validator_1.check('a'))
        self.assertFalse(validator_1.check([]))
        self.assertFalse(validator_1.check([1, 2, 3]))
        self.assertFalse(validator_1.check(False))

    def test_validator_none(self):
        """
        Test that initialization and check works properly for a variety
        of criteria and targets.
        """
        validator_none = validator.Validator(None)

        # Confirm that exactly one parameter is required.
        self.assertRaises(TypeError, validator_none.check)
        self.assertRaises(TypeError, validator_none.check, 1, 2)

        # Confirm that checks that should return True, do so.
        self.assertTrue(validator_none.check(None))

        # Confirm that checks that should return False, do so.
        self.assertFalse(validator_none.check(1))
        self.assertFalse(validator_none.check(0))
        self.assertFalse(validator_none.check('a'))
        self.assertFalse(validator_none.check([]))
        self.assertFalse(validator_none.check([1, 2, 3]))
        self.assertFalse(validator_none.check(True))
        self.assertFalse(validator_none.check(False))


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestValidator)
    unittest.TextTestRunner(verbosity=3).run(suite)
