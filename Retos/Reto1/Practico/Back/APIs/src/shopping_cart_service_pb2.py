# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: shopping_cart_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bshopping_cart_service.proto\"+\n\x15ProductAdditionToCart\x12\x12\n\nid_product\x18\x01 \x01(\x05\"4\n\x1dProductAdditionToCartResponse\x12\x13\n\x0bstatus_code\x18\x01 \x01(\x05\x32X\n\x0eProductService\x12\x46\n\nAddProduct\x12\x16.ProductAdditionToCart\x1a\x1e.ProductAdditionToCartResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'shopping_cart_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PRODUCTADDITIONTOCART._serialized_start=31
  _PRODUCTADDITIONTOCART._serialized_end=74
  _PRODUCTADDITIONTOCARTRESPONSE._serialized_start=76
  _PRODUCTADDITIONTOCARTRESPONSE._serialized_end=128
  _PRODUCTSERVICE._serialized_start=130
  _PRODUCTSERVICE._serialized_end=218
# @@protoc_insertion_point(module_scope)
