import pandas as pd
import requests

from src.db.db import get_db


def get_sql():
    return "insert into fund_his(" \
           "`fund_code`," \
           "`date`," \
           "`fund_worth`," \
           "`fund_total_worth`," \
           "`fund_change`) value(" \
           "%s," \
           "%s," \
           "%s," \
           "%s," \
           "%s)"


def get_fund_k_history(fund_code: str, pz: int = 40000) -> pd.DataFrame:
    '''
    根据基金代码和要获取的页码抓取基金净值信息

    Parameters
    ----------
    fund_code : 6位基金代码
    page : 页码 1 为最新页数据

    Return
    ------
    DataFrame : 包含基金历史k线数据
    '''
    # 请求头
    EastmoneyFundHeaders = {
        'User-Agent': 'EMProjJijin/6.2.8 (iPhone; iOS 13.6; Scale/2.00)',
        'GTOKEN': '98B423068C1F4DEF9842F82ADF08C5db',
        'clientInfo': 'ttjj-iPhone10,1-iOS-iOS13.6',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'fundmobapi.eastmoney.com',
        'Referer': 'https://mpservice.com/516939c37bdb4ba2b1138c50cf69a2e1/release/pages/FundHistoryNetWorth',
    }
    # 请求参数
    data = {
        'FCODE': f'{fund_code}',
        'appType': 'ttjj',
        'cToken': '1',
        'deviceid': '1',
        'pageIndex': '1',
        'pageSize': f'{pz}',
        'plat': 'Iphone',
        'product': 'EFund',
        'serverVersion': '6.2.8',
        'version': '6.2.8'
    }
    url = 'https://fundmobapi.eastmoney.com/FundMNewApi/FundMNHisNetList'
    json_response = requests.get(
        url, headers=EastmoneyFundHeaders, data=data).json()
    rows = []
    columns = ['日期', '单位净值', '累计净值', '涨跌幅']
    if json_response is None:
        return pd.DataFrame(rows, columns=columns)
    datas = json_response['Datas']
    if len(datas) == 0:
        return pd.DataFrame(rows, columns=columns)
    rows = []
    for stock in datas:
        date = stock['FSRQ']
        row_data = {
            '日期': date,
            '单位净值': stock['DWJZ'],
            '累计净值': stock['LJJZ'],
            '涨跌幅': stock['JZZZL']
        }
        get_db.update(get_sql(), [
            fund_code,
            date,
            stock["DWJZ"],
            stock["LJJZ"],
            stock['JZZZL']
        ])

        rows.append(row_data)

    df = pd.DataFrame(rows)
    df['单位净值'] = pd.to_numeric(df['单位净值'], errors='coerce')

    df['累计净值'] = pd.to_numeric(df['累计净值'], errors='coerce')

    df['日期'] = pd.to_datetime(df['日期'], errors='coerce')
    return df

