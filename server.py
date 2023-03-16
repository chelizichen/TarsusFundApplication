from sanic import Sanic, json, Request, HTTPResponse

from src.db.db import DBPool
from src.util.ret import ret

app = Sanic("TarsusFundApplication")


@app.route("/fund_sort")
async def fund_sort(request: Request) -> HTTPResponse:
    data = DBPool.select("SELECT count(*) as total,fund_type from fund_list GROUP BY fund_list.fund_type")

    return json(ret.success(data))

if __name__ == '__main__':
    app.run()
