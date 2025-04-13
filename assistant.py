import requests
from typing import Optional

class KubanGuide:
    def __init__(self):
        # Настройки API
        self.api_key = "jTFMMj8aHY6dM1bUJfoNQzXUZbLkM9LM"
        self.api_url = "https://api.deepinfra.com/v1/openai/chat/completions"
        
        # Системный промт
        self.system_prompt = """Ты Казачок — виртуальный гид по Краснодарскому краю. Отвечай:
1. На вопросы о маршрутах — развернуто и структурированно
2. На общие вопросы — кратко и по-дружески
3. Всегда одним вариантом ответа
4. Говори естественно, как живой человек
5. Используй казачьи выражения ("батько", "голубчик")"""

    def generate_response(self, query: str) -> str:
        """Генерация ответа через API"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "meta-llama/Meta-Llama-3-70B-Instruct",
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": f"Ответь естественно: {query}"}
            ],
            "temperature": 0.7,
            "max_tokens": 500,
            "stop": ["\n\n"]
        }
        
        try:
            response = requests.post(self.api_url, headers=headers, json=data, timeout=15)
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content'].strip()
            return "Ой, что-то не вышло сообразить..."
        except Exception as e:
            return f"Произошла ошибка: {str(e)}"