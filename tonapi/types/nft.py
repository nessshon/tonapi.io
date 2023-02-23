from pydantic import BaseModel

from . import address
from .blockchain import AccountAddress


class Collection(BaseModel):
    address: address
    name: str


class NftCollection(BaseModel):
    address: address
    metadata: None | dict
    next_item_index: int
    owner: None | AccountAddress
    raw_collection_content: str


class NftCollections(BaseModel):
    nft_collections: list[NftCollection]


class Price(BaseModel):
    token_name: str
    value: str


class Sale(BaseModel):
    address: address
    market: AccountAddress
    owner: None | AccountAddress
    price: Price


class ImagePreview(BaseModel):
    resolution: None | str
    url: None | str


class NftItemRepr(BaseModel):
    address: address
    approved_by: None | list[str]
    collection: None | Collection
    dns: None | str
    index: int
    metadata: dict
    owner: None | AccountAddress
    previews: None | ImagePreview
    sale: None | Sale
    verified: bool


class NftItemsRepr(BaseModel):
    nft_items: list[NftItemRepr]
