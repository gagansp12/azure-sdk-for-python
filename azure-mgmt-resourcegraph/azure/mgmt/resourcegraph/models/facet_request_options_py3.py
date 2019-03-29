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


class FacetRequestOptions(Model):
    """The options for facet evaluation.

    :param sort_by: The column name or query expression to sort on. Defaults
     to count if not present.
    :type sort_by: str
    :param sort_order: The sorting order by the selected column (count by
     default). Possible values include: 'asc', 'desc'. Default value: "desc" .
    :type sort_order: str or ~azure.mgmt.resourcegraph.models.FacetSortOrder
    :param filter: Specifies the filter condition for the 'where' clause which
     will be run on main query's result, just before the actual faceting.
    :type filter: str
    :param top: The maximum number of facet rows that should be returned.
    :type top: int
    """

    _validation = {
        'top': {'maximum': 1000, 'minimum': 1},
    }

    _attribute_map = {
        'sort_by': {'key': 'sortBy', 'type': 'str'},
        'sort_order': {'key': 'sortOrder', 'type': 'FacetSortOrder'},
        'filter': {'key': 'filter', 'type': 'str'},
        'top': {'key': '$top', 'type': 'int'},
    }

    def __init__(self, *, sort_by: str=None, sort_order="desc", filter: str=None, top: int=None, **kwargs) -> None:
        super(FacetRequestOptions, self).__init__(**kwargs)
        self.sort_by = sort_by
        self.sort_order = sort_order
        self.filter = filter
        self.top = top
