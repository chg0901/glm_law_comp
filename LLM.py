from zhipuai import ZhipuAI
import json
import re
from utils import get_zhipu_api_key
from autogen.coding import LocalCommandLineCodeExecutor
from autogen_tools import *
from autogen import ConversableAgent, AssistantAgent
from prompt import *
def LLM(query):
    client = ZhipuAI()
    response = client.chat.completions.create(
    model="glm-4",
        messages=[
            {"role": "user", "content": query},
        ],
        stream=False,
        )
    return response.choices[0].message.content

def prase_json_from_response(rsp: str):
    pattern = r"```json(.*?)```"
    rsp_json = None
    try:
      match = re.search(pattern, rsp, re.DOTALL)
      if match is not None:
        try:
          rsp_json =  json.loads(match.group(1).strip())
        except:
          pass
      else:
        rsp_json  = json.loads(rsp)
      return rsp_json
    except json.JSONDecodeError as e:
      raise("Json Decode Error: {error}".format(error = e))

def write_execute(plan_id, query):
  ZHIPU_API_KEY = get_zhipu_api_key()
  llm_config = {
      "config_list": [
          {
      'api_key': ZHIPU_API_KEY,   
      "model": "glm-4",
      'base_url': "https://open.bigmodel.cn/api/paas/v4/",
          },
      ],
  }
  executor = LocalCommandLineCodeExecutor(
    timeout=60,
    work_dir="coding",
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
)
  code_executor_agent = ConversableAgent(
      name="code_executor_agent",
      llm_config=False,
      code_execution_config={"executor": executor},
      human_input_mode="NEVER",
      default_auto_reply=
      "请继续 如果所有的事情都已经做完，请只返回'TERMINATE'。",
  )
  prompt_list = [WRITER_PROMPT_1, WRITER_PROMPT_2, WRITER_PROMPT_3]
  code_writer_agent = AssistantAgent(
      name="code_writer_agent",
      system_message=prompt_list[plan_id - 1],
      llm_config=llm_config,
      code_execution_config=False,
      human_input_mode="NEVER",
  )
  chat_result = code_executor_agent.initiate_chat(
      code_writer_agent,
      message=query,
      max_turns=8
  )
  return chat_result.chat_history[-2]['content']