from pydantic import BaseModel

from . import address, msg_data


class Account(BaseModel):
    balance: int
    code: None | int
    data: None | int
    status: int


class Block(BaseModel):
    end_lt: int
    file_hash: str
    root_hash: str
    seqno: int
    shard: str
    start_lt: int
    workchain_id: int


class AccountAddress(BaseModel):
    address: address
    icon: None | str
    is_scam: bool
    name: None | str


class Message(BaseModel):
    created_lt: int
    destination: None | AccountAddress
    fwd_fee: int
    ihr_fee: int
    msg_data: msg_data
    source: None | AccountAddress
    value: int


class Transaction(BaseModel):
    account: AccountAddress
    data: str
    fee: int
    hash: str
    in_msg: None | Message
    lt: int
    other_fee: int
    out_msgs: list[Message]
    storage_fee: int
    utime: int


class Transactions(BaseModel):
    transactions: list[Transaction]


class Validator(BaseModel):
    address: address
    adnlAddress: str
    maxFactor: int
    stake: int


class Validators(BaseModel):
    electAt: int
    electClose: int
    minStake: int
    totalStake: int
    electAt: list[Validator]
