# coding: utf-8

"""
    PreForm API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.40.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from formlabs_local_api.models.scene_print_post200_response import ScenePrintPost200Response

class TestScenePrintPost200Response(unittest.TestCase):
    """ScenePrintPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScenePrintPost200Response:
        """Test ScenePrintPost200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScenePrintPost200Response`
        """
        model = ScenePrintPost200Response()
        if include_optional:
            return ScenePrintPost200Response(
                job_id = ''
            )
        else:
            return ScenePrintPost200Response(
        )
        """

    def testScenePrintPost200Response(self):
        """Test ScenePrintPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
