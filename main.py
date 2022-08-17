from classes import discordgateway, voice_client
import asyncio
from aioconsole import aprint



token = "token"

async def main():
    dg = discordgateway(token)
    await dg.simple_connect()
    await dg.member_chunk(976120247427948564)
    # await dg.on_msg()
    # await dg.lazy_guild(1007769600689176617, 1007769601251225704)

asyncio.run(main())