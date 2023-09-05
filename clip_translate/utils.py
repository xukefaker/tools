import http.client
import json


class chatGPTInstance():

    def __init__(self, config):
        self.key = config['key']
        self.config = config
        self.AUTHORIZATION = 'Bearer {}'.format(self.config['key'])
        self.models = self.get_model()

    def get_model(self):
        conn = http.client.HTTPSConnection("api.chatanywhere.com.cn")
        payload = ''
        headers = {
            'Authorization': self.AUTHORIZATION,
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'
        }
        conn.request("GET", "/v1/models", payload, headers)
        res = conn.getresponse()
        data = json.loads(res.read())
        models = []
        for model_data in data['data']:
            models.append(model_data['id'])
        return models

    def translate_single(self, sentence): # 翻译单个句子

        conn = http.client.HTTPSConnection("api.chatanywhere.com.cn")
        payload = json.dumps({
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": "{}:{}".format(self.config['prompt'], sentence)
                }
            ]
        })
        headers = {
            'Authorization': self.AUTHORIZATION,
            'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
            'Content-Type': 'application/json'
        }
        conn.request("POST", "/v1/chat/completions", payload, headers)
        res = conn.getresponse()
        data = json.loads(res.read())
        return data['choices'][0]['message']['content']
