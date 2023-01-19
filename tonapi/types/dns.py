from pydantic import BaseModel

from .blockchain import AccountAddress


class DomainNames(BaseModel):
    domains: list[str]


class NftItem(BaseModel):
    address: str
    owner: AccountAddress


class DomainInfo(BaseModel):
    expiration: int
    nft_item: None | NftItem


class WalletDNS(BaseModel):
    address: str
    has_method_pubkey: bool
    has_method_seqno: bool
    is_wallet: bool
    names: list[str]


class DnsRecord(BaseModel):
    next_resolver: None | str
    site: list[str]
    wallet: None | WalletDNS
