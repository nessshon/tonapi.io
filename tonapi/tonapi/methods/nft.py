from ..client import TonapiClient

from ...constants import Method
from ...types.nft import NftItemsRepr, NftCollection, NftCollections


class NFT(TonapiClient):

    def get_collection(self, account: str) -> NftCollection:
        """Get NFT collection by collection address.

        :param account: Address in raw (hex without 0x) or base64url format.
        :return: :class:`NftCollection` object.
        """
        params = {'account': account}
        response = self._request(Method.nft.getCollection, params)

        return NftCollection(**response)

    def get_collections(self, limit: int = 15, offset: int = 0) -> NftCollections:
        """Get all NFT collections.

        :param limit: Default value : 15
        :param offset: Default value : 0
        :return: :class:`NftCollections` object.
        """
        params = {
            'limit': limit,
            'offset': offset
        }
        response = self._request(Method.nft.getCollections, params)

        return NftCollections(**response)

    def get_items(self, addresses: list[str]) -> NftItemsRepr:
        """Get NFT items by addresses.

        :param addresses: NFT items addresses in raw
         (hex without 0x) or base64url format.
        :return: :class:`NftItemsRepr` object.
        """
        params = {'addresses': ','.join(map(str, addresses))}
        response = self._request(Method.nft.getItems, params)

        return NftItemsRepr(**response)

    def search_items(self, owner: str = None, collection: str = None,
                     include_on_sale: bool = False, limit: int = 100,
                     offset: int = 0) -> NftItemsRepr:
        """Search NFT items using filters.

        :param owner: address in raw (hex without 0x) or base64url
         format or word 'no' for items without owner.
        :param collection: address in raw (hex without 0x)
         or base64url format or word 'no' for items without collection.
        :param include_on_sale: Default value false. Include nft items which
         are currently are on market.
        :param limit: Default value 100. Maximum qty of items.
        :param offset: Default value 0. Offset for pagination.
        :return: :class:`NftItemsRepr` object.
        """
        params = {
            'include_on_sale': 'true' if include_on_sale else 'false',
            'limit': limit,
            'offset': offset
        }
        if owner: params['owner'] = owner
        if collection: params['collection'] = collection

        response = self._request(Method.nft.searchItems, params)

        return NftItemsRepr(**response)
