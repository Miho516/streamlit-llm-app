from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

import streamlit as st

# LLMからの応答を取得する関数
def get_llm_response(user_input, expert_type):
    # 専門家に応じたシステムメッセージの設定
    if expert_type == "心理カウンセラー":
        system_message = SystemMessage(content="あなたは優しい心理カウンセラーです。")
    elif expert_type == "歴史学者":
        system_message = SystemMessage(content="あなたは知識豊富な歴史学者です。")

    # ユーザーメッセージの作成
    human_message = HumanMessage(content=user_input)

    # ChatOpenAIインスタンスの作成
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    # チャットの実行
    response = llm.invoke([system_message, human_message])

    return response.content

st.title("💬 専門家AIチャットアプリ")
st.write("ラジオボタンで専門家を選び、質問を入力してください。")

# 専門家選択
expert_type = st.radio(
    "どの専門家に質問しますか？",
    ("心理カウンセラー", "歴史学者")
)

# テキスト入力
user_input = st.text_area("質問内容を入力してください")

# 送信ボタン
if st.button("送信"):
    if user_input:
        response = get_llm_response(user_input, expert_type)
        st.write("### 回答:")
        st.write(response)
    else:
        st.warning("テキストを入力してください。")

