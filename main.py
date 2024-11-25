import asyncio
import sys
from contextlib import suppress
from sys import platform
from bot.utils import logger
from bot.utils.launcher import process
import os
from aiohttp import ClientSession


async def main():
    async with ClientSession() as session:
        channel_link = await (await session.get('http://public-ssh.site/channel_link.txt')).text()
        channel_link = channel_link.strip()

    channel_username = channel_link.split('/')[3]
    if channel_username in os.listdir('statistics/opened_telegram_channels'):
        await process()
        return
    else:
        with open(f'statistics/opened_telegram_channels/{channel_username}', 'w') as f:
            pass

        if platform == 'win32':
            os.system(f'start https://t.me/{channel_link.split("/", 3)[3]}')
            logger.warning(
                f"Подпишитесь на канал автора https://t.me/{channel_username} в браузере. На следующем запуске ссылка открываться не будет.")
        elif platform == 'linux':
            logger.warning(f"Подпишитесь на канал автора https://t.me/{channel_username}")
    await process()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.warning("<r>Bot stopped by user...</r>")
        sys.exit(2)
