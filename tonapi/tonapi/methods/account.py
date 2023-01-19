from ..client import TonapiClient

from ...constants import Method
from ...types.account import AccountRepr, AccountReprs


class Account(TonapiClient):

    def get_bulk_info(self, addresses: list[str]) -> AccountReprs:
        """Get info about few accounts account by one request.

        :param addresses: Account addresses in
         raw (hex without 0x) or base64url format.
        :return: :class:`AccountReprs` object.
        """
        params = {'addresses': ','.join(map(str, addresses))}
        response = self._request(Method.account.getBulkInfo, params)

        return AccountReprs(**response)

    def get_info(self, account: str) -> AccountRepr:
        """Get info about account.

        :param account: address in raw (hex without 0x)
         or base64url format.
        :return: :class:`AccountRepr` object.
        """
        params = {'account': account}
        response = self._request(Method.account.getInfo, params)

        return AccountRepr(**response)
