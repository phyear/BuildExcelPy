import random
import json
import openpyxl

def buildData(buildJson):
    ### 定义返回的数据空list
    datas = []
    if buildJson == None and buildJson =='':
        return datas
    #### 如果字段名列表为空报错    
    jsonObject = json.loads(buildJson)
    heandNames = jsonObject['headNames'] 
    if heandNames == None and heandNames.lenght <= 0:
        return datas   