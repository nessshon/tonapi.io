import base64

from pydantic.main import BaseModel

from ..utils import raw_to_userfriendly


class address(BaseModel):
    __root__: str

    @property
    def userfriendly(self):
        return raw_to_userfriendly(self.__root__)

    def __str__(self):
        return self.__root__


class msg_data(BaseModel):
    __root__: str | dict

    @property
    def text(self) -> str | None:
        try:
            return (base64.b64decode(self.__root__)
                    .strip(b"\x00").decode('utf-8'))
        except UnicodeDecodeError:
            return None

    def __str__(self):
        return self.__root__
