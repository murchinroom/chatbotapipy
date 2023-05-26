# chatbotapiv2

[muvtuber](https://github.com/cdfmlr/muvtuber) 的 Chatbot API 服务端框架。

- based on proto [muvtuber.chatbot.v2.ChatbotService](https://github.com/cdfmlr/muvtuber-proto/blob/8d7cc02676cb8144683a185266c36dca18436b5e/muvtuber/chatbot/v2/chatbot.proto)
- stole codes from [t5_chatbot/muvtuber_chatbot_api](https://github.com/cdfmlr/t5_chatbot/tree/main/t5_chatbot/muvtuber_chatbot_api)

## 用法

继承一些类：

- `Chatbot`: 封装深度学习模型 or 远程方法调用，提供对话能力:
    - 重载：`ask(prompt) -> response`
- `ChatbotFactory`: 用来创建你的 `Chatbot` 子类
    - 重载：`create_chatbot(config) -> Chatbot`
- `ChatbotConfig`: dataclass，你的 `ChatbotFactory`、`Chatbot` 可以使用的创建参数

开启 muvtuber 的 chatbot 服务：

```python
from chatbotapiv2 import serve_grpc, MuvtuberGrpcServerConfig

# 把你的 factory 和 config 注入进去
config = MuvtuberGrpcServerConfig(
    chatbot_factory=T5ChatbotFactory(),
    chatbot_config_class=T5ChatbotConfig,
    address="localhost:50053",  # gRPC 服务监听的地址
    # ... 其他一些可选的配置
    )

# 开启服务
serve_grpc(config)
```

