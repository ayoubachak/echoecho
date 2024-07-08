from models import ai_models
from common import logger


for name, instance in ai_models.models.items():
    print(name, instance)
second_model = list(ai_models.models.keys())[1]
result = ai_models.models[second_model].sys_inference(
    "You are an intelligent assistant, genius in geography, and history",
    "What's the independance date of Morocco ?",
    seed=42
    )

logger.info(f"Result: {result}")