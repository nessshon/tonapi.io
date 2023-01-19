from pydantic import BaseModel


class AuthToken(BaseModel):
    """This is a test class for dataclasses.

    This is the body of the docstring description.

    Attributes:
        address (int): An integer.
        user_token (str): A string.
        pubkey (str): A string.
        wallet_version (str): A string.
        client_id (str): A string.
    """
    address: str
    user_token: str
    pubkey: None | str
    wallet_version: None | str
    client_id: None | str
