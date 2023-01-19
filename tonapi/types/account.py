from pydantic import BaseModel


class Address(BaseModel):
    bounceable: str
    non_bounceable: str
    raw: str


class AccountRepr(BaseModel):
    address: Address
    balance: int
    interfaces: list[str]
    is_scam: bool
    last_update: int
    memo_required: bool
    status: str
    icon: None | str = None
    name: None | str = None


class AccountReprs(BaseModel):
    account: list[AccountRepr]
