from tools import *

# 查询公司全称
company_social_code = "91310000677833266F"
company_name_info = get_company_register_name(social_code=company_social_code)
company_name = company_name_info['公司名称']
print("公司全称是:", company_name)

# 查询2020年作为被起诉人的次数和总金额
# 注意：这里使用了affiliated_company_name而不是company_name
legal_documents = get_legal_document_list(affiliated_company_name=company_name, need_fields=["标题", "案号", "涉案金额", "被告"])
for i in legal_documents:
    print(i)
# print(legal_documents)  # 打印所有相关的法律文书信息

# 假设我们手动筛选出2020年的数据
sued_times_2020 = 0
total_amount_2020 = 0
for doc in legal_documents:
    # 假设每个文档都有一个日期字段，并且可以从中提取年份信息
    if '日期' in doc and doc['日期'].startswith('2020'):
        sued_times_2020 += 1
        # 假设涉案金额是一个可以转换为数值的字段
        try:
            total_amount_2020 += float(doc['涉案金额'])
        except ValueError:
            # 如果转换失败，可以跳过或者进行其他处理
            pass

print("作为被起诉人的次数为:", sued_times_2020)
print("总金额为:", total_amount_2020)