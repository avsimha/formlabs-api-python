# coding: utf-8

"""
    PreForm API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.40.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from formlabs_local_api.models.sls import SLS

class TestSLS(unittest.TestCase):
    """SLS unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SLS:
        """Test SLS
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SLS`
        """
        model = SLS()
        if include_optional:
            return SLS(
                total_powder_ml = 1.337,
                total_powder_kg = 1.337,
                total_sintered_powder_ml = 1.337,
                total_sintered_powder_kg = 1.337,
                mass_packing_density = 1.337
            )
        else:
            return SLS(
                total_powder_ml = 1.337,
                total_powder_kg = 1.337,
                total_sintered_powder_ml = 1.337,
                total_sintered_powder_kg = 1.337,
                mass_packing_density = 1.337,
        )
        """

    def testSLS(self):
        """Test SLS"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
