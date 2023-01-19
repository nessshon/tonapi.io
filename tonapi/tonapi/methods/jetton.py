from ..client import TonapiClient

from ...constants import Method
from ...types.event import AccountEvents
from ...types.jetton import JettonsBalances, JettonInfo


class Jetton(TonapiClient):

    def get_balances(self, account: str) -> JettonsBalances:
        """Get all Jettons balances by owner address.

        :param account: Address in raw (hex without 0x) or base64url format.
        :return: :class:`JettonsBalances` object.
        """
        params = {'account': account}
        response = self._request(Method.jetton.getBalances, params)

        return JettonsBalances(**response)

    def get_history(self, account: str, jetton_master: str,
                    limit: int = 1000) -> AccountEvents:
        """Get all Jetton transfers for account.

        :param account: Address in raw (hex without 0x) or base64url format.
        :param jetton_master: Address in raw (hex without 0x) or base64url format.
        :param limit: Default value 1000
        :return: :class:`AccountEvents` object.
        """
        params = {
            'account': account,
            'jetton_master': jetton_master,
            'limit': limit,
        }
        response = self._request(Method.jetton.getHistory, params)

        return AccountEvents(**response)

    def get_info(self, account: str) -> JettonInfo:
        """Get jetton metadata by jetton master address.

        :param account: Address in raw (hex without 0x) or base64url format.
        :return: :class:`JettonInfo` object.
        """
        params = {'account': account}
        response = self._request(Method.jetton.getInfo, params)

        return JettonInfo(**response)
