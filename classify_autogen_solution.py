from utils import *
from tqdm import tqdm
from LLM import *

queries = read_jsonl('./question.json')
results = []
table_plan_map = {
    'company_info': 0,
    'company_register': 1,
    'sub_company_info': 2,
    'legal_document': 3,
    'legal_abstract': 4,
    'xzgxf_info': 5,
    'court_info': 6,
    'court_code': 7,
    'lawfirm_info': 8,
    'lawfirm_log': 9,
    'address_info': 10,
    'address_code': 11,
    'temp_info': 12
    }
prompt_list = [
    WRITER_PROMPT_0,
    WRITER_PROMPT_1,
    WRITER_PROMPT_2,
    WRITER_PROMPT_3,
    WRITER_PROMPT_4,
    WRITER_PROMPT_5,
    WRITER_PROMPT_6,
    WRITER_PROMPT_7,
    WRITER_PROMPT_8,
    WRITER_PROMPT_9,
    WRITER_PROMPT_10,
    WRITER_PROMPT_11,
    WRITER_PROMPT_12
]
utils_plan_map = {
    'get_sum': 0,
    'get_rank': 1,
    'save_dict_list_to_word': 2,
    'get_citizens_sue_citizens': 3,
    'get_company_sue_citizens': 4,
    'get_citizens_sue_company': 5,
    'get_company_sue_company': 6,
    }
utils_prompt = [
    GET_SUM,
    RANK,
    SAVE_DICT_LIST2WORD,
    CITIZENS_SUE_CITIZENS,
    COMPANY_SUE_CITIZENS,
    CITIZENS_SUE_COMPANY,
    COMPANY_SUE_COMPANY,
]
for question in tqdm(queries):
    try:
        rsp = LLM(TABLE_PROMPT.format(question=question["question"]))
        fcts = prase_json_from_response(rsp=rsp)
        plan_id = [table_plan_map[fct] for fct in fcts]
        
        prompt = WRITER_PROMPT
        prompt += SIMILAR_RELASIONSHIP_PROMPT
        
        for id in plan_id: prompt += prompt_list[id]
        rsp = LLM(UTILS_PROMPT.format(question=question))
        fcts = prase_json_from_response(rsp=rsp)
        plan_id = [utils_plan_map[fct] for fct in fcts]
        for id in plan_id: prompt += utils_prompt[id]
        result = write_execute(prompt=prompt, question=question["question"])
        results.append(result)

    except Exception as e:
        print(str(question["id"]) + "回答失败")
        results.append("回答失败")

save_answers(queries=queries, results=results)