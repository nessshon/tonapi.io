from __future__ import annotations

from pydantic import BaseModel

from .blockchain import AccountAddress


class TXAnnotation(BaseModel):
    data: dict
    name: str


class TraceTX(BaseModel):
    annotations: None | list[TXAnnotation]
    block_id: str
    fee: int
    hash: str
    lt: int
    other_fee: int
    out_msgs: None | list[TraceMsg]
    storage_fee: int
    utime: int

    def __init__(self, **kwargs):
        self.update_forward_refs()
        super().__init__(**kwargs)


class TraceMsg(BaseModel):
    comment: None | str
    created_lt: int
    destination: AccountAddress
    fwd_fee: int
    ihr_fee: int
    source: AccountAddress
    tx: None | TraceTX
    value: int


class AnnotatedTraceMsg(BaseModel):
    account: AccountAddress
    annotations: None | list[TXAnnotation]
    children: None | list[AnnotatedTraceMsg]
    fee: int
    hash: str
    input_value: int
    interfaces: list[str]
    lt: int
    other_fee: int
    storage_fee: int
    success: bool
