from aiohttp import web
import asyncio

from equipment.tools_setter import HosesSetter

async def handle(request):
    name = request.match_info.get("name", "firefighter")
    text = "Hi, " + name
    setter = HosesSetter()
    hoses = setter()
    text = text + '\n' + f"""
        first hose:{hoses[1]}, 
        second: {hoses[-1]}
    """

    return web.Response(text = text)

app = web.Application()
app.add_routes([
    web.get('/', handle),
    web.get('/{name}', handle)
    ])

if __name__ == '__main__':
    web.run_app(app)