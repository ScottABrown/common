import unittest
import validator


class TestValidatorExceptions(unittest.TestCase):
    """
    Test the management and use of the class and instance level
    pass_exceptions and fail_exceptions lists.
    """
    def test_instance_add_exceptions(self):
        """
        Test that exceptions can be added to an instance's exceptions
        management lists unless one occurs already in the "other"
        list, in which case a ValueError is raised.
        """
        a_validator = validator.Validator(1)

        self.assertEqual(a_validator.pass_exceptions, [])
        self.assertEqual(a_validator.fail_exceptions, [])

        # Basic assignment to exception lists is OK.
        a_validator.pass_exceptions = [IOError]
        a_validator.fail_exceptions = [TabError]

        self.assertEqual(a_validator.pass_exceptions, [IOError])
        self.assertEqual(a_validator.fail_exceptions, [TabError])

        # A second assignment to exception lists results in a list
        # with two Exceptions.
        a_validator.pass_exceptions = a_validator.pass_exceptions.append(
            OSError
            )
        a_validator.fail_exceptions = a_validator.fail_exceptions.append(
            NotImplementedError
            )

        self.assertEqual(len(a_validator.pass_exceptions), 2)
        self.assertTrue(IOError in a_validator.pass_exceptions)
        self.assertTrue(OSError in a_validator.pass_exceptions)

        self.assertEqual(len(a_validator.fail_exceptions), 2)
        self.assertTrue(TabError in a_validator.fail_exceptions)
        self.assertTrue(NotImplementedError in a_validator.fail_exceptions)

        # Trying to add an exception that's already in the "other" list
        # raises a ValueError exception. Check when the list being modified
        # was previously empty and when it was not; also make sure it doesn't
        # do anything funky when ValueError is the duplicate exception in
        # question.
        a_validator.pass_exceptions = []
        a_validator.fail_exceptions = [ValueError]

        self.assertRaises(
            # Hmm, this is a property, right? How to do this? Don't think 
            # assertRaises will work, just have to wrap in try and check the
            # result after.
            )


class TestValidatorCheck(unittest.TestCase):
    """
    Test that initialization and check works properly for a variety
    of criteria and targets.
    """

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


# Build a suite with all the tests
# class AllTests(unittest.TestCase):
class AllTests():
    def suite(self):
        suite1 = unittest.TestLoader().loadTestsFromTestCase(
            TestValidatorCheck
            )
        suite2 = unittest.TestLoader().loadTestsFromTestCase(
            TestValidatorExceptions
            )
        return unittest.TestSuite([suite1, suite2])

if __name__ == "__main__":
    # unittest.main()
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestValidatorCheck)
    alltests = AllTests()
    suite = alltests.suite()
    unittest.TextTestRunner(verbosity=3).run(suite)
    print "Hello World!"
