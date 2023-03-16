import urllib3
import re

# 已完成 拿到数据所有基金数据
# done


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
