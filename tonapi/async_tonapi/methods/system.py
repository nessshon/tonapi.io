from ..client import AsyncTonapiClient

from ...constants import Method
from ...types.system import Time


class System(AsyncTonapiClient):

    async def time(self) -> Time:
        """Get current time.

        :return: :class:`Time` object.
        """
        response = await self._request(Method.system.time)

        return Time(**response)
