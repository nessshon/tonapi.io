from pydantic import BaseModel

from . import address


class Subscription(BaseModel):
    address: address
    amount: int
    beneficiary_address: address
    failed_attempts: int
    last_payment_time: int
    last_request_time: int
    period: int
    start_time: int
    subscription_id: int
    timeout: int
    wallet_address: address


class Subscriptions(BaseModel):
    subscriptions: list[Subscription]
