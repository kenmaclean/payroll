from django.test import TestCase

# Create your tests here.
from .controller import checkIfPreviouslyProcessed

class CheckIfPreviouslyProcessedTest(TestCase):

    def test_no_file_in_test_database(self):
        """
        This is a terrible test
        better tests would be to checked mocked data gets stored in the test database,
        Test fail and edge cases
        For this excersise this is just a sample
        """
        # this should never exist in test DB as it has no data
        test_file_id = 10

        # returns false if the test file id is not found in the test database
        self.assertIs(checkIfPreviouslyProcessed(test_file_id), False)
