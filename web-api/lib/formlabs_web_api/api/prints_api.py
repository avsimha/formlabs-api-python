# coding: utf-8

"""
    Formlabs Developer API

    The Formlabs Dashboard Developer API provides resources to integrate Formlabs products into customer’s workflow and existing systems

    The version of the OpenAPI document: 0.1.0
    Contact: api-inquiry@formlabs.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from datetime import datetime
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from formlabs_web_api.models.paginated_print_run_with_fleet_control_data_list import PaginatedPrintRunWithFleetControlDataList

from formlabs_web_api.api_client import ApiClient, RequestSerialized
from formlabs_web_api.api_response import ApiResponse
from formlabs_web_api.rest import RESTResponseType


class PrintsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def prints_list(
        self,
        var_date: Annotated[Optional[datetime], Field(description="Filter by date time (ISO 8601 Format) ")] = None,
        date__gt: Annotated[Optional[datetime], Field(description="Filter by date time greater than date time specified (ISO 8601 Format)")] = None,
        date__lt: Annotated[Optional[datetime], Field(description="Filter by date time less than date time specified (ISO 8601 Format)")] = None,
        machine_type_id: Annotated[Optional[List[StrictStr]], Field(description="Filter by machine type id.")] = None,
        material: Optional[StrictStr] = None,
        name: Annotated[Optional[StrictStr], Field(description="Filter by name of the print (Substring Match)")] = None,
        page: Annotated[Optional[StrictInt], Field(description="A page number within the paginated result set.")] = None,
        per_page: Annotated[Optional[StrictInt], Field(description="Number of results to return per page.")] = None,
        printer: Annotated[Optional[StrictStr], Field(description="Filter by printer serial")] = None,
        status: Annotated[Optional[StrictStr], Field(description="Filter by status of the print. Possible values are:                      * `QUEUED` - Queued               * `PREPRINT` - Preprint               * `PRINTING` - Printing             * `PAUSED` - Paused             * `FINISHED` - Finished             * `ABORTING` - Aborting             * `ABORTED` - Aborted             * `ERROR` - Error             * `WAITING_FOR_RESOLUTION` - Waiting for Resolution             * `PREHEAT` - Preheat             * `PRECOAT` - Precoat             * `POSTCOAT` - Postcoat")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> PaginatedPrintRunWithFleetControlDataList:
        """prints_list

        List of all prints from my printer. Please replace {printer_pk} field with your printer serial, Ex. SweetMatcha.

        :param var_date: Filter by date time (ISO 8601 Format) 
        :type var_date: datetime
        :param date__gt: Filter by date time greater than date time specified (ISO 8601 Format)
        :type date__gt: datetime
        :param date__lt: Filter by date time less than date time specified (ISO 8601 Format)
        :type date__lt: datetime
        :param machine_type_id: Filter by machine type id.
        :type machine_type_id: List[str]
        :param material:
        :type material: str
        :param name: Filter by name of the print (Substring Match)
        :type name: str
        :param page: A page number within the paginated result set.
        :type page: int
        :param per_page: Number of results to return per page.
        :type per_page: int
        :param printer: Filter by printer serial
        :type printer: str
        :param status: Filter by status of the print. Possible values are:                      * `QUEUED` - Queued               * `PREPRINT` - Preprint               * `PRINTING` - Printing             * `PAUSED` - Paused             * `FINISHED` - Finished             * `ABORTING` - Aborting             * `ABORTED` - Aborted             * `ERROR` - Error             * `WAITING_FOR_RESOLUTION` - Waiting for Resolution             * `PREHEAT` - Preheat             * `PRECOAT` - Precoat             * `POSTCOAT` - Postcoat
        :type status: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._prints_list_serialize(
            var_date=var_date,
            date__gt=date__gt,
            date__lt=date__lt,
            machine_type_id=machine_type_id,
            material=material,
            name=name,
            page=page,
            per_page=per_page,
            printer=printer,
            status=status,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedPrintRunWithFleetControlDataList",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def prints_list_with_http_info(
        self,
        var_date: Annotated[Optional[datetime], Field(description="Filter by date time (ISO 8601 Format) ")] = None,
        date__gt: Annotated[Optional[datetime], Field(description="Filter by date time greater than date time specified (ISO 8601 Format)")] = None,
        date__lt: Annotated[Optional[datetime], Field(description="Filter by date time less than date time specified (ISO 8601 Format)")] = None,
        machine_type_id: Annotated[Optional[List[StrictStr]], Field(description="Filter by machine type id.")] = None,
        material: Optional[StrictStr] = None,
        name: Annotated[Optional[StrictStr], Field(description="Filter by name of the print (Substring Match)")] = None,
        page: Annotated[Optional[StrictInt], Field(description="A page number within the paginated result set.")] = None,
        per_page: Annotated[Optional[StrictInt], Field(description="Number of results to return per page.")] = None,
        printer: Annotated[Optional[StrictStr], Field(description="Filter by printer serial")] = None,
        status: Annotated[Optional[StrictStr], Field(description="Filter by status of the print. Possible values are:                      * `QUEUED` - Queued               * `PREPRINT` - Preprint               * `PRINTING` - Printing             * `PAUSED` - Paused             * `FINISHED` - Finished             * `ABORTING` - Aborting             * `ABORTED` - Aborted             * `ERROR` - Error             * `WAITING_FOR_RESOLUTION` - Waiting for Resolution             * `PREHEAT` - Preheat             * `PRECOAT` - Precoat             * `POSTCOAT` - Postcoat")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[PaginatedPrintRunWithFleetControlDataList]:
        """prints_list

        List of all prints from my printer. Please replace {printer_pk} field with your printer serial, Ex. SweetMatcha.

        :param var_date: Filter by date time (ISO 8601 Format) 
        :type var_date: datetime
        :param date__gt: Filter by date time greater than date time specified (ISO 8601 Format)
        :type date__gt: datetime
        :param date__lt: Filter by date time less than date time specified (ISO 8601 Format)
        :type date__lt: datetime
        :param machine_type_id: Filter by machine type id.
        :type machine_type_id: List[str]
        :param material:
        :type material: str
        :param name: Filter by name of the print (Substring Match)
        :type name: str
        :param page: A page number within the paginated result set.
        :type page: int
        :param per_page: Number of results to return per page.
        :type per_page: int
        :param printer: Filter by printer serial
        :type printer: str
        :param status: Filter by status of the print. Possible values are:                      * `QUEUED` - Queued               * `PREPRINT` - Preprint               * `PRINTING` - Printing             * `PAUSED` - Paused             * `FINISHED` - Finished             * `ABORTING` - Aborting             * `ABORTED` - Aborted             * `ERROR` - Error             * `WAITING_FOR_RESOLUTION` - Waiting for Resolution             * `PREHEAT` - Preheat             * `PRECOAT` - Precoat             * `POSTCOAT` - Postcoat
        :type status: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._prints_list_serialize(
            var_date=var_date,
            date__gt=date__gt,
            date__lt=date__lt,
            machine_type_id=machine_type_id,
            material=material,
            name=name,
            page=page,
            per_page=per_page,
            printer=printer,
            status=status,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedPrintRunWithFleetControlDataList",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def prints_list_without_preload_content(
        self,
        var_date: Annotated[Optional[datetime], Field(description="Filter by date time (ISO 8601 Format) ")] = None,
        date__gt: Annotated[Optional[datetime], Field(description="Filter by date time greater than date time specified (ISO 8601 Format)")] = None,
        date__lt: Annotated[Optional[datetime], Field(description="Filter by date time less than date time specified (ISO 8601 Format)")] = None,
        machine_type_id: Annotated[Optional[List[StrictStr]], Field(description="Filter by machine type id.")] = None,
        material: Optional[StrictStr] = None,
        name: Annotated[Optional[StrictStr], Field(description="Filter by name of the print (Substring Match)")] = None,
        page: Annotated[Optional[StrictInt], Field(description="A page number within the paginated result set.")] = None,
        per_page: Annotated[Optional[StrictInt], Field(description="Number of results to return per page.")] = None,
        printer: Annotated[Optional[StrictStr], Field(description="Filter by printer serial")] = None,
        status: Annotated[Optional[StrictStr], Field(description="Filter by status of the print. Possible values are:                      * `QUEUED` - Queued               * `PREPRINT` - Preprint               * `PRINTING` - Printing             * `PAUSED` - Paused             * `FINISHED` - Finished             * `ABORTING` - Aborting             * `ABORTED` - Aborted             * `ERROR` - Error             * `WAITING_FOR_RESOLUTION` - Waiting for Resolution             * `PREHEAT` - Preheat             * `PRECOAT` - Precoat             * `POSTCOAT` - Postcoat")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """prints_list

        List of all prints from my printer. Please replace {printer_pk} field with your printer serial, Ex. SweetMatcha.

        :param var_date: Filter by date time (ISO 8601 Format) 
        :type var_date: datetime
        :param date__gt: Filter by date time greater than date time specified (ISO 8601 Format)
        :type date__gt: datetime
        :param date__lt: Filter by date time less than date time specified (ISO 8601 Format)
        :type date__lt: datetime
        :param machine_type_id: Filter by machine type id.
        :type machine_type_id: List[str]
        :param material:
        :type material: str
        :param name: Filter by name of the print (Substring Match)
        :type name: str
        :param page: A page number within the paginated result set.
        :type page: int
        :param per_page: Number of results to return per page.
        :type per_page: int
        :param printer: Filter by printer serial
        :type printer: str
        :param status: Filter by status of the print. Possible values are:                      * `QUEUED` - Queued               * `PREPRINT` - Preprint               * `PRINTING` - Printing             * `PAUSED` - Paused             * `FINISHED` - Finished             * `ABORTING` - Aborting             * `ABORTED` - Aborted             * `ERROR` - Error             * `WAITING_FOR_RESOLUTION` - Waiting for Resolution             * `PREHEAT` - Preheat             * `PRECOAT` - Precoat             * `POSTCOAT` - Postcoat
        :type status: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._prints_list_serialize(
            var_date=var_date,
            date__gt=date__gt,
            date__lt=date__lt,
            machine_type_id=machine_type_id,
            material=material,
            name=name,
            page=page,
            per_page=per_page,
            printer=printer,
            status=status,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PaginatedPrintRunWithFleetControlDataList",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _prints_list_serialize(
        self,
        var_date,
        date__gt,
        date__lt,
        machine_type_id,
        material,
        name,
        page,
        per_page,
        printer,
        status,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'machine_type_id': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if var_date is not None:
            if isinstance(var_date, datetime):
                _query_params.append(
                    (
                        'date',
                        var_date.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('date', var_date))
            
        if date__gt is not None:
            if isinstance(date__gt, datetime):
                _query_params.append(
                    (
                        'date__gt',
                        date__gt.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('date__gt', date__gt))
            
        if date__lt is not None:
            if isinstance(date__lt, datetime):
                _query_params.append(
                    (
                        'date__lt',
                        date__lt.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('date__lt', date__lt))
            
        if machine_type_id is not None:
            
            _query_params.append(('machine_type_id', machine_type_id))
            
        if material is not None:
            
            _query_params.append(('material', material))
            
        if name is not None:
            
            _query_params.append(('name', name))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if per_page is not None:
            
            _query_params.append(('per_page', per_page))
            
        if printer is not None:
            
            _query_params.append(('printer', printer))
            
        if status is not None:
            
            _query_params.append(('status', status))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'bearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/developer/v1/prints/',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


