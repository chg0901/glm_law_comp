from zhipuai import ZhipuAI
import json
import re
from utils import get_zhipu_api_key
from autogen.coding import LocalCommandLineCodeExecutor
from tools import *
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

def refine_answer(question, answer):
  prompt=f"""
  问题：{question}
  信息：{answer}
  请整合答案，直接给出简洁、完整且清晰的回答。回答格式忠于提问方式。不要回答问题之外的内容。
  回答：
  """
  final_answer = LLM(query=prompt)
  return final_answer

def write_execute(prompt, question):
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
      functions=[
         get_company_info,
         get_company_register,
         get_company_register_name,
         get_sub_company_info,
         get_sub_company_info_list,
         get_legal_document,
         get_legal_document_list,
         get_legal_abstract,
         get_xzgxf_info,
         get_xzgxf_info_list,
         get_court_info,
         get_court_code,
         get_lawfirm_info,
         get_lawfirm_log,
         get_address_info,
         get_address_code,
         get_temp_info,
         save_dict_list_to_word,
         get_citizens_sue_citizens,
         get_company_sue_citizens,
         get_citizens_sue_company,
         get_company_sue_company,
         get_sum,
         get_rank
      ]
  )
    code_executor_agent = ConversableAgent(
        name="code_executor_agent",
        llm_config=False,
        code_execution_config={"executor": executor},
        human_input_mode="NEVER",
        default_auto_reply=
        "请继续 如果所有的事情都已经做完，请只返回'TERMINATE'。",
    )
    code_writer_agent = AssistantAgent(
        name="code_writer_agent",
        system_message=prompt,
        llm_config=llm_config,
        code_execution_config=False,
        human_input_mode="NEVER",
    )
    chat_result = code_executor_agent.initiate_chat(
        code_writer_agent,
        message=question,
        max_turns=8
    )
    code_result = chat_result.chat_history[-2]['content']
    answer = refine_answer(question=question, answer=code_result)
    return answer