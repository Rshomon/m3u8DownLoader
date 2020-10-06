import asyncio, aiohttp
import re
import aiofiles


class Downloader:
    def __init__(self) -> None:
        with open("1.txt", "r") as f:
            self.url_list = f.readlines()

    async def fetch(self, session, url):
        url = url.strip()
        print(url)
        print('aa')
        async with session.get(url) as resp:
            print(resp.status)

    async def main(self):
        async with aiohttp.ClientSession() as session:
            task_list = [
                self.fetch(session=session, url=url)
                for url in self.url_list[:5]
            ]
            # 返回处理的状态
            result = await asyncio.wait(task_list)
            print(result)


if __name__ == "__main__":
    download = Downloader()
    asyncio.run(download.main())