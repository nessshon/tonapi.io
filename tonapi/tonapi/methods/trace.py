from ..client import AsyncTonapiClient

from ...constants import Method
from ...types.trace import TraceMsg, AnnotatedTraceMsg


class Trace(AsyncTonapiClient):

    async def get_trace(self, hash_: str) -> TraceMsg:
        """Get the trace by trace ID or hash of any transaction in trace.

        :param hash_: trace ID or transaction hash in hex (without 0x)
         or base64url format.
        :return: :class:`TraceMsg` object
        """
        params = {'hash': hash_}
        response = await self._request(Method.trace.getTrace, params)

        return TraceMsg(**response)

    async def get_annotated_trace(self, hash_: str) -> AnnotatedTraceMsg:
        """Get the annotated trace by trace ID or hash of any transaction in trace.

        :param hash_: trace ID or transaction hash in hex (without 0x)
         or base64url format.
        :return: :class:`AnnotatedTraceMsg` object
        """
        params = {'hash': hash_}
        response = await self._request(Method.trace.getAnnotatedTrace, params)

        return AnnotatedTraceMsg(**response)
