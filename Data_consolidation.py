import pandas as pd
##-------------------
def run(path1,path2):
    system = readCSV2List(path1)
    power = readCSV2List(path2)

    systemlength = len(system)-1
    powerlength = len(power)-1

    for i in range(systemlength):
        for j in range(powerlength):
            if(system[i][1]==power[j][0]): 
                system[i].append(power[j][2])
                break
    print('------------------')

    for row in system:  
        del row[0]

    concen=pd.DataFrame(system)
    concen.to_csv('foo.csv',encoding='gbk')

    remain = list()
    for i in range(systemlength):
        for j in range(powerlength):
            if(len(system[i])!=4):
                system[i]=0         
                remain.append(i)  
                break

    for i in range(len(remain)):   
         system.remove(0)           

    concen=pd.DataFrame(system)
    print(concen)
    concen.to_csv('foo.csv',encoding='gbk')

def readCSV2List(filePath):
    try:
        file=open(filePath,'r',encoding="gbk")
        context = file.read() 
        list_result=context.split("\n")
        length=len(list_result)
        for i in range(length):
            list_result[i]=list_result[i].split(",")
        return list_result
    except Exception :
        print("文件读取转换失败，请检查文件路径及文件编码是否正确")
    finally:
        file.close();
