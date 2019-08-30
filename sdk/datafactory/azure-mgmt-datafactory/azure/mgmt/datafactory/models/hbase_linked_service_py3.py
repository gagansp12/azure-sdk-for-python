# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .linked_service_py3 import LinkedService


class HBaseLinkedService(LinkedService):
    """HBase server linked service.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param parameters: Parameters for linked service.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param annotations: List of tags that can be used for describing the
     linked service.
    :type annotations: list[object]
    :param type: Required. Constant filled by server.
    :type type: str
    :param host: Required. The IP address or host name of the HBase server.
     (i.e. 192.168.222.160)
    :type host: object
    :param port: The TCP port that the HBase instance uses to listen for
     client connections. The default value is 9090.
    :type port: object
    :param http_path: The partial URL corresponding to the HBase server. (i.e.
     /gateway/sandbox/hbase/version)
    :type http_path: object
    :param authentication_type: Required. The authentication mechanism to use
     to connect to the HBase server. Possible values include: 'Anonymous',
     'Basic'
    :type authentication_type: str or
     ~azure.mgmt.datafactory.models.HBaseAuthenticationType
    :param username: The user name used to connect to the HBase instance.
    :type username: object
    :param password: The password corresponding to the user name.
    :type password: ~azure.mgmt.datafactory.models.SecretBase
    :param enable_ssl: Specifies whether the connections to the server are
     encrypted using SSL. The default value is false.
    :type enable_ssl: object
    :param trusted_cert_path: The full path of the .pem file containing
     trusted CA certificates for verifying the server when connecting over SSL.
     This property can only be set when using SSL on self-hosted IR. The
     default value is the cacerts.pem file installed with the IR.
    :type trusted_cert_path: object
    :param allow_host_name_cn_mismatch: Specifies whether to require a
     CA-issued SSL certificate name to match the host name of the server when
     connecting over SSL. The default value is false.
    :type allow_host_name_cn_mismatch: object
    :param allow_self_signed_server_cert: Specifies whether to allow
     self-signed certificates from the server. The default value is false.
    :type allow_self_signed_server_cert: object
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    """

    _validation = {
        'type': {'required': True},
        'host': {'required': True},
        'authentication_type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'type': {'key': 'type', 'type': 'str'},
        'host': {'key': 'typeProperties.host', 'type': 'object'},
        'port': {'key': 'typeProperties.port', 'type': 'object'},
        'http_path': {'key': 'typeProperties.httpPath', 'type': 'object'},
        'authentication_type': {'key': 'typeProperties.authenticationType', 'type': 'str'},
        'username': {'key': 'typeProperties.username', 'type': 'object'},
        'password': {'key': 'typeProperties.password', 'type': 'SecretBase'},
        'enable_ssl': {'key': 'typeProperties.enableSsl', 'type': 'object'},
        'trusted_cert_path': {'key': 'typeProperties.trustedCertPath', 'type': 'object'},
        'allow_host_name_cn_mismatch': {'key': 'typeProperties.allowHostNameCNMismatch', 'type': 'object'},
        'allow_self_signed_server_cert': {'key': 'typeProperties.allowSelfSignedServerCert', 'type': 'object'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
    }

    def __init__(self, *, host, authentication_type, additional_properties=None, connect_via=None, description: str=None, parameters=None, annotations=None, port=None, http_path=None, username=None, password=None, enable_ssl=None, trusted_cert_path=None, allow_host_name_cn_mismatch=None, allow_self_signed_server_cert=None, encrypted_credential=None, **kwargs) -> None:
        super(HBaseLinkedService, self).__init__(additional_properties=additional_properties, connect_via=connect_via, description=description, parameters=parameters, annotations=annotations, **kwargs)
        self.host = host
        self.port = port
        self.http_path = http_path
        self.authentication_type = authentication_type
        self.username = username
        self.password = password
        self.enable_ssl = enable_ssl
        self.trusted_cert_path = trusted_cert_path
        self.allow_host_name_cn_mismatch = allow_host_name_cn_mismatch
        self.allow_self_signed_server_cert = allow_self_signed_server_cert
        self.encrypted_credential = encrypted_credential
        self.type = 'HBase'
