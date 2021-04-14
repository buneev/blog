import asyncio
from aiohttp import web


async def parse_site(request):
    jo = await request.json()
    cmd = f"cd /code/src && scrapy crawl {jo['spider']} --logfile=/log/{jo['spider']}.log"
    cmd = cmd + f" -a debug={jo.get('debug', False)}"
    pid = await run(cmd)
    # jo.update({'pid': pid, 'ppid': ppid})
    print(f'Run web scraping success, PID: {pid}\nCMD: {cmd}')
    return web.json_response(jo)

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    # print(f'[{cmd!r} exited with {proc.returncode}]')
    # if stdout:
    #     print(f'[stdout]\n{stdout.decode()}')
    # if stderr:
    #     print(f'[stderr]\n{stderr.decode()}')

# async def main():
app = web.Application()
app.router.add_post('/parse_site', parse_site)
web.run_app(app, port=5858)
# return app

