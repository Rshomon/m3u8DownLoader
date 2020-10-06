import aiohttp, asyncio


async def Demo():
    async with aiohttp.ClientSession() as session:
        resp = session.get(
            "https://c1v-h.phncdn.com/hls/videos/202009/04/348853841/,1080P_4000K,720P_4000K,480P_2000K,240P_400K,_348853841.mp4.urlset/seg-5-f2-v1-a1.ts?fGv3BvJDqNNMhaCPBV9fDKhGq9eoN5SFIx2AO3hi0seM3K7WofIAeGR9yiKTyktU5EA0I_EkMTZsUy4bZ_XfyjsNwRrdmH0YMW0cEI0vrfBKh2Xy9gEyIIRxTvbYiVKZF90-S2FxYwk_PHwAQfVadASzVN0kQLrcjttfsYUUmt4yN3A55WoKXKz6qZ9lli_mNu6j37MZnLhhqvhmvNcBUg"
        )
        result = await resp.read()
        with open('2.ts', 'wb') as f:
            f.write(result)


if __name__ == "__main__":
    asyncio.run(Demo())
