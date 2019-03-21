import requests
import json
import jsonpath
import pygal

# 1. 请求拿到全部刺激战场的数据 json数据
response = requests.get("http://pg.qq.com/zlkdatasys/data_zlk_zlzx.json")

# 2. 把json数据转化为Python数据
py_data = json.loads(response.text)

# 3. 从Python数据抽取 枪支名称、枪支性能
gun_name = jsonpath.jsonpath(py_data, "$..mc_94")[1:8]
gun_xinn = jsonpath.jsonpath(py_data, "$..ldtw_f2")[0:7]

data = []

for i in gun_xinn:
    data.append([int(i[0]['wl_45']), int(i[0]['sc_54']), int(i[0]['ss_d0']), int(i[0]['wdx_a7']), int(i[0]['zds_62'])])

# 4. 雷达图设计
# 调用Radar这个类，设置雷达图
radar_chart = pygal.Radar()
# 设置雷达图标题
radar_chart.title = "步枪性能"
# 添加雷达图各顶点的含义
radar_chart.x_labels = ["威力", "射程", "射速", "稳定性", "子弹数"]
for n, d in zip(gun_name, data):
    radar_chart.add(n, d)

# 保存图像
radar_chart.render_to_file("gun.svg")
