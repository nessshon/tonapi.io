from ..client import AsyncTonapiClient

from ...constants import Method
from ...types.blockchain import Account, Transactions, Transaction, Block, Validators


class Blockchain(AsyncTonapiClient):

    async def get_account(self, account: str) -> Account:
        """Get raw account data.

        :param account: address in raw (hex without 0x)
         or base64url format.
        :return: :class:`Account` object.
        """
        params = {'account': account}
        response = await self._request(Method.blockchain.getAccount, params)

        return Account(**response)

    async def get_block(self, block_id: str) -> Block:
        """Get block by id.

        :param block_id: block id.
        :return: :class:`Block` object.
        """
        params = {'block_id': block_id}
        response = await self._request(Method.blockchain.getBlock, params)

        return Block(**response)

    async def get_transaction(self, hash_: str) -> Transaction:
        """Get transaction by hash.

        :param hash_: Transaction hash in hex (without 0x) or base64url format.
        :return: :class:`Transaction` object.
        """
        params = {'hash': hash_}
        response = await self._request(Method.blockchain.getTransaction, params)

        return Transaction(**response)

    async def get_transactions(self, account: str, max_lt: int = None,
                               min_lt: int = None, limit: int = 100
                               ) -> Transactions:
        """Get transactions.

        :param account: Address in raw (hex without 0x) or base64url format.
        :param max_lt: Omit this parameter to get last transactions.
        :param min_lt: Omit this parameter to get last transactions.
        :param limit: Default value : 100
        :return: :class:`Transactions` object.
        """

        params = {
            'account': account,
            'limit': limit,
        }
        if max_lt: params['maxLt'] = max_lt
        if min_lt: params['minLt'] = min_lt

        response = await self._request(Method.blockchain.getTransactions, params)

        return Transactions(**response)

    async def validators(self) -> Validators:
        """Get validators info list.

        :return: :class:`Validators` object.
        """
        response = await self._request(Method.blockchain.validators)

        return Validators(**response)
