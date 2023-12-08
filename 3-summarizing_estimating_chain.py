import semantic_kernel as sk
kernel = sk.Kernel()

from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
api_key, org_id = sk.openai_settings_from_dot_env()
kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-4", api_key, org_id))

summarizing_skill = kernel.import_semantic_skill_from_directory("plugins", "tasks")
summarizing_function = summarizing_skill["SummarizingTask"]

# print(summarizing_function("Limpar a cozinha"))

estimating_skill = kernel.import_semantic_skill_from_directory("plugins", "tasks")
estimating_function = estimating_skill["EstimatingTask"]

summarizingResult = summarizing_function("Limpar a cozinha").result

estimatingResult = estimating_function(summarizingResult).result

print("Primeira skill: \n" + summarizingResult)
print("Segunda skill: \n" + estimatingResult)

