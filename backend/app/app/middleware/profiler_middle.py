import cProfile
import pstats
import time
from typing import Optional

from starlette.requests import Request
from starlette.routing import Router
from starlette.types import ASGIApp, Message, Receive, Scope, Send


class CProfileMiddleware:
    def __init__(
            self,
            app: ASGIApp,
            server_app: Optional[Router] = None,
            enable: bool = True,
            sort_by: str = 'cumulative',
            print_each_request: bool = False,
            filename: str = None,
            strip_dirs: bool = False):

        self.app = app
        self.enable = enable
        self._server_app = server_app
        if enable:
            self._profiler = cProfile.Profile()
            self._sort_by = sort_by
            self._print_each_request = print_each_request
            self._filename = filename
            self._strip_dirs = strip_dirs

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:

        if scope["type"] != "http" or self.enable is False:
            await self.app(scope, receive, send)
            return

        if self._server_app is not None:
            self._server_app.add_event_handler("shutdown", self.get_profiler_result)

        self._profiler.enable()

        request = Request(scope, receive=receive)
        method = request.method
        path = request.url.path
        begin = time.perf_counter()

        # Default status code used when the application does not return a valid response
        # or an unhandled exception occurs.
        status_code = 500

        async def wrapped_send(message: Message) -> None:
            if message['type'] == 'http.response.start':
                nonlocal status_code
                status_code = message['status']
            await send(message)

        try:
            await self.app(scope, receive, wrapped_send)
        finally:
            if self._print_each_request:
                self._profiler.disable()
                end = time.perf_counter()
                print(f"Method: {method} ", f"Path: {path} ", f"Duration: {end - begin} ", f"Status: {status_code}")
                ps = pstats.Stats(self._profiler).sort_stats(self._sort_by)
                if self._strip_dirs:
                    ps.strip_dirs()
                ps.print_stats()

    async def get_profiler_result(self):
        self._profiler.disable()
        ps = pstats.Stats(self._profiler).sort_stats(self._sort_by)
        if self._strip_dirs:
            ps.strip_dirs()
        if self._filename:
            ps.dump_stats(self._filename)
