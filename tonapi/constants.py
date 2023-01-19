from dataclasses import dataclass


@dataclass
class Url:
    MAINNET = "https://tonapi.io"
    TESTNET = "https://testnet.tonapi.io"


@dataclass
class Method:
    class oauth:
        getToken = "v1/oauth/getToken"

    class account:
        getBulkInfo = "/v1/account/getBulkInfo"
        getInfo = "/v1/account/getInfo"

    class auction:
        getBids = "/v1/auction/getBids"
        getCurrent = "/v1/auction/getCurrent"

    class blockchain:
        getAccount = "/v1/blockchain/getAccount"
        getBlock = "/v1/blockchain/getBlock"
        getTransaction = "/v1/blockchain/getTransaction"
        getTransactions = "/v1/blockchain/getTransactions"
        validators = "/v1/blockchain/validators"

    class dns:
        backresolve = "/v1/dns/backresolve"
        domains_search = "/v1/dns/domains/search"
        getInfo = "/v1/dns/getInfo"
        resolve = "/v1/dns/resolve"

    class jetton:
        getBalances = "/v1/jetton/getBalances"
        getHistory = "/v1/jetton/getHistory"
        getInfo = "/v1/jetton/getInfo"

    class nft:
        getCollection = "/v1/nft/getCollection"
        getCollections = "/v1/nft/getCollections"
        getItems = "/v1/nft/getItems"
        searchItems = "/v1/nft/searchItems"

    class subscription:
        getByWallet = "/v1/subscription/getByWallet"

    class system:
        time = "/v1/system/time"
