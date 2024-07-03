import requests
url = f"https://comm.chatglm.cn/law_api/s1_b/save_dict_list_to_word"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
}
data = {"company_name": company_name, "dict_list": dict_list}
rsp = requests.post(url, json=data, headers=headers)
open('1.docx', "wb").write(rsp.content)