# pip install openai streamlit -> Install these libraries become executing

from openai import OpenAI
import streamlit as st

#Api key 
with open("keys/api_key.txt") as f:
    key = f.read()

client = OpenAI(api_key=key)


def fix_code(language,code):
    prompt = f"Fix this {language} code {code}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-16k-0613",
        messages=[
            {"role": "system", "content": "You are a helpful code assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    response = response.choices[0].message.content
    print(response)
    return response


def main():
    st.title("An AI Code Reviewer")

    code = st.text_area("Enter you code here",height=300)
    language = st.selectbox("Select yor language",("Python","JavaScript","Java","csharp"))

    if st.button("Generate"):
        if code.strip():
            fixed_code = fix_code(language,code)
            st.subheader("Code Review")
            st.write(fixed_code)


if __name__ == '__main__':
    main()
