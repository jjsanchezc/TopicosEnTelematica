from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteProductFromCart(_message.Message):
    __slots__ = ["id_product", "reason"]
    ID_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    id_product: int
    reason: str
    def __init__(self, id_product: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...

class ProductAdditionToCart(_message.Message):
    __slots__ = ["id_product"]
    ID_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    id_product: int
    def __init__(self, id_product: _Optional[int] = ...) -> None: ...

class ProductAdditionToCartResponse(_message.Message):
    __slots__ = ["status_code"]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    status_code: int
    def __init__(self, status_code: _Optional[int] = ...) -> None: ...

class ProductDeletedInCartResponse(_message.Message):
    __slots__ = ["id_product", "product_quantity_left", "status_code"]
    ID_PRODUCT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_QUANTITY_LEFT_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    id_product: int
    product_quantity_left: int
    status_code: bool
    def __init__(self, status_code: bool = ..., id_product: _Optional[int] = ..., product_quantity_left: _Optional[int] = ...) -> None: ...
