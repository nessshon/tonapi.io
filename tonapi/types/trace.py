from __future__ import annotations

from pydantic import BaseModel

from .blockchain import AccountAddress


class TXAnnotation(BaseModel):
    data: dict
    name: str


class TraceTX(BaseModel):
    annotations: list[TXAnnotation]
    block_id: str
    fee: int
    hash: str
    lt: int
    other_fee: int
    out_msgs: list[TraceMsg]
    storage_fee: int
    utime: int


class TraceMsg(BaseModel):
    created_lt: int
    destination: AccountAddress
    fwd_fee: int
    ihr_fee: int
    source: AccountAddress
    value: int
    comment: None | str
    tx: None | TraceTX


class AnnotatedTraceMsg(BaseModel):
    account: AccountAddress
    annotations: None | list[TXAnnotation]
    children: list[AnnotatedTraceMsg]
    fee: int
    hash: str
    input_value: int
    interfaces: list[str]
    lt: int
    other_fee: int
    storage_fee: int
    success: bool
