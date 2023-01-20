## Tonapi.io
Python wrapper for [tonapi.io](https://tonapi.io/swagger-ui/).\
You need an api key to use it, get it here [telegram-bot](https://tonapi_bot.t.me/)

### Installation

```bash
pip install tonapi.io
```

### Examples

Get wallet balance:

```python
# Importing required package
from tonapi import Tonapi
from tonapi.utils import nano_to_amount


def main():
    # Creating new Tonapi object
    tonapi = Tonapi(api_key="Your api key")

    address = "EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess"
    account = tonapi.account.get_info(account=address)

    # print account balance (default returned in nanoton)
    print(account.balance)
    # 1500000000

    # print account balance in amount
    print(nano_to_amount(account.balance))
    # 1.5


if __name__ == '__main__':
    main()
```

#### Asynchronous example:

```python
# Importing required package
import asyncio

from tonapi import AsyncTonapi
from tonapi.utils import nano_to_amount


# Declaring asynchronous function for using await
async def main():
    # Creating new Tonapi object
    tonapi = AsyncTonapi(api_key="Your api key")

    address = "EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess"
    account = await tonapi.account.get_info(account=address)

    # print account balance (default returned in nanoton)
    print(account.balance)
    # 1500000000

    # print account balance in amount
    print(nano_to_amount(account.balance))
    # 1.5


if __name__ == '__main__':
    # Running asynchronous function
    asyncio.run(main())
```

\
Get transactions by wallet address:

```python
# Importing required package
from tonapi import Tonapi
from tonapi.utils import nano_to_amount


def main():
    # Creating new Tonapi object
    tonapi = Tonapi(api_key="Your api key")

    address = "EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess"
    search = tonapi.blockchain.get_transactions(
        account=address, limit=100
    )
    for transaction in search.transactions:
        # print transaction value (default returned in nanoton)
        print(transaction.in_msg.value)
        # 1000000000

        # print transaction value in amount
        print(nano_to_amount(transaction.in_msg.value))
        # 1.0

        # print transaction comment (if the comment is missing will return the None)
        print(transaction.in_msg.msg_data.text)
        # Hello, World!


if __name__ == '__main__':
    main()
```

\
Search for NFT items in the wallet using filters:

```python
# Importing required package
from tonapi import Tonapi


def main():
    # Creating new Tonapi object
    tonapi = Tonapi(api_key="Your api key")

    address = "EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess"
    search = tonapi.nft.search_items(
        owner=address, include_on_sale=True, limit=10
    )
    for nft in search.nft_items:
        # print nft address (default returned in raw)
        print(nft.address)
        # 0:5208588c1643b4cef7a673a57ee00a3967e485fcc8418c1581a8120444f199e1

        # print nft address to userfriendly
        print(nft.address.userfriendly)
        # EQBSCFiMFkO0zvemc6V-4Ao5Z-SF_MhBjBWBqBIERPGZ4aYe


if __name__ == '__main__':
    main()
```

\
Get all NFT items from collection by collection address:

```python
# Importing required package
from tonapi import Tonapi


def main():
    # Creating new Tonapi object
    tonapi = Tonapi(api_key="Your api key")

    collection_address = "EQAUxYSo-UwoqAGixaD3d7CNLp9PthgmEZfnr6BvsijzJHdA"
    search = tonapi.nft.search_items(
        collection=collection_address, include_on_sale=True, limit=1000
    )
    for nft in search.nft_items:
        # print nft owner address (default returned in raw)
        print(nft.owner.address)
        # 0:5208588c1643b4cef7a673a57ee00a3967e485fcc8418c1581a8120444f199e1

        # print nft owner address to userfriendly
        print(nft.owner.address.userfriendly)
        # EQBSCFiMFkO0zvemc6V-4Ao5Z-SF_MhBjBWBqBIERPGZ4aYe


if __name__ == '__main__':
    main()
```

And more . . .\
\
\
**Buy Me a Coffee:**\
<a href="https://app.tonkeeper.com/transfer/EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess"><img src="https://telegra.ph//file/8e0ac22311be3fa6f772c.png" width="55"/></a>
<a href="https://tonhub.com/transfer/EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess"><img src="https://telegra.ph//file/7fa75a1b454a00816d83b.png" width="55"/></a>\
```EQC-3ilVr-W0Uc3pLrGJElwSaFxvhXXfkiQA3EwdVBHNNess```
