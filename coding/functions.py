

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


def get_sum(nums: list[int] | list[float] | list[str]):
    import requests
    url = f"https://comm.chatglm.cn/law_api/s1_b/get_sum"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    rsp = requests.post(url, json=nums, headers=headers)
    return rsp.json()


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


