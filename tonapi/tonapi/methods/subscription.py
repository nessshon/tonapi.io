from ..client import TonapiClient

from ...constants import Method
from ...types.subscription import Subscriptions


class Subscription(TonapiClient):

    def get_by_wallet(self, account: str) -> Subscriptions:
        """Get all subscriptions by wallet address.

        :param account: address in raw (hex without 0x) or base64url format.
        :return: :class:`Subscriptions` object.
        """
        params = {'account': account}
        response = self._request(Method.subscription.getByWallet, params)

        return Subscriptions(**response)
