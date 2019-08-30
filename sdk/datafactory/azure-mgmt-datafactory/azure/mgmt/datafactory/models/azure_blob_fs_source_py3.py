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

from .copy_source_py3 import CopySource


class AzureBlobFSSource(CopySource):
    """A copy activity Azure BlobFS source.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param source_retry_count: Source retry count. Type: integer (or
     Expression with resultType integer).
    :type source_retry_count: object
    :param source_retry_wait: Source retry wait. Type: string (or Expression
     with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type source_retry_wait: object
    :param max_concurrent_connections: The maximum concurrent connection count
     for the source data store. Type: integer (or Expression with resultType
     integer).
    :type max_concurrent_connections: object
    :param type: Required. Constant filled by server.
    :type type: str
    :param treat_empty_as_null: Treat empty as null. Type: boolean (or
     Expression with resultType boolean).
    :type treat_empty_as_null: object
    :param skip_header_line_count: Number of header lines to skip from each
     blob. Type: integer (or Expression with resultType integer).
    :type skip_header_line_count: object
    :param recursive: If true, files under the folder path will be read
     recursively. Default is true. Type: boolean (or Expression with resultType
     boolean).
    :type recursive: object
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'source_retry_count': {'key': 'sourceRetryCount', 'type': 'object'},
        'source_retry_wait': {'key': 'sourceRetryWait', 'type': 'object'},
        'max_concurrent_connections': {'key': 'maxConcurrentConnections', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
        'treat_empty_as_null': {'key': 'treatEmptyAsNull', 'type': 'object'},
        'skip_header_line_count': {'key': 'skipHeaderLineCount', 'type': 'object'},
        'recursive': {'key': 'recursive', 'type': 'object'},
    }

    def __init__(self, *, additional_properties=None, source_retry_count=None, source_retry_wait=None, max_concurrent_connections=None, treat_empty_as_null=None, skip_header_line_count=None, recursive=None, **kwargs) -> None:
        super(AzureBlobFSSource, self).__init__(additional_properties=additional_properties, source_retry_count=source_retry_count, source_retry_wait=source_retry_wait, max_concurrent_connections=max_concurrent_connections, **kwargs)
        self.treat_empty_as_null = treat_empty_as_null
        self.skip_header_line_count = skip_header_line_count
        self.recursive = recursive
        self.type = 'AzureBlobFSSource'
