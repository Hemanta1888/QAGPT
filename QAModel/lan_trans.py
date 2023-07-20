from translate import Translator


class LanguageConversation:
    def __init__(self, source_lan="en", target_lan="or") -> str:
        self.source_lang = source_lan
        self.target_lang = target_lan

    def __eng_to_or(self, text) -> str:
        translator = Translator(to_lang=self.target_lang)
        or_translation = translator.translate(text)
        return or_translation

    def __or_to_eng(self, text) -> str:
        translator = Translator(from_lang=self.target_lang, to_lang=self.source_lang)
        eng_translation = translator.translate(text)
        return eng_translation

    def language_con(self, lan, text) -> str:
        if lan == self.target_lang:
            return self.__or_to_eng(text)
        else:
            return self.__eng_to_or(text)
