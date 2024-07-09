from functions import get_company_register_name, get_legal_document_list

# 查询公司全称
company_name = get_company_register_name(social_code='91310000677833266F')
print("公司全称：", company_name.get('公司名称', '未知'))

# 查询2020年作为被起诉人的次数及总金额
company_legal_docs = get_legal_document_list(affiliated_company_name=company_name.get('公司名称', '未知'), need_fields=['案号', '涉案金额'])
print("涉案次数：", len(company_legal_docs))

def is_sued_in_2020(doc):
    # 检查起诉日期是否在2020年
    return doc.get('日期', '').startswith('2020')

def sum_of_amount(docs):
    # 计算总金额
    total_amount = 0
    for doc in docs:
        amount = doc.get('涉案金额')
        if amount:
            try:
                total_amount += float(amount)
            except ValueError:
                pass
    return total_amount

sued_docs = list(filter(is_sued_in_2020, company_legal_docs))
print("作为被起诉人的次数（2020年）：", len(sued_docs))
print("作为被起诉人的总金额（2020年）：", sum_of_amount(sued_docs))