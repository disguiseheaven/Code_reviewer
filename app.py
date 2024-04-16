from openai import OpenAI
import streamlit as st

########## Import key #######

f = open('keys/app_key.txt')
app_key = f.read()
client = OpenAI(api_key = app_key)

##############################

##### Heading ##########

st.title('💬AI Code :red[Reviewer] 😎')
st.subheader("Enter your code to fix the bugs!")

###### Prompt ########
prompt = st.text_area("Enter your code: ")

###### OPenai Code ########
if st.button('Generate') == True:
    response = client.chat.completions.create(
    model = "gpt-3.5-turbo-1106",
    messages = [
        {"role": "system", "content":"You are a code bug fixer, you return the bugs in code in an ordered list and also the correct code in jupyter notebook look."},
        {"role": "user", "content": prompt}
    ]
    )

    st.write(response.choices[0].message.content)

