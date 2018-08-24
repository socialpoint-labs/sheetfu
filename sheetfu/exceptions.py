# -*- coding: utf-8 -*-


class SizeNotMatchingException(Exception):
    """The size of the values submitted array does not match the Range coordinates. Make sure sizes are matching"""
    pass


class SheetNameNoMatchError(Exception):
    """There is no sheet name with this name"""
    pass


class SheetIdNoMatchError(Exception):
    """There is no sheet ID matching"""
    pass


class NoDataRangeError(Exception):
    """No data found in target sheet."""
    pass
