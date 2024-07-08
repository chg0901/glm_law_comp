from utils import *
from tqdm import tqdm
from LLM import *

queries = read_jsonl('./question.json')
results = []
table_plan_map = {'company_info': 1,'company_register': 1,'sub_company_info': 2,'legal_document': 3}

for query in tqdm(queries):
    try:
        response = LLM(TABLE_PROMPT.format(question=query['question']))
        plan_id = table_plan_map[prase_json_from_response(response)["名称"]]
        result = write_execute(plan_id=plan_id, query=query['question'])
        results.append(result)
    except Exception as e:
        print(str(query["id"]) + "回答失败")
        results.append("回答失败")

save_answers(queries=queries, results=results)