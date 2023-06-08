from src.db.db import get_db
from src.script.load_his import get_fund_k_history


data = get_db.select("select fund_code from fund_list limit 0,100")

for i in range(len(data)):
    get_fund_k_history(data[i][0])
    print(data[i][0],"加载完毕")


