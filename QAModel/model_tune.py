from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper


class ModelFineTune:
    def __init__(self, model="deepset/roberta-base-squad2") -> None:
        self.model_name = model

    def __model_tokenizer(self, temp=0.8, k_nearest=5) -> pipeline:
        model = AutoModelForQuestionAnswering.from_pretrained(self.model_name)
        tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        qa_bot = pipeline(
            "question-answering",
            model=model,
            tokenizer=tokenizer,
            temperature=temp,
            k=k_nearest,
        )

        return qa_bot

    def __user_query_input(self, user_text) -> WikipediaAPIWrapper:
        user_query = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
        context_gen = user_query.run(user_text)
        print("context", context_gen)
        qa_input = {"question": user_text, "context": context_gen}
        return qa_input

    def model_response(self, text) -> dict:
        qa_bot_model = self.__model_tokenizer()
        user_query = self.__user_query_input(text)
        model_response = qa_bot_model(user_query)
        return model_response["answer"]
