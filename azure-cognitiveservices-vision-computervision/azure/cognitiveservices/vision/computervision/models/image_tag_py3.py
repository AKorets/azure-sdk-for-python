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


class ImageTag(Model):
    """An image caption, i.e. a brief description of what the image depicts.

    :param name: The tag value
    :type name: str
    :param confidence: The level of confidence the service has in the caption
    :type confidence: float
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'confidence': {'key': 'confidence', 'type': 'float'},
    }

    def __init__(self, *, name: str=None, confidence: float=None, **kwargs) -> None:
        super(ImageTag, self).__init__(**kwargs)
        self.name = name
        self.confidence = confidence
