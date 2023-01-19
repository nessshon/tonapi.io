from ..client import AsyncTonapiClient

from ...constants import Method
from ...types.auction import DomainBids, Auctions


class Auction(AsyncTonapiClient):

    async def get_bids(self, domain: str) -> DomainBids:
        """Get domain bids.

        :param domain: domain names with .ton
        :return: :class:`DomainBids` object.
        """
        params = {'domain': domain}
        response = await self._request(Method.auction.getBids, params)

        return DomainBids(**response)

    async def get_current(self, tld: str) -> Auctions:
        """Get all auctions.

        :param tld: Domain filter for current auctions "ton" or "t.me".
        :return: :class:`Auctions` object.
        """
        params = {'tld': tld}
        response = await self._request(Method.auction.getCurrent, params)

        return Auctions(**response)
