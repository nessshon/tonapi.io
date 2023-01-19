from ..client import TonapiClient

from ...constants import Method
from ...types.system import Time


class System(TonapiClient):

    def time(self) -> Time:
        """Get current time.

        :return: :class:`Time` object.
        """
        response = self._request(Method.system.time)

        return Time(**response)
