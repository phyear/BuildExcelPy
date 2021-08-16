import random
import json
import openpyxl

def handlerPredefinedValue(predefinedValueDist, predefinedValueS, headNames):
    for index in range(len(predefinedValueS)):
        predefinedValue = predefinedValueS[index]
        if isinstance(predefinedValue, list):
            if len(headNames) > index and headNames[index] != None:
                predefinedValueDist[headNames[index]] = predefinedValue
        if isinstance(predefinedValue, dict):
            predefinedValueDist[predefinedValue['headName']]= predefinedValue['valueRanges']

def handlerRowData(predefinedValueDist, heandNames):
    data = {}
    for index in range(len(heandNames)):
       predefinedValue = predefinedValueDist[heandNames[index]]
       if predefinedValue != None and len(predefinedValue) > 0:
           data[index+1] = predefinedValue[random.randrange(0, len(predefinedValue))]
    return data

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
    ### 处理预定义predefinedValue
    predefinedValueDist = {}
    handlerPredefinedValue(predefinedValueDist, jsonObject['predefinedValue'], heandNames) 
    ### 构造数据
    for calcRule in jsonObject['calcRules']:
        custom = predefinedValueDist.copy()
        handlerPredefinedValue(custom, calcRule['predefinedValue'], heandNames)
        for i in range(calcRule['amount']):
            datas.append(handlerRowData(custom,heandNames))   

    return datas         