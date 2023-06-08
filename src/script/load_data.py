import os

from src.db.db import funs_db, get_db

# done


root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))

target_path = os.path.normpath(root_directory + '/fund_list.txt')

f = open(target_path, encoding='utf-8')

data = f.readlines()
f.close()  # 关

to_list = eval(data[0])

sql = "insert into fund_list(" \
      "`fund_code`," \
      "`fund_eng_name`," \
      "`fund_name`," \
      "`fund_type`) values(" \
      "%s," \
      "%s," \
      "%s," \
      "%s)"

for i in range(len(to_list)):
    args = [to_list[i][0], to_list[i][1], to_list[i][2], to_list[i][3]]
    get_db.update(sql, args)
