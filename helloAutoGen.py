import autogen
import openai
from apikey import apikey

openai.api_key = apikey

assistant = autogen.AssistantAgent("assistant")
user_proxy = autogen.UserProxyAgent("user_proxy")
user_proxy.initiate_chat(assistant, message="Show me the YTD gain of 10 largest technology companies as of today.")