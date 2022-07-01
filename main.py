import asyncio

from lyght.http.server import Server


if __name__ == "__main__":
    _server = Server(host='localhost', port=5000, log_level='info')
    asyncio.run(_server.serve())
