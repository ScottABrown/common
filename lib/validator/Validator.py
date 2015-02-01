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
            raise TypeError(ValidatorRequiredErrorMsg)
        super(ComboValidator, self).__init__(criteria_as_list)

    def add(self, newcriterion):
        """Add a new criterion to the criteria list."""
        if not isinstance(newcriterion, Validator):
            raise TypeError(ValidatorRequiredErrorMsg)

        self.criteria.append(newcriterion)




