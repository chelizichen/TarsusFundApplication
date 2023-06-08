from sanic import Sanic, json, Request, HTTPResponse

from src.db.db import get_db
from src.script.load_his import get_fund_k_history
from src.util.ret import ret

app = Sanic("TarsusFundApplication")



@app.route("/fund_sort")
async def fund_sort(request: Request) -> HTTPResponse:
    data = get_db.select("SELECT count(*) as total,fund_type from fund_list GROUP BY fund_list.fund_type")

    return json(ret.success(data))


@app.post("/getFundList")
async def fund_sort(request: Request) -> HTTPResponse:
    fundCode = request.json['fundCode']
    pz = int(request.json['pz'])
    print(fundCode,pz)
    get_fund_k_history(fundCode,pz)

    return json(ret.success(pz))


if __name__ == '__main__':
    app.run()
