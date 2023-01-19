from ..client import AsyncTonapiClient

from ...constants import Method
from ...types.account import AccountRepr, AccountReprs


class Account(AsyncTonapiClient):

    async def get_bulk_info(self, addresses: list[str]) -> AccountReprs:
        """Get info about few accounts account by one request.

        :param addresses: Account addresses in
         raw (hex without 0x) or base64url format.
        :return: :class:`AccountReprs` object.
        """
        params = {'addresses': ','.join(map(str, addresses))}
        response = await self._request(Method.account.getBulkInfo, params)

        return AccountReprs(**response)

    async def get_info(self, account: str) -> AccountRepr:
        """Get info about account.

        :param account: address in raw (hex without 0x)
         or base64url format.
        :return: :class:`AccountRepr` object.
        """
        params = {'account': account}
        response = await self._request(Method.account.getInfo, params)

        return AccountRepr(**response)
