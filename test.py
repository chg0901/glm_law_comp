from prompt import *
from LLM import *

table_plan_map = {
    'company_info': 0,
    'company_register': 1,
    'sub_company_info': 2,
    'legal_document': 3,
    'legal_abstract': 4,
    'xzgxf_info': 5,
    'legal_document_list': 6,
    'court_info': 7,
    'court_code': 8,
    'lawfirm_info': 9,
    'lawfirm_log': 10,
    'address_info': 11,
    'address_code': 12,
    'temp_info': 13
    }

print(LLM(TABLE_PROMPT.format(question="91310000677833266F的公司全称是？该公司的涉案次数为？（起诉日期在2020年）作为被起诉人的次数及总金额为？")))
