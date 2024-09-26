# coding: utf-8

"""
    PreForm API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.40.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from formlabs_local_api.models.print_validation_result_model_per_model_results_value import PrintValidationResultModelPerModelResultsValue

class TestPrintValidationResultModelPerModelResultsValue(unittest.TestCase):
    """PrintValidationResultModelPerModelResultsValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PrintValidationResultModelPerModelResultsValue:
        """Test PrintValidationResultModelPerModelResultsValue
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PrintValidationResultModelPerModelResultsValue`
        """
        model = PrintValidationResultModelPerModelResultsValue()
        if include_optional:
            return PrintValidationResultModelPerModelResultsValue(
                cups = 56,
                unsupported_minima = 56,
                undersupported = True,
                has_seamline = True
            )
        else:
            return PrintValidationResultModelPerModelResultsValue(
        )
        """

    def testPrintValidationResultModelPerModelResultsValue(self):
        """Test PrintValidationResultModelPerModelResultsValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
