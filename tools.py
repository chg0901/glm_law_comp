def get_company_info(key: str, value:str, need_fields: list[str] = None):
    '''
    key: str  可以为 公司名称、公司简称、公司代码
    value: str
    need_fields:list[str] [公司名称,公司简称,英文名称,关联证券,公司代码,曾用简称,所属市场,所属行业,成立日期,上市日期,法人代表,总经理,董秘,邮政编码,注册地址,办公地址,联系电话,传真,官方网址,电子邮箱,入选指数,主营业务,经营范围,机构简介,每股面值,首发价格,首发募资净额,首发主承销商]
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/get_company_info"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    if need_fields is None: need_fields = []
    data = {"query_conds": {key: value}, "need_fields": need_fields}

    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()

# print(get_company_info(key="公司名称", value="上海妙可蓝多食品科技股份有限公司", need_fields=["公司简称", "注册地址"]))

def get_company_register(company_name: str, need_fields: list[str] = None):
    '''
    company_name: str
    need_fields:list[str] [公司名称,登记状态,统一社会信用代码,法定代表人,注册资本,成立日期,企业地址,联系电话,联系邮箱,注册号,组织机构代码,参保人数,行业一级,行业二级,行业三级,曾用名,企业简介,经营范围]
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/get_company_register"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    if need_fields is None: need_fields = []
    data = {"query_conds": {"公司名称": company_name}, "need_fields": need_fields}

    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()

# print(get_company_register(company_name="天能电池集团股份有限公司", need_fields=["法定代表人", "联系电话"]))
def get_company_register_name(social_code: str):
    '''
    company_name: str
    need_fields:list[str] [公司名称,登记状态,统一社会信用代码,法定代表人,注册资本,成立日期,企业地址,联系电话,联系邮箱,注册号,组织机构代码,参保人数,行业一级,行业二级,行业三级,曾用名,企业简介,经营范围]
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/get_company_register_name"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }

    data = {"query_conds": {"统一社会信用代码": social_code}, "need_fields": []}

    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()

# print(get_company_register_name(social_code="913305007490121183"))

def get_sub_company_info(sub_company_name: str, need_fields: list[str] = None):
    '''
    company_name: str
    need_fields:list[str] [关联上市公司全称,上市公司关系,上市公司参股比例,上市公司投资金额,公司名称]
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/get_sub_company_info"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    if need_fields is None: need_fields = []
    data = {"query_conds": {"公司名称": sub_company_name}, "need_fields": need_fields}

    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()

# print(get_sub_company_info(sub_company_name="上海爱斯达克汽车空调系统有限公司", need_fields=["关联上市公司全称", "上市公司参股比例"]))

def get_sub_company_info_list(parent_company_name: str, need_fields: list[str] = None):
    '''
    parent_company_name: str
    need_fields:list[str] [关联上市公司全称,上市公司关系,上市公司参股比例,上市公司投资金额,公司名称]
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/get_sub_company_info_list"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    if need_fields is None: need_fields = []
    data = {"query_conds": {"关联上市公司全称": parent_company_name}, "need_fields": need_fields}

    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()
# print(get_sub_company_info_list(parent_company_name="上海航天汽车机电股份有限公司", need_fields=["上市公司投资金额"]))
def get_legal_document(legal_num: str, need_fields: list[str] = None):
    '''
    parent_company_name: str
    need_fields:list[str] [关联公司,标题,案号,文书类型,原告,被告,原告律师事务所,被告律师事务所,案由,涉案金额,判决结果,日期,文件名]
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/get_legal_document"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    if need_fields is None: need_fields = []
    data = {"query_conds": {"案号": legal_num}, "need_fields": need_fields}

    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()

# print(get_legal_document(legal_num="(2019)沪0115民初61975号", need_fields=["关联公司", "标题", "案由"]))

def get_legal_document_list(affiliated_company_name: str, need_fields: list[str] = None):
    '''
    company_name: str
    need_fields:list[str] [关联公司,标题,案号,文书类型,原告,被告,原告律师事务所,被告律师事务所,案由,涉案金额,判决结果,日期,文件名]
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/get_legal_document_list"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    if need_fields is None: need_fields = []
    data = {"query_conds": {"关联公司": affiliated_company_name}, "need_fields": need_fields}

    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()

# print(get_legal_document_list(affiliated_company_name="上海爱斯达克汽车空调系统有限公司", need_fields=["标题", "案号"]))
def get_legal_abstract(legal_num: str, need_fields: list[str] = None):
    '''
    parent_company_name: str
    need_fields:list[str] [文件名,案号,文本摘要]
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/get_legal_abstract"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    if need_fields is None: need_fields = []
    data = {"query_conds": {"案号": legal_num}, "need_fields": need_fields}

    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()

# print(get_legal_abstract(legal_num="（2019）沪0115民初61975号", need_fields=["文件名", "案号"]))
def get_xzgxf_info(legal_num: str, need_fields: list[str] = None):
    '''
    parent_company_name: str
    need_fields:list[str] [限制高消费企业名称,案号,法定代表人,申请人,涉案金额,执行法院,立案日期,限高发布日期]
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/get_xzgxf_info"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    if need_fields is None: need_fields = []
    data = {"query_conds": {"案号": legal_num}, "need_fields": need_fields}

    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()
# print(get_xzgxf_info(legal_num="（2018）鲁0403执1281号", need_fields=["限制高消费企业名称", "执行法院"]))
def get_xzgxf_info_list(company_name: str, need_fields: list[str] = None):
    '''
    parent_company_name: str
    need_fields:list[str] [限制高消费企业名称,案号,法定代表人,申请人,涉案金额,执行法院,立案日期,限高发布日期]
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/get_xzgxf_info_list"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    if need_fields is None: need_fields = []
    data = {"query_conds": {"限制高消费企业名称": company_name}, "need_fields": need_fields}

    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()

# print(get_xzgxf_info_list(company_name="欣水源生态环境科技有限公司", need_fields=["限制高消费企业名称", "执行法院"]))
def get_court_info(court_name: str, need_fields: list[str] = None):
    '''
    company_name: str
    need_fields:list[str] [法院名称,法院负责人,成立日期,法院地址,法院联系电话,法院官网]
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/get_court_info"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    if need_fields is None: need_fields = []
    data = {"query_conds": {"法院名称": court_name}, "need_fields": need_fields}

    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()

# print(get_court_info(court_name="上海市浦东新区人民法院", need_fields=["法院名称", "法院地址"]))
def get_court_code(key: str, value: str, need_fields: list[str] = None):
    '''
    key: str 法院名称、法院代字
    value: str
    need_fields:list[str] [法院名称,行政级别,法院级别,法院代字,区划代码,级别]
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/get_court_code"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    if need_fields is None: need_fields = []
    data = {"query_conds": {key: value}, "need_fields": need_fields}
    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()

# print(get_court_code(key="法院名称", value="上海市浦东新区人民法院", need_fields=["法院名称", "法院级别"]))
def get_lawfirm_info(lawfirm_name: str, need_fields: list[str] = None):
    '''
    lawfirm_name: str
    need_fields:list[str] [律师事务所名称,律师事务所唯一编码,律师事务所负责人,事务所注册资本,事务所成立日期,律师事务所地址,通讯电话,通讯邮箱,律所登记机关]
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/get_lawfirm_info"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    if need_fields is None: need_fields = []
    data = {"query_conds": {"律师事务所名称": lawfirm_name}, "need_fields": need_fields}
    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()

# print(get_lawfirm_info(lawfirm_name="爱德律师事务所", need_fields=["律师事务所名称", "事务所注册资本"]))
def get_lawfirm_log(lawfirm_name: str, need_fields: list[str] = None):
    '''
    lawfirm_name: str
    need_fields:list[str] [律师事务所名称,业务量排名,服务已上市公司,报告期间所服务上市公司违规事件,报告期所服务上市公司接受立案调查]
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/get_lawfirm_log"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    if need_fields is None: need_fields = []
    data = {"query_conds": {"律师事务所名称": lawfirm_name}, "need_fields": need_fields}
    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()

# print(get_lawfirm_log(lawfirm_name="北京市金杜律师事务所", need_fields=["律师事务所名称", "业务量排名"]))

def get_address_info(address: str, need_fields: list[str] = None):
    '''
    address: str
    need_fields:list[str] [地址,省份,城市,区县]
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/get_address_info"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    if need_fields is None: need_fields = []
    data = {"query_conds": {"地址": address}, "need_fields": need_fields}
    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()

# print(get_address_info("西藏自治区那曲地区安多县帕那镇中路13号", need_fields=["省份", "区县"]))
def get_address_code(province: str, city: str, district: str, need_fields: list[str] = None):
    '''
    address: str
    need_fields:list[str] [省份,城市,城市区划代码,区县,区县区划代码]
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/get_address_code"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    if need_fields is None: need_fields = []
    data = {"query_conds": {"省份": province, "城市": city, "区县": district}, "need_fields": need_fields}
    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()

# print(get_address_code(province="西藏自治区", city="拉萨市", district="城关区", need_fields=["城市区划代码", "区县区划代码"]))
def get_temp_info(province: str, city: str, date: str, need_fields: list[str] = None):
    '''
    address: str
    need_fields:list[str] [日期,省份,城市,天气,最高温度,最低温度,湿度]
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/get_temp_info"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    if need_fields is None: need_fields = []
    data = {"query_conds": {"省份": province, "城市": city, "日期": date}, "need_fields": need_fields}
    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()

# print(get_temp_info(province="北京市", city="北京市", date="2020年1月1日", need_fields=["天气", "最高温度"]))
def save_dict_list_to_word(company_name: str, dict_list: str, save_path: str):
    '''
    company_name: str
    dict_list: str
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/save_dict_list_to_word"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    data = {"company_name": company_name, "dict_list": dict_list}
    rsp = requests.post(url, json=data, headers=headers)
    open(save_path, "wb").write(rsp.content)

# dict_list = "{'工商信息': [{'公司名称': '北京碧水源科技股份有限公司', '登记状态': '存续', '统一社会信用代码': '91110000802115985Y', '参保人数': '351', '行业一级': '科学研究和技术服务业', '行业二级': '科技推广和应用服务业', '行业三级': '其他科技推广服务业'}], '子公司信息': [{'关联上市公司全称': '北京碧水源科技股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': 100.0, '上市公司投资金额': '1.06亿', '公司名称': '北京碧海环境科技有限公司'}], '裁判文书': [{'关联公司': '北京碧水源科技股份有限公司', '原告': '四川帝宇水利水电工程有限公司', '被告': '成都碧水源江环保科技有限公司,北京碧水源科技股份有限公司', '案由': '建设工程施工合同纠纷', '涉案金额': 0.0, '日期': Timestamp('2019-07-23 00:00:00')}], '限制高消费': [{'限制高消费企业名称': '南京仙林碧水源污水处理有限公司', '案号': '（2024）苏0113执1601号', '申请人': '苏华建设集团有限公司', '涉案金额': '-', '立案日期': Timestamp('2024-04-07 00:00:00'), '限高发布日期': Timestamp('2024-06-24 00:00:00')}]}"
# save_dict_list_to_word(company_name="北京碧水源科技股份有限公司", dict_list=dict_list, save_path="1.docx")
def get_citizens_sue_citizens(
        原告: str,
        原告性别: str,
        原告生日: str,
        原告民族: str,
        原告工作单位: str,
        原告地址: str,
        原告联系方式: str,
        原告委托诉讼代理人: str,
        原告委托诉讼代理人联系方式: str,
        被告: str,
        被告性别: str,
        被告生日: str,
        被告民族: str,
        被告工作单位: str,
        被告地址: str,
        被告联系方式: str,
        被告委托诉讼代理人: str,
        被告委托诉讼代理人联系方式: str,
        诉讼请求: str,
        事实和理由: str,
        证据: str,
        法院名称: str,
        起诉日期: str,
        ):
    '''公民起诉公民'''

    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/get_citizens_sue_citizens"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    data = {
        '原告': 原告,
        '原告性别': 原告性别,
        '原告生日': 原告生日,
        '原告民族': 原告民族,
        '原告工作单位': 原告工作单位,
        '原告地址': 原告地址,
        '原告联系方式': 原告联系方式,
        '原告委托诉讼代理人': 原告委托诉讼代理人,
        '原告委托诉讼代理人联系方式': 原告委托诉讼代理人联系方式,
        '被告': 被告,
        '被告性别': 被告性别,
        '被告生日': 被告生日,
        '被告民族': 被告民族,
        '被告工作单位': 被告工作单位,
        '被告地址': 被告地址,
        '被告联系方式': 被告联系方式,
        '被告委托诉讼代理人': 被告委托诉讼代理人,
        '被告委托诉讼代理人联系方式': 被告委托诉讼代理人联系方式,
        '诉讼请求': 诉讼请求,
        '事实和理由': 事实和理由,
        '证据': 证据,
        '法院名称': 法院名称,
        '起诉日期': 起诉日期}
    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()

# print(get_citizens_sue_citizens(原告='张三', 原告性别='男', 原告生日='1976-10-2', 原告民族='汉', 原告工作单位='XXX', 原告地址='中国', 原告联系方式='123456', 原告委托诉讼代理人='李四', 原告委托诉讼代理人联系方式='421313', 被告='王五', 被告性别='女', 被告生日='1975-02-12', 被告民族='汉', 被告工作单位='YYY', 被告地址='江苏', 被告联系方式='56354321', 被告委托诉讼代理人='赵六', 被告委托诉讼代理人联系方式='09765213', 诉讼请求='AA纠纷', 事实和理由='上诉', 证据='PPPPP', 法院名称='最高法', 起诉日期='2012-09-08'))

def get_company_sue_citizens(
        原告: str,
        原告地址: str,
        原告法定代表人: str,
        原告联系方式: str,
        原告委托诉讼代理人: str,
        原告委托诉讼代理人联系方式: str,
        被告: str,
        被告性别: str,
        被告生日: str,
        被告民族: str,
        被告工作单位: str,
        被告地址: str,
        被告联系方式: str,
        被告委托诉讼代理人: str,
        被告委托诉讼代理人联系方式: str,
        诉讼请求: str,
        事实和理由: str,
        证据: str,
        法院名称: str,
        起诉日期: str,
):
    '''公司起诉公民'''
    import requests

    url = f"https://comm.chatglm.cn/law_api/s1_b/get_company_sue_citizens"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    data = {
        '原告': 原告,
        '原告地址': 原告地址,
        '原告法定代表人': 原告法定代表人,
        '原告联系方式': 原告联系方式,
        '原告委托诉讼代理人': 原告委托诉讼代理人,
        '原告委托诉讼代理人联系方式': 原告委托诉讼代理人联系方式,
        '被告': 被告,
        '被告性别': 被告性别,
        '被告生日': 被告生日,
        '被告民族': 被告民族,
        '被告工作单位': 被告工作单位,
        '被告地址': 被告地址,
        '被告联系方式': 被告联系方式,
        '被告委托诉讼代理人': 被告委托诉讼代理人,
        '被告委托诉讼代理人联系方式': 被告委托诉讼代理人联系方式,
        '诉讼请求': 诉讼请求,
        '事实和理由': 事实和理由,
        '证据': 证据,
        '法院名称': 法院名称,
        '起诉日期': 起诉日期,
    }
    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()

# print(get_company_sue_citizens(原告= '上海公司', 原告地址= '上海', 原告法定代表人= '张三', 原告联系方式= '872638', 原告委托诉讼代理人= 'B律师事务所', 原告委托诉讼代理人联系方式= '5678900', 被告= '王五', 被告性别= '女', 被告生日= '1975-02-12', 被告民族= '汉', 被告工作单位= 'YYY', 被告地址= '江苏', 被告联系方式= '56354321', 被告委托诉讼代理人= '赵六', 被告委托诉讼代理人联系方式= '09765213', 诉讼请求= 'AA纠纷', 事实和理由= '上诉', 证据= 'PPPPP', 法院名称= '最高法', 起诉日期= '2012-09-08'))

def get_citizens_sue_company(
        原告: str,
        原告性别: str,
        原告生日: str,
        原告民族: str,
        原告工作单位: str,
        原告地址: str,
        原告联系方式: str,
        原告委托诉讼代理人: str,
        原告委托诉讼代理人联系方式: str,
        被告: str,
        被告地址: str,
        被告法定代表人: str,
        被告联系方式: str,
        被告委托诉讼代理人: str,
        被告委托诉讼代理人联系方式: str,
        诉讼请求: str,
        事实和理由: str,
        证据: str,
        法院名称: str,
        起诉日期: str,
):
    '''公民起诉公司'''
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/get_citizens_sue_company"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    data = {
        '原告': 原告,
        '原告性别': 原告性别,
        '原告生日': 原告生日,
        '原告民族': 原告民族,
        '原告工作单位': 原告工作单位,
        '原告地址': 原告地址,
        '原告联系方式': 原告联系方式,
        '原告委托诉讼代理人': 原告委托诉讼代理人,
        '原告委托诉讼代理人联系方式': 原告委托诉讼代理人联系方式,
        '被告': 被告,
        '被告地址': 被告地址,
        '被告法定代表人': 被告法定代表人,
        '被告联系方式': 被告联系方式,
        '被告委托诉讼代理人': 被告委托诉讼代理人,
        '被告委托诉讼代理人联系方式': 被告委托诉讼代理人联系方式,
        '诉讼请求': 诉讼请求,
        '事实和理由': 事实和理由,
        '证据': 证据,
        '法院名称': 法院名称,
        '起诉日期': 起诉日期,
    }
    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()
# print(get_citizens_sue_company(原告='张三', 原告性别='男', 原告生日='1976-10-2', 原告民族='汉', 原告工作单位='XXX', 原告地址='中国', 原告联系方式='123456', 原告委托诉讼代理人='李四', 原告委托诉讼代理人联系方式='421313', 被告='王五公司', 被告地址='公司地址', 被告法定代表人='赵四', 被告联系方式='98766543', 被告委托诉讼代理人='C律师事务所', 被告委托诉讼代理人联系方式='425673398', 诉讼请求='AA纠纷', 事实和理由='上诉', 证据='PPPPP', 法院名称='最高法', 起诉日期='2012-09-08'))

def get_company_sue_company(
        原告: str,
        原告地址: str,
        原告法定代表人: str,
        原告联系方式: str,
        原告委托诉讼代理人: str,
        原告委托诉讼代理人联系方式: str,
        被告: str,
        被告地址: str,
        被告法定代表人: str,
        被告联系方式: str,
        被告委托诉讼代理人: str,
        被告委托诉讼代理人联系方式: str,
        诉讼请求: str,
        事实和理由: str,
        证据: str,
        法院名称: str,
        起诉日期: str,
):
    '''公司起诉公司'''
    import requests

    url = f"https://comm.chatglm.cn/law_api/s1_b/get_company_sue_company"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    data = {
        '原告': 原告,
        '原告地址': 原告地址,
        '原告法定代表人': 原告法定代表人,
        '原告联系方式': 原告联系方式,
        '原告委托诉讼代理人': 原告委托诉讼代理人,
        '原告委托诉讼代理人联系方式': 原告委托诉讼代理人联系方式,
        '被告': 被告,
        '被告地址': 被告地址,
        '被告法定代表人': 被告法定代表人,
        '被告联系方式': 被告联系方式,
        '被告委托诉讼代理人': 被告委托诉讼代理人,
        '被告委托诉讼代理人联系方式': 被告委托诉讼代理人联系方式,
        '诉讼请求': 诉讼请求,
        '事实和理由': 事实和理由,
        '证据': 证据,
        '法院名称': 法院名称,
        '起诉日期': 起诉日期,
    }
    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()

# print(get_company_sue_company(原告='上海公司', 原告地址='上海', 原告法定代表人='张三', 原告联系方式='872638', 原告委托诉讼代理人='B律师事务所', 原告委托诉讼代理人联系方式='5678900', 被告='王五公司', 被告地址='公司地址', 被告法定代表人='赵四', 被告联系方式='98766543', 被告委托诉讼代理人='C律师事务所', 被告委托诉讼代理人联系方式='425673398', 诉讼请求='AA纠纷', 事实和理由='上诉', 证据='PPPPP', 法院名称='最高法', 起诉日期='2012-09-08'))

def get_sum(nums: list[int] | list[float] | list[str]):
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/get_sum"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    rsp = requests.post(url, json=nums, headers=headers)
    return rsp.json()
# print(get_sum(nums=[1, 2, 3, 4, 5]))

def get_rank(keys: list[any], values: list[float], is_desc: bool = False):
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/rank"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    data = {
        'keys': keys,
        'values': values,
        'is_desc': is_desc
    }
    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()

# print(get_rank(keys=["a", "b", "c"], values=[2, 1, 3] ))