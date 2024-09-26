# coding: utf-8

"""
    Formlabs Developer API

    The Formlabs Dashboard Developer API provides resources to integrate Formlabs products into customer’s workflow and existing systems

    The version of the OpenAPI document: 0.1.0
    Contact: api-inquiry@formlabs.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from formlabs_web_api.models.basic_user import BasicUser
from formlabs_web_api.models.harvest_status_enum import HarvestStatusEnum
from formlabs_web_api.models.print_part import PrintPart
from formlabs_web_api.models.print_run_feedback import PrintRunFeedback
from formlabs_web_api.models.print_run_note import PrintRunNote
from formlabs_web_api.models.print_run_success import PrintRunSuccess
from formlabs_web_api.models.print_thumbnail_serializer_only_thumbnail import PrintThumbnailSerializerOnlyThumbnail
from formlabs_web_api.models.printer_group import PrinterGroup
from formlabs_web_api.models.status_enum import StatusEnum
from typing import Optional, Set
from typing_extensions import Self

class PrintRunWithFleetControlData(BaseModel):
    """
    PrintRunWithFleetControlData
    """ # noqa: E501
    guid: StrictStr
    name: StrictStr
    printer: StrictStr
    status: StatusEnum
    using_open_mode: Optional[StrictBool]
    z_height_offset_mm: Optional[Union[StrictFloat, StrictInt]]
    print_started_at: Optional[datetime]
    print_finished_at: Optional[datetime]
    layer_count: StrictInt
    volume_ml: Union[StrictFloat, StrictInt]
    material: Optional[StrictStr]
    layer_thickness_mm: Union[StrictFloat, StrictInt]
    currently_printing_layer: StrictInt
    estimated_duration_ms: StrictInt
    elapsed_duration_ms: StrictInt
    estimated_time_remaining_ms: StrictInt
    created_at: datetime
    print_run_success: PrintRunSuccess
    feedback: PrintRunFeedback
    firmware_version: Optional[StrictStr]
    cartridge: Optional[StrictStr]
    front_cartridge: Optional[StrictStr]
    back_cartridge: Optional[StrictStr]
    tank: Optional[StrictStr]
    cylinder: Optional[StrictStr]
    note: PrintRunNote
    print_thumbnail: PrintThumbnailSerializerOnlyThumbnail
    post_print_photo_url: Optional[StrictStr]
    user: BasicUser
    user_custom_label: StrictStr
    group: PrinterGroup
    adaptive_thickness: StrictBool
    probably_finished: StrictBool
    message: Optional[StrictStr]
    print_job: Optional[StrictStr]
    material_name: StrictStr
    print_settings_name: StrictStr
    print_settings_code: StrictStr
    cloud_queue_item: Optional[Dict[str, Any]]
    form_auto_serial: Optional[StrictStr]
    form_auto_fw_version: Optional[StrictStr]
    harvest_status: Optional[HarvestStatusEnum]
    parts: List[PrintPart]
    __properties: ClassVar[List[str]] = ["guid", "name", "printer", "status", "using_open_mode", "z_height_offset_mm", "print_started_at", "print_finished_at", "layer_count", "volume_ml", "material", "layer_thickness_mm", "currently_printing_layer", "estimated_duration_ms", "elapsed_duration_ms", "estimated_time_remaining_ms", "created_at", "print_run_success", "feedback", "firmware_version", "cartridge", "front_cartridge", "back_cartridge", "tank", "cylinder", "note", "print_thumbnail", "post_print_photo_url", "user", "user_custom_label", "group", "adaptive_thickness", "probably_finished", "message", "print_job", "material_name", "print_settings_name", "print_settings_code", "cloud_queue_item", "form_auto_serial", "form_auto_fw_version", "harvest_status", "parts"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PrintRunWithFleetControlData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "printer",
            "status",
            "using_open_mode",
            "z_height_offset_mm",
            "print_started_at",
            "print_finished_at",
            "layer_count",
            "volume_ml",
            "material",
            "layer_thickness_mm",
            "currently_printing_layer",
            "estimated_duration_ms",
            "elapsed_duration_ms",
            "estimated_time_remaining_ms",
            "created_at",
            "print_run_success",
            "feedback",
            "firmware_version",
            "cartridge",
            "front_cartridge",
            "back_cartridge",
            "tank",
            "cylinder",
            "note",
            "print_thumbnail",
            "post_print_photo_url",
            "user",
            "user_custom_label",
            "group",
            "adaptive_thickness",
            "probably_finished",
            "message",
            "print_job",
            "material_name",
            "print_settings_name",
            "print_settings_code",
            "cloud_queue_item",
            "form_auto_serial",
            "form_auto_fw_version",
            "parts",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of print_run_success
        if self.print_run_success:
            _dict['print_run_success'] = self.print_run_success.to_dict()
        # override the default output from pydantic by calling `to_dict()` of feedback
        if self.feedback:
            _dict['feedback'] = self.feedback.to_dict()
        # override the default output from pydantic by calling `to_dict()` of note
        if self.note:
            _dict['note'] = self.note.to_dict()
        # override the default output from pydantic by calling `to_dict()` of print_thumbnail
        if self.print_thumbnail:
            _dict['print_thumbnail'] = self.print_thumbnail.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict['group'] = self.group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in parts (list)
        _items = []
        if self.parts:
            for _item_parts in self.parts:
                if _item_parts:
                    _items.append(_item_parts.to_dict())
            _dict['parts'] = _items
        # set to None if using_open_mode (nullable) is None
        # and model_fields_set contains the field
        if self.using_open_mode is None and "using_open_mode" in self.model_fields_set:
            _dict['using_open_mode'] = None

        # set to None if z_height_offset_mm (nullable) is None
        # and model_fields_set contains the field
        if self.z_height_offset_mm is None and "z_height_offset_mm" in self.model_fields_set:
            _dict['z_height_offset_mm'] = None

        # set to None if print_started_at (nullable) is None
        # and model_fields_set contains the field
        if self.print_started_at is None and "print_started_at" in self.model_fields_set:
            _dict['print_started_at'] = None

        # set to None if print_finished_at (nullable) is None
        # and model_fields_set contains the field
        if self.print_finished_at is None and "print_finished_at" in self.model_fields_set:
            _dict['print_finished_at'] = None

        # set to None if material (nullable) is None
        # and model_fields_set contains the field
        if self.material is None and "material" in self.model_fields_set:
            _dict['material'] = None

        # set to None if firmware_version (nullable) is None
        # and model_fields_set contains the field
        if self.firmware_version is None and "firmware_version" in self.model_fields_set:
            _dict['firmware_version'] = None

        # set to None if cartridge (nullable) is None
        # and model_fields_set contains the field
        if self.cartridge is None and "cartridge" in self.model_fields_set:
            _dict['cartridge'] = None

        # set to None if front_cartridge (nullable) is None
        # and model_fields_set contains the field
        if self.front_cartridge is None and "front_cartridge" in self.model_fields_set:
            _dict['front_cartridge'] = None

        # set to None if back_cartridge (nullable) is None
        # and model_fields_set contains the field
        if self.back_cartridge is None and "back_cartridge" in self.model_fields_set:
            _dict['back_cartridge'] = None

        # set to None if tank (nullable) is None
        # and model_fields_set contains the field
        if self.tank is None and "tank" in self.model_fields_set:
            _dict['tank'] = None

        # set to None if cylinder (nullable) is None
        # and model_fields_set contains the field
        if self.cylinder is None and "cylinder" in self.model_fields_set:
            _dict['cylinder'] = None

        # set to None if post_print_photo_url (nullable) is None
        # and model_fields_set contains the field
        if self.post_print_photo_url is None and "post_print_photo_url" in self.model_fields_set:
            _dict['post_print_photo_url'] = None

        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['message'] = None

        # set to None if print_job (nullable) is None
        # and model_fields_set contains the field
        if self.print_job is None and "print_job" in self.model_fields_set:
            _dict['print_job'] = None

        # set to None if cloud_queue_item (nullable) is None
        # and model_fields_set contains the field
        if self.cloud_queue_item is None and "cloud_queue_item" in self.model_fields_set:
            _dict['cloud_queue_item'] = None

        # set to None if form_auto_serial (nullable) is None
        # and model_fields_set contains the field
        if self.form_auto_serial is None and "form_auto_serial" in self.model_fields_set:
            _dict['form_auto_serial'] = None

        # set to None if form_auto_fw_version (nullable) is None
        # and model_fields_set contains the field
        if self.form_auto_fw_version is None and "form_auto_fw_version" in self.model_fields_set:
            _dict['form_auto_fw_version'] = None

        # set to None if harvest_status (nullable) is None
        # and model_fields_set contains the field
        if self.harvest_status is None and "harvest_status" in self.model_fields_set:
            _dict['harvest_status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PrintRunWithFleetControlData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "guid": obj.get("guid"),
            "name": obj.get("name"),
            "printer": obj.get("printer"),
            "status": obj.get("status"),
            "using_open_mode": obj.get("using_open_mode"),
            "z_height_offset_mm": obj.get("z_height_offset_mm"),
            "print_started_at": obj.get("print_started_at"),
            "print_finished_at": obj.get("print_finished_at"),
            "layer_count": obj.get("layer_count"),
            "volume_ml": obj.get("volume_ml"),
            "material": obj.get("material"),
            "layer_thickness_mm": obj.get("layer_thickness_mm"),
            "currently_printing_layer": obj.get("currently_printing_layer"),
            "estimated_duration_ms": obj.get("estimated_duration_ms"),
            "elapsed_duration_ms": obj.get("elapsed_duration_ms"),
            "estimated_time_remaining_ms": obj.get("estimated_time_remaining_ms"),
            "created_at": obj.get("created_at"),
            "print_run_success": PrintRunSuccess.from_dict(obj["print_run_success"]) if obj.get("print_run_success") is not None else None,
            "feedback": PrintRunFeedback.from_dict(obj["feedback"]) if obj.get("feedback") is not None else None,
            "firmware_version": obj.get("firmware_version"),
            "cartridge": obj.get("cartridge"),
            "front_cartridge": obj.get("front_cartridge"),
            "back_cartridge": obj.get("back_cartridge"),
            "tank": obj.get("tank"),
            "cylinder": obj.get("cylinder"),
            "note": PrintRunNote.from_dict(obj["note"]) if obj.get("note") is not None else None,
            "print_thumbnail": PrintThumbnailSerializerOnlyThumbnail.from_dict(obj["print_thumbnail"]) if obj.get("print_thumbnail") is not None else None,
            "post_print_photo_url": obj.get("post_print_photo_url"),
            "user": BasicUser.from_dict(obj["user"]) if obj.get("user") is not None else None,
            "user_custom_label": obj.get("user_custom_label"),
            "group": PrinterGroup.from_dict(obj["group"]) if obj.get("group") is not None else None,
            "adaptive_thickness": obj.get("adaptive_thickness"),
            "probably_finished": obj.get("probably_finished"),
            "message": obj.get("message"),
            "print_job": obj.get("print_job"),
            "material_name": obj.get("material_name"),
            "print_settings_name": obj.get("print_settings_name"),
            "print_settings_code": obj.get("print_settings_code"),
            "cloud_queue_item": obj.get("cloud_queue_item"),
            "form_auto_serial": obj.get("form_auto_serial"),
            "form_auto_fw_version": obj.get("form_auto_fw_version"),
            "harvest_status": obj.get("harvest_status"),
            "parts": [PrintPart.from_dict(_item) for _item in obj["parts"]] if obj.get("parts") is not None else None
        })
        return _obj


