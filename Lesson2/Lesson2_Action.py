import requests
from bs4 import BeautifulSoup
import pandas as pd

# 请求url
url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-1.shtml'

# 根据request_url得到soup
def get_page_content(request_url):
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
    html = requests.get(request_url, headers=headers, timeout=10)
    content = html.text
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    return soup

# 分析当前页面的投诉
def analysis(soup):
    temp = soup.find('div', class_='tslb_b')
    df = pd.DataFrame(columns = ['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        temp = {}
        td_list = tr.find_all('td')
        # 第一个tr没有td, 其余都有8个td
        if len(td_list) > 0:
            id, brand, car_model, type, desc, problem, datetime, status = td_list[0].text, td_list[1].text, td_list[2].text, td_list[3].text, td_list[4].text, td_list[5].text, td_list[6].text, td_list[7].text
            temp['id'], temp['brand'], temp['car_model'], temp['type'], temp['desc'], temp['problem'], temp['datetime'], temp['status'] = id, brand, car_model, type, desc, problem, datetime, status
            df = df.append(temp, ignore_index=True)
    return df

page_num = 10
base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'

result = pd.DataFrame(columns = ['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])

for i in range(1, page_num+1):
    request_url = base_url + str(i) + '.shtml'
    soup = get_page_content(request_url)
    df = analysis(soup)
    result = result.append(df)

result.to_excel('./car_complain.xlsx', index=False)