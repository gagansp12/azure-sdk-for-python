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

from .proxy_resource import ProxyResource


class BackupLongTermRetentionPolicy(ProxyResource):
    """A backup long term retention policy.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar location: The geo-location where the resource lives
    :vartype location: str
    :param state: The status of the backup long term retention policy.
     Possible values include: 'Disabled', 'Enabled'
    :type state: str or :class:`BackupLongTermRetentionPolicyState
     <azure.mgmt.sql.models.BackupLongTermRetentionPolicyState>`
    :param recovery_services_backup_policy_resource_id: The azure recovery
     services backup protection policy resource id
    :type recovery_services_backup_policy_resource_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'readonly': True},
        'state': {'required': True},
        'recovery_services_backup_policy_resource_id': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'BackupLongTermRetentionPolicyState'},
        'recovery_services_backup_policy_resource_id': {'key': 'properties.recoveryServicesBackupPolicyResourceId', 'type': 'str'},
    }

    def __init__(self, state, recovery_services_backup_policy_resource_id):
        super(BackupLongTermRetentionPolicy, self).__init__()
        self.location = None
        self.state = state
        self.recovery_services_backup_policy_resource_id = recovery_services_backup_policy_resource_id
