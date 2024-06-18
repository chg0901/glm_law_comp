from utils import *
from tqdm import tqdm
from autogen.coding import LocalCommandLineCodeExecutor
from autogen_tools import *
from autogen import ConversableAgent, AssistantAgent

ZHIPU_API_KEY = get_zhipu_api_key()

llm_config = {
    "config_list": [
        {
    'api_key': ZHIPU_API_KEY,
    "model": "glm-4",
    'base_url': "https://open.bigmodel.cn/api/paas/v4/",
        },
    ],
    "timeout": 60 # 好像没用。。。。
}

functions=[get_company_info,
           search_company_name_by_info,
           get_company_register,
           search_company_name_by_register,
           ch2int,
           get_sub_company_info,
           search_company_name_by_sub_info,
           get_sub_company_info_by_company_info,
           get_legal_document,
           search_case_num_by_legal_document]

executor = LocalCommandLineCodeExecutor(
    timeout=60,
    work_dir="coding",
    functions=functions
)


code_executor_agent = ConversableAgent(
    name="code_executor_agent",
    llm_config=False,
    code_execution_config={"executor": executor},
    human_input_mode="NEVER",
    default_auto_reply=
    "请继续 如果所有的事情都已经做完，请只返回 TERMINATE",
)
from prompt import WRITER_PROMPT
code_writer_agent = AssistantAgent(
    name="code_writer_agent",
    system_message=WRITER_PROMPT,
    llm_config=llm_config,
    code_execution_config=False,
    human_input_mode="NEVER",
)


queries = read_jsonl('./question.json')
results = []
for query in tqdm(queries):
    try:
        chat_result = code_executor_agent.initiate_chat(code_writer_agent, message=query['question'], max_turns=8)
        results.append(chat_result.chat_history[-3]['content'])
    except Exception as e:
        results.append(query['question'])

save_answers(queries=queries, results=results)