from pydantic import BaseModel

from .blockchain import AccountAddress


class Auction(BaseModel):
    bids: int
    date: int
    domain: str
    owner: str
    price: int


class Auctions(BaseModel):
    data: list[Auction]
    total: int


class DomainBid(BaseModel):
    bidder: AccountAddress
    success: bool
    txHash: str
    txTime: int
    value: int


class DomainBids(BaseModel):
    data: list[DomainBid]
