import os
import openai

openai.api_key = "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"  # 请替换为您的API密钥
def chat_gtp():
    """
    system: 系统消息有助于设置助手assistant的行为。在下面的例子中，助手被指示为“你是一个有用的助手”。
    user:  用户消息有助于指导助手assistant。通常是用户输入，描述用户要问的内容
    assistant: 由于模型对过去的请求没有记忆。 用 assistant 存储先前的响应。当用户在提问时,引用了以前的消息时,后台可以自动帮助openai理解上下文。
    如果对话不适合模型的令牌限制，则需要以某种方式缩短它。
    """
    messages = [
        {"role": "system", "content": "You’re a kind helpful assistant"}
    ]

    while True:
        user_input = input("->问题: ")
        if not user_input.strip():   # 如果用户输入为空，退出程序
            break
        messages.append({"role": "user", "content": user_input})

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        print(f'{completion.choices[0]}')   # 输出这个响应
        chat_response = completion.choices[0].message.content   # 从响应中提起用户关心的回答
        print(f'\n{chat_response}')
        messages.append({"role": "assistant", "content": chat_response})  #用 assistant 存储先前的响应


if __name__=="__main__":
    chat_gtp()

