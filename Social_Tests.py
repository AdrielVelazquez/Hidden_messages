import unittest

from SocialWire import valid_messages, check_validity, digit_validation


class TestValidMessagesFunctions(unittest.TestCase):

    def testValidMessage(self):
        '''
        Verify that proper empty strings are returned for True Expressions
        '''
        self.assertEqual(valid_messages('Za'), '')
        self.assertEqual(valid_messages('Ma'), 'Ma')
        self.assertEqual(valid_messages("MZa"), "")
        self.assertEqual(valid_messages("M1Za"), "")


    def testCheckValidity(self):
        '''
        Verify the output is either Valid or Invalid
        '''
        self.assertEqual(check_validity(valid_messages('Za')), 'Valid')
        self.assertEqual(check_validity(valid_messages('Ma')), 'Invalid')
        self.assertEqual(check_validity(valid_messages("MZa")), "Valid")

    def testDigitalValidation(self):
        '''
        Verify that numbered messages output as valid or not
        '''
        self.assertEqual(digit_validation(2, "aa"), "")
        self.assertEqual(digit_validation(2, "Ma"), "Invalid")
        self.assertEqual(digit_validation(2, "Maa"), "Invalid")
        self.assertEqual(digit_validation(2, "Maaa"), "")
        self.assertEqual(digit_validation(2, "ZaZaZa"), "")
        self.assertEqual(digit_validation(2, "ZaZaMa"), "Invalid")

if __name__ == '__main__':
    unittest.main()