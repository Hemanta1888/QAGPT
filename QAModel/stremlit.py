from user_model import UserModel
from html_temp import user_template, css, bot_template
import streamlit as st
import time


class APP(UserModel):
    st.title("QAGPT 🤖")
    st.write(css, unsafe_allow_html=True)

    def __init__(self) -> None:
        pass

    def run_model_response(self) -> str:
        user_selection = st.selectbox(
            "Please select your preferred language", ("English", "Odia")
        )
        if user_selection.lower() == "odia":
            time.sleep(5)
            or_intro_prompt = "ନମସ୍କାର! ମୁଁ ହେମନ୍ତଙ୍କ ଦ୍ୱାରା ବିକଶିତ ଏକ AI ବଟ୍ | ମୁଁ ତୁମର ପ୍ରଶ୍ନର ଉତ୍ତର ଦେବାକୁ ସାହାଯ୍ୟ କରିପାରିବି | ଯଦି ମୁଁ ଭୁଲ ଉତ୍ତର ଦିଏ ଦୟାକରି ମୋତେ କ୍ଷମା କରିବେ କାରଣ ମୁଁ ଶିକ୍ଷଣ ପର୍ଯ୍ୟାୟରେ ଅଛି"
            st.markdown(or_intro_prompt)
            user_question = st.text_input("ଦୟାକରି ମୋତେ ତୁମର ପ୍ରଶ୍ନ ପଚାର: ")
            if user_question:
                user = UserModel("or", user_question)
                response = user.response_data()
                st.write(
                    user_template.replace("{{MSG}}", user_question),
                    unsafe_allow_html=True,
                )
                st.write(
                    bot_template.replace("{{MSG}}", response), unsafe_allow_html=True
                )
        else:
            time.sleep(5)
            en_intro_prompt = "Hello! I am an AI bot developed by Hemanta. I can help answer your questions. Please forgive me if I answer wrongly as I am still learning"
            st.markdown(en_intro_prompt)
            user_question = st.text_input("Please enter your question: ")
            if user_question:
                user = UserModel("en", user_question)
                response = user.response_data()
                st.write(
                    user_template.replace("{{MSG}}", user_question),
                    unsafe_allow_html=True,
                )
                st.write(
                    bot_template.replace("{{MSG}}", response), unsafe_allow_html=True
                )
                # st.text_area("Answer:", response)
        return user_question


app = APP()
app.run_model_response()
