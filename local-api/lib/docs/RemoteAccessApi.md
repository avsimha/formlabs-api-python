# formlabs_local_api.RemoteAccessApi

All URIs are relative to *http://localhost:44388*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_print_0**](RemoteAccessApi.md#call_print_0) | **POST** /scene/print/ | Print
[**discover_devices_0**](RemoteAccessApi.md#discover_devices_0) | **POST** /discover-devices/ | Discover Devices
[**get_device_0**](RemoteAccessApi.md#get_device_0) | **GET** /devices/{id}/ | Get Device
[**get_devices_0**](RemoteAccessApi.md#get_devices_0) | **GET** /devices/ | Get Devices
[**login**](RemoteAccessApi.md#login) | **POST** /login/ | Login


# **call_print_0**
> Print200Response call_print_0(print_request, var_async=var_async)

Print

Upload the current scene to a printer or Fleet Control.  By default, only locally discovered printer names or local IP addresses are supported. To upload prints remotely to your Fleet Control queue or printers registered to your Dashboard account, you must be logged in and have an Internet connection. Use the Login endpoint to authenticate with Formlabs Web Services. 

### Example


```python
import formlabs_local_api
from formlabs_local_api.models.print200_response import Print200Response
from formlabs_local_api.models.print_request import PrintRequest
from formlabs_local_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs_local_api.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with formlabs_local_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs_local_api.RemoteAccessApi(api_client)
    print_request = {"printer":"10.35.15.12","job_name":"Test Job"} # PrintRequest | 
    var_async = True # bool | Whether to run the operation asynchronously (optional)

    try:
        # Print
        api_response = api_instance.call_print_0(print_request, var_async=var_async)
        print("The response of RemoteAccessApi->call_print_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteAccessApi->call_print_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **print_request** | [**PrintRequest**](PrintRequest.md)|  | 
 **var_async** | **bool**| Whether to run the operation asynchronously | [optional] 

### Return type

[**Print200Response**](Print200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_devices_0**
> DiscoverDevices200Response discover_devices_0(discover_devices_request)

Discover Devices

Discover new devices on the network

### Example


```python
import formlabs_local_api
from formlabs_local_api.models.discover_devices200_response import DiscoverDevices200Response
from formlabs_local_api.models.discover_devices_request import DiscoverDevicesRequest
from formlabs_local_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs_local_api.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with formlabs_local_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs_local_api.RemoteAccessApi(api_client)
    discover_devices_request = {"timeout_seconds":10} # DiscoverDevicesRequest | 

    try:
        # Discover Devices
        api_response = api_instance.discover_devices_0(discover_devices_request)
        print("The response of RemoteAccessApi->discover_devices_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteAccessApi->discover_devices_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **discover_devices_request** | [**DiscoverDevicesRequest**](DiscoverDevicesRequest.md)|  | 

### Return type

[**DiscoverDevices200Response**](DiscoverDevices200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_0**
> DeviceStatusModel get_device_0(id)

Get Device

Get a previously discovered device's status

### Example


```python
import formlabs_local_api
from formlabs_local_api.models.device_status_model import DeviceStatusModel
from formlabs_local_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs_local_api.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with formlabs_local_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs_local_api.RemoteAccessApi(api_client)
    id = 'id_example' # str | The unique identifier of the printer

    try:
        # Get Device
        api_response = api_instance.get_device_0(id)
        print("The response of RemoteAccessApi->get_device_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteAccessApi->get_device_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier of the printer | 

### Return type

[**DeviceStatusModel**](DeviceStatusModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_0**
> GetDevices200Response get_devices_0()

Get Devices

List of previously discovered device statuses  By default, only locally discovered printer names are returned. To include your Fleet Control queues or printers registered to your Dashboard account, you must be logged in and have an Internet connection. Use the Login endpoint to authenticate with Formlabs Web Services. 

### Example


```python
import formlabs_local_api
from formlabs_local_api.models.get_devices200_response import GetDevices200Response
from formlabs_local_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs_local_api.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with formlabs_local_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs_local_api.RemoteAccessApi(api_client)

    try:
        # Get Devices
        api_response = api_instance.get_devices_0()
        print("The response of RemoteAccessApi->get_devices_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteAccessApi->get_devices_0: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetDevices200Response**](GetDevices200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> WebAuthTokensModel login(login_request)

Login

Log in to Formlabs Web Services using an existing formlabs.com account.

### Example


```python
import formlabs_local_api
from formlabs_local_api.models.login_request import LoginRequest
from formlabs_local_api.models.web_auth_tokens_model import WebAuthTokensModel
from formlabs_local_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:44388
# See configuration.py for a list of all supported configuration parameters.
configuration = formlabs_local_api.Configuration(
    host = "http://localhost:44388"
)


# Enter a context with an instance of the API client
with formlabs_local_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = formlabs_local_api.RemoteAccessApi(api_client)
    login_request = {"username":"username","password":"password"} # LoginRequest | User credentials

    try:
        # Login
        api_response = api_instance.login(login_request)
        print("The response of RemoteAccessApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteAccessApi->login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)| User credentials | 

### Return type

[**WebAuthTokensModel**](WebAuthTokensModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

