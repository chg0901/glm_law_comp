from autogen_tools import get_company_register

# 使用get_company_register函数获取河南中敏传感器技术研究院有限公司注册信息
company_register = get_company_register(company_name=["河南中敏传感器技术研究院有限公司"])
# 打印结果
print("河南中敏传感器技术研究院有限公司的组织机构代码为：" + company_register[0]["组织机构代码"])