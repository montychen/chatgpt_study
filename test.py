# coding=utf-8
import openai

openai.api_key='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'

def complete_davinci():
    res = openai.Completion.create(
        model="text-davinci-003", 
        prompt="老虎和狮子谁厉害", 
        temperature=0, 
        max_tokens=1000)
    return res['choices'][0]['text']


if __name__=="__main__":
    print(complete_davinci())
