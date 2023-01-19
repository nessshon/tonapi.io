import base64
import struct

import libscrc


def raw_to_userfriendly(address: str, tag=0x11) -> str:
    workchain_id, key = address.split(':')
    workchain_id = int(workchain_id)
    key = bytearray.fromhex(key)

    short_ints = [j * 256 + i for i, j in zip(*[iter(key)] * 2)]
    payload = struct.pack(f'Bb{"H" * 16}', tag, workchain_id, *short_ints)
    crc = libscrc.xmodem(payload, )
    e_key = payload + struct.pack('>H', crc)

    return base64.urlsafe_b64encode(e_key).decode("utf-8")


def userfriendly_to_raw(address: str) -> str:
    k = base64.urlsafe_b64decode(address)[1:34]
    workchain_id = struct.unpack('b', k[:1])[0]
    key = k[1:].hex().upper()

    return f'{workchain_id}:{key}'


def nano_to_amount(value: int | float, precision: int = 2) -> float:
    """from nanoton to TON

    Args:
        value: [ :class:`int` | :class:`float` ] Amount TON in nanoton.
        precision: [ :class:`int` ] Number of digits after floating point.

    Returns:
        :class:`float` - TON

    """
    converted_value = round(value / 10 ** 9, 9)

    return float(f'{converted_value:.{precision}f}')


def amount_to_nano(value: int | float) -> int:
    """From TON to nanoton

    Args:
        value: [ :class:`int` | :class:`float` ] Amount in TON

    Returns:
        :class:`int` - nanoton
    """
    return int(value * (10 ** 9))
