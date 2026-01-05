import aiohttp
from bs4 import BeautifulSoup


async def get_gold_rate():
    url = "https://goldpricez.com/"

    async with aiohttp.ClientSession() as session:
        headers = {"User-Agent": "Mozilla/5.0"}
        async with session.get(url, headers=headers) as response:
            html = await response.text()

    soup = BeautifulSoup(html, "html.parser")

    price_span = soup.find("span", id="gold_price")

    if price_span:
        price_text = price_span.text.strip()
        price_text = price_text.replace("$", "").replace(",", "")
        try:
            price = float(price_text.split('=')[-1].strip())
            return price
        except ValueError:
            return None
    return None
