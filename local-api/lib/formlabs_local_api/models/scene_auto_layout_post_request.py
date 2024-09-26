# coding: utf-8

"""
    PreForm API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.40.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from formlabs_local_api.models.models_selection_model import ModelsSelectionModel
from typing import Optional, Set
from typing_extensions import Self

class SceneAutoLayoutPostRequest(BaseModel):
    """
    SceneAutoLayoutPostRequest
    """ # noqa: E501
    models: ModelsSelectionModel
    model_spacing_mm: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, description="Minimum (non-zero) distance between models in the scene.")
    allow_overlapping_supports: Optional[StrictBool] = Field(default=None, description="Whether to allow rafts to overlap.")
    lock_rotation: Optional[StrictBool] = Field(default=None, description="Whether to keep model rotation about Z fixed during layout.")
    build_platform_2_optimized: Optional[StrictBool] = Field(default=None, description="Whether to optimize the build platform for two models.")
    __properties: ClassVar[List[str]] = ["models", "model_spacing_mm", "allow_overlapping_supports", "lock_rotation", "build_platform_2_optimized"]

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
        """Create an instance of SceneAutoLayoutPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of models
        if self.models:
            _dict['models'] = self.models.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SceneAutoLayoutPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "models": ModelsSelectionModel.from_dict(obj["models"]) if obj.get("models") is not None else None,
            "model_spacing_mm": obj.get("model_spacing_mm"),
            "allow_overlapping_supports": obj.get("allow_overlapping_supports"),
            "lock_rotation": obj.get("lock_rotation"),
            "build_platform_2_optimized": obj.get("build_platform_2_optimized")
        })
        return _obj


