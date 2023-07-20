from model_tune import ModelFineTune
from lan_trans import LanguageConversation


class UserModel(LanguageConversation, ModelFineTune):
    def __init__(self, lang, que) -> None:
        LanguageConversation.__init__(self)
        ModelFineTune.__init__(self)
        self.lang = lang
        self.user_question = que

    def __model_or_response(self) -> str:
        or_intro_prompt = "ନମସ୍କାର! ମୁଁ ହେମନ୍ତଙ୍କ ଦ୍ୱାରା ବିକଶିତ ଏକ AI ବଟ୍ | ମୁଁ ତୁମର ପ୍ରଶ୍ନର ଉତ୍ତର ଦେବାକୁ ସାହାଯ୍ୟ କରିପାରିବି | ଯଦି ମୁଁ ଭୁଲ ଉତ୍ତର ଦିଏ ଦୟାକରି ମୋତେ କ୍ଷମା କରିବେ କାରଣ ମୁଁ ଶିକ୍ଷଣ ପର୍ଯ୍ୟାୟରେ ଅଛି"
        print(or_intro_prompt)
        or_que_prompt = "ଦୟାକରି ମୋତେ ତୁମର ପ୍ରଶ୍ନ ପଚାର: "
        return or_intro_prompt, or_que_prompt

    def __model_eng_response(self) -> str:
        en_intro_prompt = "Hello! I am an AI bot developed by Hemanta. I can help answer your questions. Please forgive me if I answer wrongly as I am still learning"
        print(en_intro_prompt)
        en_que_prompt = "Please ask me your question: "
        return en_intro_prompt, en_que_prompt

    def lan_con_model(self):
        if self.lang in ("odia", "or"):
            self.user_que = self.__model_or_response()
            lan_que_response = self.language_con(self.lang, self.user_question)
        else:
            self.user_que = self.__model_eng_response()
            lan_que_response = self.user_question

        return self.user_que, lan_que_response

    def response_data(self):
        user_que, lang_res = self.lan_con_model()
        response = self.model_response(lang_res)
        print(response)
        if response == "No good Wikipedia Search Result was found":
            response = "I don't know"
        # if 'wikipedia' in response.lower():
        # response = "I don't know"
        if self.lang in ("odia", "or"):
            response = self.language_con("en", response)
        return response
