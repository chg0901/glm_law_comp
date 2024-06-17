def get_company_info(
    company_name: list[str]) -> list[dict]:
    '''根据公司名称获得该公司如下基本信息[公司名称,公司简称,英文名称,关联证券,公司代码,曾用简称,所属市场,所属行业,上市日期,法人代表,总经理,董秘,邮政编码,注册地址,办公地址,联系电话,传真,官方网址,电子邮箱,入选指数,主营业务,经营范围,机构简介,每股面值,首发价格,首发募资净额,首发主承销商]
        Args:
        company_name (list[str]): 公司名称
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/get_company_info"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    
    data = {
        "company_name": company_name
    }

    rsp = requests.post(url, json=data, headers=headers)
    if len(company_name) == 1:
        return [rsp.json()]
    else: 
        return rsp.json()

def search_company_name_by_info(
    key: str,
    value: list[str]) -> list[dict]:
    '''根据公司基本信息某个字段是某个值来查询具体的公司名称
        Args:
        key(str):公司基本信息字段
        value(str):字段的值
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/search_company_name_by_info"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    data = {
        "key": key,
        'value': value
    }

    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()

def get_company_register(
    company_name: list[str]) -> list[dict]:
    '''根据公司名称获得该公司如下注册信息[公司名称,登记状态,统一社会信用代码,注册资本,成立日期,省份,城市,区县,注册号,组织机构代码,参保人数,企业类型,曾用名]
    Args:
    company_name(list[str]):公司名称
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/get_company_register"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }

    data = {
        "company_name": company_name
    }

    rsp = requests.post(url, json=data, headers=headers)
    if len(company_name) == 1:
        return [rsp.json()]
    else: 
        return rsp.json()


def search_company_name_by_register(
    key: str,
    value: str) -> dict:
    '''根据公司注册信息某个字段是某个值来查询具体的公司名称公司注册信息如下[公司名称,登记状态,统一社会信用代码,注册资本,成立日期,省份,城市,区县,注册号,组织机构代码,参保人数,企业类型,曾用名]
        Args:
        key(str):公司注册信息字段
        value(str):字段的值
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/search_company_name_by_register"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    data = {
        "key": key,
        'value': value
    }

    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()


def get_sub_company_info(
    company_name: list[str]) -> list[dict]:
    '''根据子公司名称获得该公司母公司信息
    Args:
    company_name(list[str]):子公司名称
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/get_sub_company_info"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }

    data = {
        "company_name": company_name
    }

    rsp = requests.post(url, json=data, headers=headers)
    if len(company_name) == 1:
        return [rsp.json()]
    else: 
        return rsp.json()


def search_company_name_by_sub_info(
    key: str,
    value: str) -> list[dict]:
    '''根据母公司信息某个字段是某个值查询子公司名称
        Args:
        key(str):母公司信息某个字段
        value(str):母公司信息字段值
    '''
    url = f"https://comm.chatglm.cn/law_api/search_company_name_by_sub_info"
    import requests
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    data = {
        "key": key,
        'value': value
    }
    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()


def get_legal_document(
    case_num: list[str]) -> list[dict]:
    '''根据案号获得该案所有基本信息
    Args:
    case_num(list[str]):案号，如果案号中有括号则只识别英文括号
    '''
    import requests
    url = f"https://comm.chatglm.cn/law_api/get_legal_document"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }

    data = {
        "case_num": case_num
    }

    rsp = requests.post(url, json=data, headers=headers)
    if len(case_num) == 1:
        return [rsp.json()]
    else:
        return rsp.json()


def search_case_num_by_legal_document(
    key: str,
    value: str) -> dict:
    '''根据法律文书某个字段是某个值来查询具体的案号
        Args:
        key(str):法律文书某个字段
        value(str):法律文书字段值
    '''
    url = f"https://comm.chatglm.cn/law_api/search_case_num_by_legal_document"
    import requests
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer D8298F2101BDBC2D2E91CE24D58792B5FA51CAD7A0F5A27B'
    }
    data = {
        "key": key,
        'value': value
    }

    rsp = requests.post(url, json=data, headers=headers)
    return rsp.json()