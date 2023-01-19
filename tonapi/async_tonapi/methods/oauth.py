from typing import Literal

from ..client import AsyncTonapiClient

from ...constants import Method
from ...types.oauth import AuthToken


class OAuth(AsyncTonapiClient):

    async def get_token(self, auth_token: str, rate_limit: int = 1,
                        token_type: Literal["client", "server"]
                        = "server") -> AuthToken:
        """Checks the validity of the auth token.

        :param auth_token: The token which was returned by
         the method below.
        :param rate_limit: Request per seconds. Default value 1
        :param token_type: [client, server], type of token which
         will be used to indicate the app. default value server.
         Learn more about serverside and clientside flows:
         https://tonapi.io/docs#serverside-and-clientside-flows/
        :return: :class:`AuthToken` object
        """
        params = {
            'auth_token': auth_token,
            'rate_limit': rate_limit,
            'token_type': token_type,
        }
        response = await self._request(Method.oauth.getToken, params)

        return AuthToken(**response)
