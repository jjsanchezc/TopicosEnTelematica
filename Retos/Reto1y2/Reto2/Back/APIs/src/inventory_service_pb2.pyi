from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProductAvailabilityResponse(_message.Message):
    __slots__ = ["status_code"]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    status_code: bool
    def __init__(self, status_code: bool = ...) -> None: ...

class ProductToSearch(_message.Message):
    __slots__ = ["id_product"]
    ID_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    id_product: int
    def __init__(self, id_product: _Optional[int] = ...) -> None: ...
