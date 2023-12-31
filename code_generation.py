import autogen
from apikey import apikey

config_list=[{
    "model":"gpt-4",
    "api_key": apikey
}]

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={
        "seed": 42,
        "config_list": config_list,
        "temperature": 0
    }
)

user_proxy = autogen.UserProxyAgent(
    name="My Assistant",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False,  # set to True or image name like "python:3" to use docker
    },
)

user_proxy.initiate_chat(
    assistant,
    message="""Write code to develop OpenAI LLM ChatBot.""",
)