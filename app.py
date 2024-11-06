import streamlit as st
import openai

# OpenAI APIキーを設定
openai.api_key = "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" 

# アドバイス生成関数
def generate_advice(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()

st.title("履歴書・エントリーシート作成支援AI")
st.write("各質問に答えてください。アドバイスを生成します。")

# フォームの入力項目
personal_pr = st.text_area("自己PRを入力してください")
student_life = st.text_area("学生時代に頑張ったことを入力してください")
motivation = st.text_area("志望動機を入力してください")

if st.button("アドバイスを生成"):
    st.write("AIがアドバイスを生成中...")

    # 各項目に対してAIに質問する
    if personal_pr:
        advice_pr = generate_advice(f"自己PRについてアドバイスしてください: {personal_pr}")
        st.write("自己PRアドバイス:", advice_pr)
    
    if student_life:
        advice_life = generate_advice(f"学生時代に頑張ったことについてアドバイスしてください: {student_life}")
        st.write("学生時代に頑張ったことアドバイス:", advice_life)
    
    if motivation:
        advice_motivation = generate_advice(f"志望動機についてアドバイスしてください: {motivation}")
        st.write("志望動機アドバイス:", advice_motivation)

