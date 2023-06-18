from aiohttp import web
import asyncio

from equipment .abs_equip import FireEquipment

async def handle(request):
    name = request.match_info.get("name", "firefighter")
    text = "Hi, " + name
    fireTest = FireEquipment().kingdom_name
    text = text + '\n' + f"this is your {fireTest}"
    return web.Response(text = text)

app = web.Application()
app.add_routes([
    web.get('/', handle),
    web.get('/{name}', handle)
    ])

if __name__ == '__main__':
    web.run_app(app)