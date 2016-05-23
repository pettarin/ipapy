#!/usr/bin/env python
# coding=utf-8

"""
ipapy contains data and functions to work with IPA strings.
"""

from __future__ import absolute_import
from __future__ import print_function

from ipapy.compatibility import is_unicode_string

__author__ = "Alberto Pettarin"
__copyright__ = "Copyright 2016, Alberto Pettarin (www.albertopettarin.it)"
__license__ = "MIT"
__email__ = "alberto@albertopettarin.it"

class IPADescriptor(object):
    """
    An IPA descriptor is a label associated with an IPA character.

    The first label in the list is assumed to be the canonical label.

    :param list labels: list of labels, each being a (Unicode) string
    """
    
    TAG = u"IPADescriptor"
    
    def __init__(self, labels):
        if not isinstance(labels, list):
            raise TypeError("Parameter labels must be a list of Unicode strings")
        if len(labels) < 1:
            raise ValueError("Parameter labels must contain at least one string")
        for l in labels:
            if not is_unicode_string(l):
                raise TypeError("Parameter labels must be a list of Unicode strings")
        self.__labels = labels

    def __len__(self):
        return len(self.labels)

    def __str__(self):
        return " ".join(self.labels)

    def __unicode__(self):
        return u" ".join(self.labels)

    def __contains__(self, other):
        return other in self.labels

    @property
    def canonical_label(self):
        """
        Return the canonical label for this descriptor.

        :rtype: str
        """
        return self.__labels[0]

    @canonical_label.setter
    def canonical_label(self, value):
        raise ValueError("The canonical_label field is read-only.")

    @property
    def labels(self):
        """
        Return all the labels for this descriptor,
        the first being the canonical label.

        :rtype: list of str
        """
        return self.__labels

    @labels.setter
    def labels(self, value):
        raise ValueError("The labels field is read-only.")



class IPADescriptorGroup(object):
    """
    An IPA descriptor group is a list of descriptors,
    for example different values for the same property,
    like "rounded" and "unrounded" for the vowel roundness.

    :param list descriptors: list of IPADescriptor objects
    """
    
    TAG = u"IPADescriptorGroup"
    
    def __init__(self, descriptors):
        if not isinstance(descriptors, list):
            raise TypeError("Parameter descriptors must be a list of IPADescriptor objects")
        if len(descriptors) < 1:
            raise ValueError("Parameter descriptors must contain at least one descriptor")
        for d in descriptors:
            if not isinstance(d, IPADescriptor):
                raise TypeError("Parameter descriptors must be a list of IPADescriptor objects")
        self.__descriptors = descriptors

    def __len__(self):
        return len(self.descriptors)

    def __str__(self):
        return "\n".join([d.__str__() for d in self.descriptors])

    def __unicode__(self):
        return u"\n".join([d.__unicode__() for d in self.descriptors])

    def __contains__(self, value):
        if isinstance(value, IPADescriptor):
            return value in self.descriptors
        return self.canonical_value(value) is not None

    def __add__(self, other):
        if not isinstance(other, IPADescriptorGroup):
            raise TypeError("Cannot concatenate an object that is not an IPADescriptorGroup")
        return IPADescriptorGroup(descriptors=self.descriptors + other.descriptors)

    @property
    def descriptors(self):
        """
        Return all the descriptors in this group.

        :rtype: list of IPADescriptor objects
        """
        return self.__descriptors

    @descriptors.setter
    def descriptors(self, value):
        raise ValueError("The descriptors field is read-only.")

    def canonical_value(self, query):
        """
        Return the canonical value corresponding to the given query value.

        Return ``None`` if the query value is not present in any descriptor of the group.

        :param str query: the descriptor value to be checked against
        """
        for d in self.descriptors:
            if query in d:
                return d.canonical_label
        return None



