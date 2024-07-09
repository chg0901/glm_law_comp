TABLE_PROMPT = """
请根据问题中提供的信息以及数据表属性，判断回答问题所需要的数据表（按照查阅数据表顺序返回）。
问题：{question}
----
table 1: {{
    名称: company_info
    属性值: 公司名称,公司简称,英文名称,关联证券,公司代码,曾用简称,所属市场,所属行业,成立日期,上市日期,法人代表,总经理,董秘,邮政编码,注册地址,办公地址,联系电话,传真,官方网址,电子邮箱,入选指数,主营业务,经营范围,机构简介,每股面值,首发价格,首发募资净额,首发主承销商
    }}

table 2: {{
    名称: company_register
    属性值: 公司名称,登记状态,统一社会信用代码,法定代表人,注册资本,成立日期,企业地址,联系电话,联系邮箱,注册号,组织机构代码,参保人数,行业一级,行业二级,行业三级,曾用名,企业简介,经营范围
    }}

table 3: {{
    名称: sub_company_info
    属性值: 关联上市公司全称,上市公司关系,上市公司参股比例,上市公司投资金额,公司名称
    }}

table 4: {{
    名称: legal_document
    属性值: 关联公司,标题,案号,文书类型,原告,被告,原告律师事务所,被告律师事务所,案由,涉案金额,判决结果(包含法院名称),日期,文件名
}}

table 5: {{
    名称: legal_abstract
    属性值: 文件名,案号,文本摘要
}}

table 6: {{
    名称: xzgxf_info
    属性值: 限制高消费企业名称,案号,法定代表人,申请人,涉案金额,执行法院,立案日期,限高发布日期
}}

table 7: {{
    名称: court_info
    属性值: 法院名称,法院负责人,成立日期,法院地址,法院联系电话,法院官网
}}

table 8: {{
    名称: court_code
    属性值: 法院名称,行政级别,法院级别,法院代字,区划代码,级别
}}

table 9: {{
    名称: lawfirm_info
    属性值: 律师事务所名称,律师事务所唯一编码,律师事务所负责人,事务所注册资本,事务所成立日期,律师事务所地址,通讯电话,通讯邮箱,律所登记机关
}}

table 10: {{
    名称: lawfirm_log
    属性值: 律师事务所名称,业务量排名,服务已上市公司,报告期间所服务上市公司违规事件,报告期所服务上市公司接受立案调查
}}

table 11: {{
    名称: address_info
    属性值: 地址,省份,城市,区县
}}

table 12: {{
    名称: address_code
    属性值: 省份,城市,城市区划代码,区县,区县区划代码
}}

table 13: {{
    名称: temp_info
    属性值: 日期,省份,城市,天气,最高温度,最低温度,湿度
}}
----
请按照以下json格式进行输出，可以被Python json.loads函数解析。不回答问题，不作任何解释，不输出其他任何信息。
```json
{{
    [str]
}}
``` 
"""
UTILS_PROMPT = """
请根据问题判断回答问题是否需要table中新的函数。
问题：{question}
----
table 1: {{
    名称: get_sum
    描述: 求和，可以对传入的int、float、str数组进行求和，str数组只能转换字符串里的千万亿，如"1万"
    }}
table 2: {{
    名称: get_rank
    描述: 排序，返回按照values排序的keys
    }}
table 3: {{
    名称: save_dict_list_to_word
    描述: 通过传入结构化信息，制作生成公司数据报告
    }}
table 4: {{
    名称: get_citizens_sue_citizens
    描述: 民事起诉状(公民起诉公民)
    }}
table 5: {{
    名称: get_company_sue_citizens
    描述: 民事起诉状(公司起诉公民)
    }}
table 6: {{
    名称: get_citizens_sue_company
    描述: 民事起诉状(公民起诉公司)
    }}
table 7: {{
    名称: get_company_sue_company
    描述: 民事起诉状(公司起诉公司)
    }}
----
请按照以下json格式进行输出，可以被Python json.loads函数解析。如果没有需要使用的函数请返回json格式的空列表。不回答问题，不作任何解释，不输出其他任何信息。
```json
{{
    [str]
}}
"""
WRITER_PROMPT = """
# 任务 #
1.  如果问题可以被下方函数解决，请你先从functions模块中导入函数再解决任务，最后结果要使用print函数打印出来。
2.  请你分步执行代码。
3.  请你把代码放在```python```代码框中，方便我执行你的代码，把代码的运行结果用print方法打印出来。
4.  如果我执行的结果是正确的，请结合结果与问题返回相应的答案。

# 你可以使用的函数 #
"""

WRITER_PROMPT_0 = """
get_company_info(key: str, value:str, need_fields: Optional[str] = None)
根据上市公司名称、简称或代码查找上市公司信息
key可以选择的字段有[公司名称, 公司简称, 公司代码]
need_fields可以选择的字段有[公司名称,公司简称,英文名称,关联证券,公司代码,曾用简称,所属市场,所属行业,成立日期,上市日期,法人代表,总经理,董秘,邮政编码,注册地址,办公地址,联系电话,传真,官方网址,电子邮箱,入选指数,主营业务,经营范围,机构简介,每股面值,首发价格,首发募资净额,首发主承销商]

例如：
    运行：print(get_company_info(key="公司名称", value="上海妙可蓝多食品科技股份有限公司", need_fields=["公司简称", "注册地址"]))
    输出：{'公司简称': '妙可蓝多', '注册地址': '上海市奉贤区工业路899号8幢'}
"""
WRITER_PROMPT_1 = """
get_company_register(company_name: str, need_fields: Optional[str] = None)
根据公司名称查询工商信息
need_fields可以选择的字段有[公司名称,登记状态,统一社会信用代码,法定代表人,注册资本,成立日期,企业地址,联系电话,联系邮箱,注册号,组织机构代码,参保人数,行业一级,行业二级,行业三级,曾用名,企业简介,经营范围]
例如：
    运行：print(get_company_register(company_name="天能电池集团股份有限公司", need_fields=["法定代表人", "联系电话"]))
    输出：{'法定代表人': '杨建芬', '联系电话': '0572-6029388'}

get_company_register_name(social_code: str)
根据统一社会信用代码查询公司名称
例如：
    运行：print(get_company_register_name(social_code="913305007490121183"))
    输出：{'公司名称': '天能电池集团股份有限公司'}
"""
WRITER_PROMPT_2 = """
get_sub_company_info(sub_company_name: str, need_fields: Optional[str] = None)
根据被投资的子公司名称获得投资该公司的上市公司、投资比例、投资金额等信息
need_fields可以选择的字段有[关联上市公司全称,上市公司关系,上市公司参股比例,上市公司投资金额,公司名称]
例如：
    运行：print(get_sub_company_info(sub_company_name="上海爱斯达克汽车空调系统有限公司", need_fields=["关联上市公司全称", "上市公司参股比例"]))
    输出：{'关联上市公司全称': '上海航天汽车机电股份有限公司', '上市公司参股比例': '87.5'}

get_sub_company_info_list(parent_company_name: str, need_fields: Optional[str] = None)
根据上市公司（母公司）的名称查询该公司投资的所有子公司信息list
need_fields可以选择的字段有[关联上市公司全称,上市公司关系,上市公司参股比例,上市公司投资金额,公司名称]
例如：
    运行：print(get_sub_company_info_list(parent_company_name="上海航天汽车机电股份有限公司", need_fields=["上市公司投资金额"]))
    输出：[{'上市公司投资金额': '8800.00万'}, {'上市公司投资金额': '1.19亿'}, {'上市公司投资金额': '3400.00万'}, {'上市公司投资金额': '5600.00万'}, {'上市公司投资金额': '8700.00万'}, {'上市公司投资金额': '1296.99万'}, {'上市公司投资金额': '100.00万'}, {'上市公司投资金额': ''}, {'上市公司投资金额': '2.50亿'}, {'上市公司投资金额': '7000.00万'}, {'上市公司投资金额': '1.26亿'}, {'上市公司投资金额': '100.00万'}, {'上市公司投资金额': '8.54亿'}, {'上市公司投资金额': '3.41亿'}, {'上市公司投资金额': '2040.00万'}, {'上市公司投资金额': '1600.00万'}, {'上市公司投资金额': '2620.00万'}, {'上市公司投资金额': '1.45亿'}]
"""
REF_PROMPT_2 = """
get_sub_company_info(sub_company_name: str, need_fields: Optional[str] = None)
根据被投资的子公司名称获得投资该公司的上市公司、投资比例、投资金额等信息
返回如下信息[关联上市公司全称,上市公司关系,上市公司参股比例,上市公司投资金额,公司名称]
get_sub_company_info_list(parent_company_name: str, need_fields: Optional[str] = None)
根据上市公司（母公司）的名称查询该公司投资的所有子公司信息list
"""
WRITER_PROMPT_3 = """
get_legal_document(legal_num: str, need_fields: Optional[str] = None)
根据案号查询裁判文书相关信息
need_fields可以选择的字段有[关联公司,标题,案号,文书类型,原告,被告,原告律师事务所,被告律师事务所,案由,涉案金额,判决结果,日期,文件名]
例如：
    运行：print(get_legal_document(legal_num="(2019)沪0115民初61975号", need_fields=["关联公司", "标题"]))
    输出：{'关联公司': '上海爱斯达克汽车空调系统有限公司', '标题': '上海爱斯达克汽车空调系统有限公司与上海逸测检测技术服务有限公司服务合同纠纷一审民事判决书'}

get_legal_document_list(company_name: str, need_fields: Optional[str] = None)
根据关联公司查询所有裁判文书相关信息list
被起诉人即为被告
need_fields可以选择的字段有[关联公司,标题,案号,文书类型,原告,被告,原告律师事务所,被告律师事务所,案由,涉案金额,判决结果,日期,文件名]
例如：
    运行：print(get_legal_document_list(affiliated_company_name="上海爱斯达克汽车空调系统有限公司", need_fields=["标题", "案号"]))
    输出：[{'标题': '上海爱斯达克汽车空调系统有限公司与上海逸测检测技术服务有限公司服务合同纠纷一审民事判决书', '案号': '(2019)沪0115民初61975号'}, {'标题': '吴某某与上海爱斯达克汽车空调系统有限公司追索劳动报酬纠纷一审民事判决书', '案号': '(2019)沪0115民初91149号'}, {'标题': '上海贝众汽车零部件有限公司与上海爱斯达克汽车空调系统有限公司技术委托开发合同纠纷民事一审案件民事判决书', '案号': '(2020)沪0115民初3857号'}]
"""

WRITER_PROMPT_4 = """
get_legal_abstract(legal_num: str, need_fields: Optional[str] = None)
根据案号查询文本摘要
need_fields可以选择的字段有[文件名,案号,文本摘要]
例如：
    运行：print(get_legal_abstract(legal_num="（2019）沪0115民初61975号", need_fields=["文件名", "案号"]))
    输出：{'文件名': '（2019）沪0115民初61975号.txt', '案号': '（2019）沪0115民初61975号'}
"""

WRITER_PROMPT_5 = """
get_xzgxf_info(legal_num: str, need_fields: Optional[str] = None)
根据案号查询限制高消费相关信息
need_fields可以选择的字段有[限制高消费企业名称,案号,法定代表人,申请人,涉案金额,执行法院,立案日期,限高发布日期]
例如：
    运行：print(get_xzgxf_info(legal_num="（2018）鲁0403执1281号", need_fields=["限制高消费企业名称", "执行法院"]))
    输出：{'限制高消费企业名称': '枣庄西能新远大天然气利用有限公司', '执行法院': '山东省枣庄市薛城区人民法院'}

get_xzgxf_info_list(company_name: str, need_fields: Optional[str] = None)
根据企业名称查询所有限制高消费相关信息list
need_fields可以选择的字段有[限制高消费企业名称,案号,法定代表人,申请人,涉案金额,执行法院,立案日期,限高发布日期]
例如：
    运行：print(get_xzgxf_info_list(company_name="欣水源生态环境科技有限公司", need_fields=["限制高消费企业名称", "执行法院"]))
    输出：{'限制高消费企业名称': '欣水源生态环境科技有限公司', '执行法院': '贵州省黔南布依族苗族自治州惠水县人民法院'}
"""

WRITER_PROMPT_6 = """
get_court_info(court_name: str, need_fields: Optional[str] = None)
根据法院名称查询法院名录相关信息
need_fields可以选择的字段有[法院名称,法院负责人,成立日期,法院地址,法院联系电话,法院官网]
例如：
    运行：print(get_court_info(court_name="上海市浦东新区人民法院", need_fields=["法院名称", "法院地址"]))
    输出：{'法院名称': '上海市浦东新区人民法院', '法院地址': '上海市浦东新区丁香路611号'}
"""

WRITER_PROMPT_7 = """
get_court_code(key: str, value: str, need_fields: Optional[str] = None)
根据法院名称或者法院代字查询法院代字等相关数据
need_fields可以选择的字段有[法院名称,行政级别,法院级别,法院代字,区划代码,级别]
例如：
    运行：print(get_court_code(key="法院名称", value="上海市浦东新区人民法院", need_fields=["法院名称", "法院级别"]))
    输出：{'法院名称': '上海市浦东新区人民法院', '法院级别': '基层法院'}
"""

WRITER_PROMPT_8="""
get_lawfirm_info(lawfirm_name: str, need_fields: Optional[str] = None)
根据律师事务所查询律师事务所名录
need_fields可以选择的字段有[律师事务所名称,律师事务所唯一编码,律师事务所负责人,事务所注册资本,事务所成立日期,律师事务所地址,通讯电话,通讯邮箱,律所登记机关]
例如：
    运行：print(get_lawfirm_info(lawfirm_name="爱德律师事务所", need_fields=["律师事务所名称", "事务所注册资本"]))
    输出：{'律师事务所名称': '爱德律师事务所', '事务所注册资本': '10万元人民币'}
"""

WRITER_PROMPT_9 = """
get_lawfirm_log(lawfirm_name: str, need_fields: Optional[str] = None)
根据律师事务所查询律师事务所统计数据
need_fields可以选择的字段有[律师事务所名称,业务量排名,服务已上市公司,报告期间所服务上市公司违规事件,报告期所服务上市公司接受立案调查]
例如：
    运行：print(get_lawfirm_log(lawfirm_name="北京市金杜律师事务所", need_fields=["律师事务所名称", "业务量排名"]))
    输出：{'律师事务所名称': '北京市金杜律师事务所', '业务量排名': '2'}
"""

WRITER_PROMPT_10 = """
get_address_info(address: str, need_fields: Optional[str] = None)
根据地址查该地址对应的省份城市区县
need_fields可以选择的字段有[地址,省份,城市,区县]
例如：
    运行：print(get_address_info("西藏自治区那曲地区安多县帕那镇中路13号", need_fields=["省份", "区县"]))
    输出：{'省份': '西藏自治区', '区县': '安多县'}
"""

WRITER_PROMPT_11 = """
get_address_code(province: str, city: str, district: str, need_fields: Optional[str] = None)
根据省市区查询区划代码
need_fields可以选择的字段有[省份,城市,城市区划代码,区县,区县区划代码]
例如：
    运行：print(get_address_code(province="西藏自治区", city="拉萨市", district="城关区", need_fields=["城市区划代码", "区县区划代码"]))
    输出：{'城市区划代码': '540100000000', '区县区划代码': '540102000000'}
"""

WRITER_PROMPT_12 = """
get_temp_info(province: str, city: str, data: str, need_fields: Optional[str] = None)
根据日期及省份城市查询天气相关信息
need_fields可以选择的字段有[日期,省份,城市,天气,最高温度,最低温度,湿度]
例如：
    运行：print(get_temp_info(province="北京市", city="北京市", date="2020年1月1日", need_fields=["天气", "最高温度"]))
    输出：{'天气': '晴', '最高温度': '11'}
"""

GET_SUM = """
get_sum(nums: list[int] | list[float] | list[str])
求和，可以对传入的int、float、str数组进行求和，str数组只能转换字符串里的千万亿，如"1万"
例如：
    运行：print(get_sum(nums=[1, 2, 3, 4, 5])
    输出：15
"""

RANK = """
get_rank
排序接口，返回按照values排序的keys
例如：
    运行：print(get_rank(keys=["a", "b", "c"], values=[2, 1, 3]))
    输出：['b', 'a', 'c']
"""

SAVE_DICT_LIST2WORD = """
save_dict_list_to_word(company_name: str, dict_list: str, save_path: str)
通过传入结构化信息，制作生成公司数据报告
例如：
dict_list = "{'工商信息': [{'公司名称': '北京碧水源科技股份有限公司', '登记状态': '存续', '统一社会信用代码': '91110000802115985Y', '参保人数': '351', '行业一级': '科学研究和技术服务业', '行业二级': '科技推广和应用服务业', '行业三级': '其他科技推广服务业'}], '子公司信息': [{'关联上市公司全称': '北京碧水源科技股份有限公司', '上市公司关系': '子公司', '上市公司参股比例': 100.0, '上市公司投资金额': '1.06亿', '公司名称': '北京碧海环境科技有限公司'}], '裁判文书': [{'关联公司': '北京碧水源科技股份有限公司', '原告': '四川帝宇水利水电工程有限公司', '被告': '成都碧水源江环保科技有限公司,北京碧水源科技股份有限公司', '案由': '建设工程施工合同纠纷', '涉案金额': 0.0, '日期': Timestamp('2019-07-23 00:00:00')}], '限制高消费': [{'限制高消费企业名称': '南京仙林碧水源污水处理有限公司', '案号': '（2024）苏0113执1601号', '申请人': '苏华建设集团有限公司', '涉案金额': '-', '立案日期': Timestamp('2024-04-07 00:00:00'), '限高发布日期': Timestamp('2024-06-24 00:00:00')}]}"
save_dict_list_to_word(company_name="北京碧水源科技股份有限公司", dict_list=dict_list, save_path="1.docx")
"""

CITIZENS_SUE_CITIZENS = """
get_citizens_sue_citizens(
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
民事起诉状(公民起诉公民)
例如：
    运行：
    print(get_citizens_sue_citizens(原告='张三', 原告性别='男', 原告生日='1976-10-2', 原告民族='汉', 原告工作单位='XXX', 原告地址='中国', 原告联系方式='123456', 原告委托诉讼代理人='李四', 原告委托诉讼代理人联系方式='421313', 被告='王五', 被告性别='女', 被告生日='1975-02-12', 被告民族='汉', 被告工作单位='YYY', 被告地址='江苏', 被告联系方式='56354321', 被告委托诉讼代理人='赵六', 被告委托诉讼代理人联系方式='09765213', 诉讼请求='AA纠纷', 事实和理由='上诉', 证据='PPPPP', 法院名称='最高法', 起诉日期='2012-09-08'))
    输出：
    民事起诉状（公民起诉公民）
    原告：张三，性别：男，出生日期：1976-10-2，民族：汉，工作单位：XXX，地址：中国，联系方式：123456。
    原告委托诉讼代理人：李四，联系方式：421313。
    被告：王五，性别：女，出生日期：1975-02-12，民族：汉，工作单位：YYY，地址：江苏，联系方式：56354321。
    被告委托诉讼代理人：赵六，联系方式：09765213。
    诉讼请求：
    AA纠纷
    事实和理由：
    上诉
    证据和证据来源，证人姓名和住所：
    PPPPP
    此致
    最高法

    附:本起诉状副本x份

    起诉人(签名)
    2012-09-08
"""
COMPANY_SUE_CITIZENS = """
get_company_sue_citizens(
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
民事起诉状(公司起诉公民)
例如：
    运行：
    print(get_company_sue_citizens(原告= '上海公司', 原告地址= '上海', 原告法定代表人= '张三', 原告联系方式= '872638', 原告委托诉讼代理人= 'B律师事务所', 原告委托诉讼代理人联系方式= '5678900', 被告= '王五', 被告性别= '女', 被告生日= '1975-02-12', 被告民族= '汉', 被告工作单位= 'YYY', 被告地址= '江苏', 被告联系方式= '56354321', 被告委托诉讼代理人= '赵六', 被告委托诉讼代理人联系方式= '09765213', 诉讼请求= 'AA纠纷', 事实和理由= '上诉', 证据= 'PPPPP', 法院名称= '最高法', 起诉日期= '2012-09-08'))
    输出：
    民事起诉状（公司起诉公民）
    原告：上海公司，地址：上海。法定代表人（负责人）：张三，联系方式：872638。
    原告委托诉讼代理人：B律师事务所，联系方式：5678900。
    被告：王五，性别：女，出生日期：1975-02-12，民族：汉，工作单位：YYY，地址：江苏，联系方式：56354321。
    被告委托诉讼代理人：赵六，联系方式：09765213。
    诉讼请求：
    AA纠纷
    事实和理由：
    上诉
    证据和证据来源，证人姓名和住所：
    PPPPP
    此致
    最高法

    附:本起诉状副本x份

    起诉人(签名)
    2012-09-08
"""
CITIZENS_SUE_COMPANY = """
get_citizens_sue_company(
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
民事起诉状(公民起诉公司)
例如：
    运行：
    print(get_citizens_sue_company(原告='张三', 原告性别='男', 原告生日='1976-10-2', 原告民族='汉', 原告工作单位='XXX', 原告地址='中国', 原告联系方式='123456', 原告委托诉讼代理人='李四', 原告委托诉讼代理人联系方式='421313', 被告='王五公司', 被告地址='公司地址', 被告法定代表人='赵四', 被告联系方式='98766543', 被告委托诉讼代理人='C律师事务所', 被告委托诉讼代理人联系方式='425673398', 诉讼请求='AA纠纷', 事实和理由='上诉', 证据='PPPPP', 法院名称='最高法', 起诉日期='2012-09-08'))
    输出：
    民事起诉状（公民起诉公司）
    原告：张三，性别：男，出生日期：1976-10-2，民族：汉，工作单位：XXX，地址：中国，联系方式：123456。
    原告委托诉讼代理人：李四，联系方式：421313。
    被告：王五公司，地址：公司地址。法定代表人（负责人）：赵四，联系方式：98766543。
    被告委托诉讼代理人：C律师事务所，联系方式：425673398。
    诉讼请求：
    AA纠纷
    事实和理由：
    上诉
    证据和证据来源，证人姓名和住所：
    PPPPP
    此致
    最高法

    附:本起诉状副本x份

    起诉人(签名)
    2012-09-08
"""
COMPANY_SUE_COMPANY = """
get_company_sue_company(
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
民事起诉状(公司起诉公司)
例如：
    运行：
    print(get_company_sue_company(原告='上海公司', 原告地址='上海', 原告法定代表人='张三', 原告联系方式='872638', 原告委托诉讼代理人='B律师事务所', 原告委托诉讼代理人联系方式='5678900', 被告='王五公司', 被告地址='公司地址', 被告法定代表人='赵四', 被告联系方式='98766543', 被告委托诉讼代理人='C律师事务所', 被告委托诉讼代理人联系方式='425673398', 诉讼请求='AA纠纷', 事实和理由='上诉', 证据='PPPPP', 法院名称='最高法', 起诉日期='2012-09-08'))
    输出：
    民事起诉状（公司起诉公司）
    原告：上海公司，地址：上海。法定代表人（负责人）：张三，联系方式：872638。
    原告委托诉讼代理人：B律师事务所，联系方式：5678900。
    被告：王五公司，地址：公司地址。法定代表人（负责人）：赵四，联系方式：98766543。
    被告委托诉讼代理人：C律师事务所，联系方式：425673398。
    诉讼请求：
    AA纠纷
    事实和理由：
    上诉
    证据和证据来源，证人姓名和住所：
    PPPPP
    此致
    最高法

    附:本起诉状副本x份

    起诉人(签名)
    2012-09-08
"""