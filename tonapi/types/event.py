from pydantic import BaseModel

from .blockchain import AccountAddress
from .jetton import Jetton
from .nft import Price, NftItemRepr


class Fee(BaseModel):
    account: AccountAddress
    deposit: int
    gas: int
    refund: int
    rent: int
    total: int


class ActionSimplePreview(BaseModel):
    full_description: str
    image: None | str
    name: str
    short_description: str


class UnSubscriptionAction(BaseModel):
    beneficiary: AccountAddress
    subscriber: AccountAddress
    subscription: str


class Refund(BaseModel):
    origin: str
    type: str


class TonTransferAction(BaseModel):
    amount: int
    comment: None | str
    payload: str
    recipient: AccountAddress
    refund: None | Refund
    sender: AccountAddress


class SubscriptionAction(BaseModel):
    amount: int
    beneficiary: AccountAddress
    initial: bool
    subscriber: AccountAddress
    amount: str


class NftPurchase(BaseModel):
    amount: Price
    buyer: AccountAddress
    nft: NftItemRepr
    purchase_type: str
    seller: AccountAddress


class NftItemTransferAction(BaseModel):
    comment: None | str
    nft: str
    payload: None | str
    recipient: None | AccountAddress
    refund: None | Refund
    sender: None | AccountAddress


class JettonTransferAction(BaseModel):
    amount: str
    comment: None | str
    jetton: Jetton
    recipient: None | AccountAddress
    recipients_wallet: str
    refund: None | Refund
    sender: None | AccountAddress
    senders_wallet: str


class ContractDeployAction(BaseModel):
    address: str
    deployer: AccountAddress
    interfaces: list[str]


class AuctionBidAction(BaseModel):
    amount: Price
    auction_type: str
    beneficiary: AccountAddress
    bidder: AccountAddress
    nft: None | NftItemRepr


class Action(BaseModel):
    AuctionBid: None | AuctionBidAction
    ContractDeploy: None | ContractDeployAction
    JettonTransfer: None | JettonTransferAction
    NftItemTransfer: None | NftItemTransferAction
    NftPurchase: None | NftPurchase
    Subscribe: None | SubscriptionAction
    TonTransfer: None | TonTransferAction
    UnSubscribe: None | UnSubscriptionAction
    simple_preview: ActionSimplePreview
    status: str
    type: str


class AccountEvent(BaseModel):
    account: AccountAddress
    actions: list[Action]
    event_id: str
    fee: Fee
    in_progress: bool
    is_scam: bool
    lt: int
    timestamp: int


class AccountEvents(BaseModel):
    events: list[AccountEvent]
    next_from: None | int


class Event(BaseModel):
    actions: list[Action]
    event_id: str
    fees: list[Fee]
    in_progress: bool
    is_scam: bool
    lt: int
    timestamp: int
