# coding: utf-8

"""
    PreForm API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.40.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from formlabs_local_api.models.device_status_model import DeviceStatusModel

class TestDeviceStatusModel(unittest.TestCase):
    """DeviceStatusModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceStatusModel:
        """Test DeviceStatusModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceStatusModel`
        """
        model = DeviceStatusModel()
        if include_optional:
            return DeviceStatusModel(
                id = '',
                product_name = '',
                status = '',
                is_connected = True,
                connection_type = 'UNKNOWN',
                ip_address = '',
                firmware_version = '',
                dashboard_group_id = '',
                dashboard_queue_id = '',
                is_remote_print_enabled = True,
                estimated_print_time_remaining_ms = 56,
                tank_id = '',
                tank_material_code = '',
                cartridge_data = {
                    'key' : formlabs_local_api.models.form_4_printer_cartridge_data_value.Form_4_Printer_cartridge_data_value(
                        cartridge_material_code = '', 
                        cartridge_estimated_volume_dispensed_m_l = 1.337, 
                        cartridge_original_volume_m_l = 1.337, )
                    },
                ready_to_print_now = True,
                form_auto_status = '',
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
            return DeviceStatusModel(
                id = '',
                product_name = '',
                status = '',
                is_connected = True,
                connection_type = 'UNKNOWN',
                ip_address = '',
                firmware_version = '',
                dashboard_group_id = '',
                dashboard_queue_id = '',
                is_remote_print_enabled = True,
                estimated_print_time_remaining_ms = 56,
                tank_id = '',
                tank_material_code = '',
                cartridge_data = {
                    'key' : formlabs_local_api.models.form_4_printer_cartridge_data_value.Form_4_Printer_cartridge_data_value(
                        cartridge_material_code = '', 
                        cartridge_estimated_volume_dispensed_m_l = 1.337, 
                        cartridge_original_volume_m_l = 1.337, )
                    },
                ready_to_print_now = True,
                form_auto_status = '',
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

    def testDeviceStatusModel(self):
        """Test DeviceStatusModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
