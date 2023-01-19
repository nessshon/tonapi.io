from pydantic import BaseModel

from . import address
from .blockchain import AccountAddress


class Jetton(BaseModel):
    address: address
    decimals: str
    image: None | str
    name: str
    symbol: str
    verification: None | str


class JettonBalance(BaseModel):
    balance: str
    jetton_address: address
    metadata: Jetton
    verification: str
    wallet_address: AccountAddress


class JettonsBalances(BaseModel):
    balances: list[JettonBalance]


class JettonMetadata(BaseModel):
    address: address
    catalogs: None | list[str]
    decimals: int
    description: None | str
    image: None | str
    name: str
    social: None | list[str]
    symbol: str
    websites: None | list[str]


class JettonInfo(BaseModel):
    metadata: JettonMetadata
    mintable: bool
    total_supply: str
    verification: str
