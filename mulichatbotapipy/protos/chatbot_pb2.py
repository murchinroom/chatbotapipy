# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: muvtuber/chatbot/v2/chatbot.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!muvtuber/chatbot/v2/chatbot.proto\x12\x13muvtuber.chatbot.v2\"R\n\x11NewSessionRequest\x12\x16\n\x06\x63onfig\x18\x01 \x01(\tR\x06\x63onfig\x12%\n\x0einitial_prompt\x18\x02 \x01(\tR\rinitialPrompt\"^\n\x12NewSessionResponse\x12\x1d\n\nsession_id\x18\x01 \x01(\tR\tsessionId\x12)\n\x10initial_response\x18\x02 \x01(\tR\x0finitialResponse\"5\n\x14\x44\x65leteSessionRequest\x12\x1d\n\nsession_id\x18\x01 \x01(\tR\tsessionId\"6\n\x15\x44\x65leteSessionResponse\x12\x1d\n\nsession_id\x18\x01 \x01(\tR\tsessionId\"D\n\x0b\x43hatRequest\x12\x1d\n\nsession_id\x18\x01 \x01(\tR\tsessionId\x12\x16\n\x06prompt\x18\x02 \x01(\tR\x06prompt\"*\n\x0c\x43hatResponse\x12\x1a\n\x08response\x18\x02 \x01(\tR\x08response2\xa4\x02\n\x0e\x43hatbotService\x12]\n\nNewSession\x12&.muvtuber.chatbot.v2.NewSessionRequest\x1a\'.muvtuber.chatbot.v2.NewSessionResponse\x12K\n\x04\x43hat\x12 .muvtuber.chatbot.v2.ChatRequest\x1a!.muvtuber.chatbot.v2.ChatResponse\x12\x66\n\rDeleteSession\x12).muvtuber.chatbot.v2.DeleteSessionRequest\x1a*.muvtuber.chatbot.v2.DeleteSessionResponseB\xc7\x01\n\x17\x63om.muvtuber.chatbot.v2B\x0c\x43hatbotProtoP\x01Z0muvtuberdriver/gen/muvtuber/chatbot/v2;chatbotv2\xa2\x02\x03MCX\xaa\x02\x13Muvtuber.Chatbot.V2\xca\x02\x13Muvtuber\\Chatbot\\V2\xe2\x02\x1fMuvtuber\\Chatbot\\V2\\GPBMetadata\xea\x02\x15Muvtuber::Chatbot::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'muvtuber.chatbot.v2.chatbot_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.muvtuber.chatbot.v2B\014ChatbotProtoP\001Z0muvtuberdriver/gen/muvtuber/chatbot/v2;chatbotv2\242\002\003MCX\252\002\023Muvtuber.Chatbot.V2\312\002\023Muvtuber\\Chatbot\\V2\342\002\037Muvtuber\\Chatbot\\V2\\GPBMetadata\352\002\025Muvtuber::Chatbot::V2'
  _globals['_NEWSESSIONREQUEST']._serialized_start=58
  _globals['_NEWSESSIONREQUEST']._serialized_end=140
  _globals['_NEWSESSIONRESPONSE']._serialized_start=142
  _globals['_NEWSESSIONRESPONSE']._serialized_end=236
  _globals['_DELETESESSIONREQUEST']._serialized_start=238
  _globals['_DELETESESSIONREQUEST']._serialized_end=291
  _globals['_DELETESESSIONRESPONSE']._serialized_start=293
  _globals['_DELETESESSIONRESPONSE']._serialized_end=347
  _globals['_CHATREQUEST']._serialized_start=349
  _globals['_CHATREQUEST']._serialized_end=417
  _globals['_CHATRESPONSE']._serialized_start=419
  _globals['_CHATRESPONSE']._serialized_end=461
  _globals['_CHATBOTSERVICE']._serialized_start=464
  _globals['_CHATBOTSERVICE']._serialized_end=756
# @@protoc_insertion_point(module_scope)
