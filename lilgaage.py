import requests
import re

# 作业01

# 定义地址
url_re = "http://127.0.0.1:8000/api/departments/"
#查询所有学院信息
res = requests.get(url_re).text
print(res)
re_dpid = '"dep_id":"(\d{1,10})"'
re_dpname = '"dep_name":"([\\u4e00-\\u9fa5_A-Z_a-z]{1,20})"'
re_mtname = '"master_name":"([\\u4e00-\\u9fa5_A-Z_a-z]{1,20})"'
re_slogan = '"slogan":"(\D{0,20})"'
print("匹配上的dep_id有：", re.findall(re_dpid, res))
print("匹配上的dep_name有：", re.findall(re_dpname, res))
print("匹配上的master_name有：", re.findall(re_mtname, res))
print("匹配上的slogan有：", re.findall(re_slogan, res))


# 作业02

# 定义地址
url = "http://127.0.0.1:8000/api/departments/"
# 查询所有学院信息
res_get = requests.get(url)
# 提取第三个学院id
reg = re.findall('"dep_id":"(.*?)","dep_name":"(.*?)","master_name":"(.*?)","slogan":"(.*?)"', res_get.text)[2]
print(reg)
# 删除第三个学院信息
url_delete = "http://127.0.0.1:8000/api/departments/" + reg[0] + "/"
res_delete = requests.delete(url_delete)
print("删除第三个学院的状态码为：", res_delete.status_code)
# 新增第三个学院信息
# 定制消息头
myheader = {"Content-Type": "application/json"}
# 定义消息体数据
data = '{"data":[{"dep_id":"%s","dep_name":"%s","master_name":"%s","slogan":"%s"}]}' % (reg[0], reg[1], reg[2], reg[3])
# 发送请求
res_post = requests.post(url, data.encode('utf-8'), headers=myheader)
print("新增第三个学院信息：", res_post.text)
