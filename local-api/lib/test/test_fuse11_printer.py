# coding: utf-8

"""
    PreForm API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.40.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from formlabs_local_api.models.fuse11_printer import Fuse11Printer

class TestFuse11Printer(unittest.TestCase):
    """Fuse11Printer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Fuse11Printer:
        """Test Fuse11Printer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Fuse11Printer`
        """
        model = Fuse11Printer()
        if include_optional:
            return Fuse11Printer(
                id = '',
                product_name = '',
                status = '',
                is_connected = True,
                connection_type = 'UNKNOWN',
                ip_address = '',
                firmware_version = '',
                is_remote_print_enabled = True,
                estimated_print_time_remaining_ms = 56,
                bed_temperature_c = 1.337,
                powder_level = '',
                printing_layer = 56,
                printing_guid = '',
                cylinder_material_code = '',
                cylinder_serial = '',
                printer_material_code = '',
                powder_credit_g = 1.337
            )
        else:
            return Fuse11Printer(
                id = '',
                product_name = '',
                status = '',
                is_connected = True,
                connection_type = 'UNKNOWN',
                ip_address = '',
                firmware_version = '',
                is_remote_print_enabled = True,
                estimated_print_time_remaining_ms = 56,
                bed_temperature_c = 1.337,
                powder_level = '',
                printing_layer = 56,
                printing_guid = '',
                cylinder_material_code = '',
                cylinder_serial = '',
                printer_material_code = '',
                powder_credit_g = 1.337,
        )
        """

    def testFuse11Printer(self):
        """Test Fuse11Printer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
