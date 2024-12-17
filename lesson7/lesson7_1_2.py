import requests
from requests import Response
from io import StringIO
from csv import DictReader
from requests.exceptions import RequestException,HTTPError

def get_youbikes()->list[dict]:
    url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/csv?page=0&size=1000'

    try:
        r:Response = requests.request('GET',url)
        r.raise_for_status()  #如果不是200raise錯誤 
        #print("下載成功") #檢查前二行
    except HTTPError as e: #單一錯
        print(e)
    except RequestException as e: #全部錯
        print(e)
    else:
        print("下載成功") #檢查全部部
        file = StringIO(r.text)
        reader = DictReader(file)
        list_reader:list[dict] = list(reader) #list 保留資料在dict裡,不用list資料會不見
       #print(list_reader)
        return list_reader
    
    '''
    建立tools
    import tools

    youbike_data:list[dict] = tools.get_youbikes()
    print(youbike_data)

    '''