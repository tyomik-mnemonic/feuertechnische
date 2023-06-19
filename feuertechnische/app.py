from aiohttp import web
import asyncio

from equipment.fire_equipment.hose import HoseFabric

RUSSIAN66_1 = HoseFabric.create_hose(66)
RUSSIAN66_2 = HoseFabric.create_hose(66)
async def handle(request):
    name = request.match_info.get("name", "firefighter")
    text = "Hi, " + name
    #FireEquipment().kingdom_name
    hose_test1 = RUSSIAN66_1.tool_property
    hose_test2 = RUSSIAN66_2.tool_property
    text = text + '\n' + f"""
        first hose:{hose_test1}, 
        second: {hose_test2}
    """

    return web.Response(text = text)

app = web.Application()
app.add_routes([
    web.get('/', handle),
    web.get('/{name}', handle)
    ])

if __name__ == '__main__':
    web.run_app(app)