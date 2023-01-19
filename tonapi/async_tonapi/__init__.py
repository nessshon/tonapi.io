from .client import AsyncTonapiClient

from .methods.account import Account
from .methods.auction import Auction
from .methods.blockchain import Blockchain
from .methods.dns import DNS
from .methods.jetton import Jetton
from .methods.nft import NFT
from .methods.oauth import OAuth
from .methods.subscription import Subscription
from .methods.system import System


class AsyncTonapi(AsyncTonapiClient):
    def __init__(self, api_key: str, testnet: bool = False):
        """
        :param api_key: Secret key from https://t.me/tonapi_bot
        :param testnet: Use true, if you want to switch to testnet
        """
        super(AsyncTonapi, self).__init__(api_key, testnet)

    @property
    def account(self) -> Account:
        return Account(self._api_key, self._testnet)

    @property
    def auction(self) -> Auction:
        return Auction(self._api_key, self._testnet)

    @property
    def blockchain(self) -> Blockchain:
        return Blockchain(self._api_key, self._testnet)

    @property
    def dns(self) -> DNS:
        return DNS(self._api_key, self._testnet)

    @property
    def jetton(self) -> Jetton:
        return Jetton(self._api_key, self._testnet)

    @property
    def nft(self) -> NFT:
        return NFT(self._api_key, self._testnet)

    @property
    def oauth(self) -> OAuth:
        return OAuth(self._api_key, self._testnet)

    @property
    def subscription(self) -> Subscription:
        return Subscription(self._api_key, self._testnet)

    @property
    def system(self) -> System:
        return System(self._api_key, self._testnet)
