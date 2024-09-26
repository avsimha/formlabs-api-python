# coding: utf-8

"""
    PreForm API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.40.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from formlabs_local_api.models.scene_auto_support_post_request import SceneAutoSupportPostRequest

class TestSceneAutoSupportPostRequest(unittest.TestCase):
    """SceneAutoSupportPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SceneAutoSupportPostRequest:
        """Test SceneAutoSupportPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SceneAutoSupportPostRequest`
        """
        model = SceneAutoSupportPostRequest()
        if include_optional:
            return SceneAutoSupportPostRequest(
                models = None,
                raft_type = 'FULL_RAFT',
                raft_label_enabled = True,
                breakaway_structure_enabled = True,
                density = 0,
                touchpoint_size_mm = 0,
                internal_supports_enabled = True,
                raft_thickness_mm = 0,
                slope_multiplier = 0,
                height_above_raft_mm = 0,
                z_compression_correction_mm = 0,
                early_layer_merge_mm = 0
            )
        else:
            return SceneAutoSupportPostRequest(
                models = None,
        )
        """

    def testSceneAutoSupportPostRequest(self):
        """Test SceneAutoSupportPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
