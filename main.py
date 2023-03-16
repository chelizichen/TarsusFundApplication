import urllib3
import re

from src.db.db import funs_db


def get_rsp(url):
    http = urllib3.PoolManager()
    response = http.request("GET", url)
    data = response.data.decode("utf-8")
    return data


def eval_to_list(pattern, data):
    match = re.search(pattern, data)
    if match:
        match_str = match.group(0)
        write_data("fund_list.txt", match_str)
        data = eval(match_str)
    return data


def write_data(local, data):
    f = open(local, "w")
    f.write(data)


get_db = funs_db("127.0.0.1","root","123456","zrq_shop")

# pattern = r'\[\[(.*?)\]\]'
#
# get_data = get_rsp("https://fund.eastmoney.com/js/fundcode_search.js")
#
# list_data = list(eval_to_list(pattern, get_data))
#
#
# print(list_data)
