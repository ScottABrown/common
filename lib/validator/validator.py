"""
Validator.py
(c) 2015    Scott A. Brown  scottbrown0001@gmail.com
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
The Validator class hierarchy provides a representation of arbitrary
combinations of various tests that can be applied to determine if a
given target entity meets some set of criteria.

Validator
    ComboValidator
        AndValidator
        OrValidator
        NotValidator
    MembershipValidator
    FunctionValidator
        RegexValidator



Handling null targets and criteria:

Handling empty boolean combinations:

Handling exceptions:
-------------------------------
By default, exceptions encountered while executing the check() method
of a validator will be raised to the calling code. In some
circumstances certain exceptions may indicate a condition that should
be treated as a "pass" or a "fail" with the corresponding True or
False return value.

To facilitate this, exceptions can be designated for such handling at
either the class or the instance level using the pass_exceptions and
the fail_exceptions member variables.

The instance variable has precedence over the class variable.

A particular exception can occur in the instance's pass_exceptions and
the class fail_exceptions or vice-versa, but the same exception can't
occur in both the pass_exceptions and fail_exceptions at the same
level of precedence. Attempting to add an exception to the second list
at the same precedence level will result in a ValueError.

"""


class Validator(object):
    """
    The basic Validator class tests targets for equality (==) with the
    value stored in its "criterion" field and returns the result.
    """
    def __init__(self, criterion):
        """Class initializer. """
        self.criterion = criterion

    def check(self, target):
        """
        Return the result of an '==' comparison between target and the
        Validators criterion.
        """
        return target == self.criterion


class ComboValidator(Validator):
    """
    ComboValidator provides a base class for subclasses that take a list
    of Validtors as criteria. It provides functionality for adding criteria
    and ensuring that only other Validators are used as criteria list members.
    """
    ValidatorRequiredErrorMsg = (
        'can only add instances of Validator to ComboValidator criteria'
        )

    def __init__(self, *criteria):
        """Class initializer."""
        criteria_as_list = list(criteria)
        if not all(isinstance(c, Validator) for c in criteria):
            raise TypeError(ComboValidator.ValidatorRequiredErrorMsg)
        super(ComboValidator, self).__init__(criteria_as_list)

    def add(self, newcriterion):
        """Add a new criterion to the criteria list."""
        if not isinstance(newcriterion, Validator):
            raise TypeError(ComboValidator.ValidatorRequiredErrorMsg)

        self.criteria.append(newcriterion)
