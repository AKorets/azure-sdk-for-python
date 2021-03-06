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

from msrest.serialization import Model


class RoleAssignmentCreateParameters(Model):
    """Role assignment create parameters.

    :param role_definition_id: The role definition ID used in the role
     assignment.
    :type role_definition_id: str
    :param principal_id: The principal ID assigned to the role. This maps to
     the ID inside the Active Directory. It can point to a user, service
     principal, or security group.
    :type principal_id: str
    :param can_delegate: The delgation flag used for creating a role
     assignment
    :type can_delegate: bool
    """

    _attribute_map = {
        'role_definition_id': {'key': 'properties.roleDefinitionId', 'type': 'str'},
        'principal_id': {'key': 'properties.principalId', 'type': 'str'},
        'can_delegate': {'key': 'properties.canDelegate', 'type': 'bool'},
    }

    def __init__(self, *, role_definition_id: str=None, principal_id: str=None, can_delegate: bool=None, **kwargs) -> None:
        super(RoleAssignmentCreateParameters, self).__init__(**kwargs)
        self.role_definition_id = role_definition_id
        self.principal_id = principal_id
        self.can_delegate = can_delegate
