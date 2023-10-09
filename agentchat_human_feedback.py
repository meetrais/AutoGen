import autogen
from apikey import apikey

config_list=[{
    "model":"gpt-4",
    "api_key": apikey
}]

assiastnt = autogen.AssistantAgent(
    name="assistant",
    llm_config={
        "seed": 41,
        "config_list": config_list
    }
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="ALWAYS",
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE")
)

autogen.ChatCompletion.start_logging()

math_problem_to_solve = """
Find $a + b + c$, given that $x+y \\neq -1$ and 
\\begin{align}
	ax + by + c & = x + 7,\\
	a + bx + cy & = 2x + 6y,\\
	ay + b + cx & = 4x + y.
\\end{align}.
"""

user_proxy.initiate_chat(assiastnt, message=math_problem_to_solve)