import requests

from ..constants import Url
from ..exceptions import TonapiError, TonapiUnauthorized, TonapiException


class TonapiClient:

    def __init__(self, api_key: str, testnet: bool = False):
        self._api_key = api_key
        self._testnet = testnet

        self.__headers = {'Authorization': 'Bearer ' + api_key}
        self.__base_url = Url.TESTNET if testnet else Url.MAINNET

    def _request(self, method: str, params: dict = None):
        params = params.copy() if params is not None else {}

        with requests.Session() as session:
            with session.get(f"{self.__base_url}{method}",
                             params=params,
                             headers=self.__headers
                             ) as response:
                response_json = response.json()

                match response.status_code:
                    case 200:
                        return response_json
                    case 400:
                        raise TonapiError
                    case 401:
                        raise TonapiUnauthorized
                    case _:
                        raise TonapiException
