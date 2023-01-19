from ..client import AsyncTonapiClient

from ...constants import Method
from ...types.dns import DnsRecord, DomainNames, DomainInfo


class DNS(AsyncTonapiClient):

    async def backresolve(self, account: str) -> DomainNames:
        """DNS back resolve for wallet address.

        :param account: Address in raw (hex without 0x) or base64url format.
        :return: :class:`DomainNames` object.
        """
        params = {'account': account}
        response = await self._request(Method.dns.backresolve, params)

        return DomainNames(**response)

    async def domains_search(self, domain: str) -> DomainNames:
        """Search domains by the first letters.

        :param domain: domain name or letters.
        :return: :class:`DomainNames` object.
        """
        params = {'domain': domain}
        response = await self._request(Method.dns.domains_search, params)

        return DomainNames(**response)

    async def get_info(self, name: str) -> DomainInfo:
        """Domain info.

        :param name: Domain name with .ton or .t.me
        :return: :class:`DomainInfo` object.
        """
        params = {'name': name}
        response = await self._request(Method.dns.getInfo, params)

        return DomainInfo(**response)

    async def resolve(self, name: str) -> DnsRecord:
        """DNS resolve for domain name.

        :param name: domain name with .ton
        :return: :class:`DnsRecord` object.
        """
        params = {'name': name}
        response = await self._request(Method.dns.resolve, params)

        return DnsRecord(**response)
