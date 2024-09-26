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
import json
from enum import Enum
from typing_extensions import Self


class StatusEnum(str, Enum):
    """
    * `QUEUED` - Queued * `PREPRINT` - Preprint * `PRINTING` - Printing * `PAUSED` - Paused * `FINISHED` - Finished * `ABORTING` - Aborting * `ABORTED` - Aborted * `ERROR` - Error * `WAITING_FOR_RESOLUTION` - Waiting for Resolution * `PREHEAT` - Preheat * `PRECOAT` - Precoat * `POSTCOAT` - Postcoat
    """

    """
    allowed enum values
    """
    QUEUED = 'QUEUED'
    PREPRINT = 'PREPRINT'
    PRINTING = 'PRINTING'
    PAUSED = 'PAUSED'
    FINISHED = 'FINISHED'
    ABORTING = 'ABORTING'
    ABORTED = 'ABORTED'
    ERROR = 'ERROR'
    WAITING_FOR_RESOLUTION = 'WAITING_FOR_RESOLUTION'
    PREHEAT = 'PREHEAT'
    PRECOAT = 'PRECOAT'
    POSTCOAT = 'POSTCOAT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StatusEnum from a JSON string"""
        return cls(json.loads(json_str))


