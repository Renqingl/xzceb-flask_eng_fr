"""Create modul to translate between English and French"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()



# apikey = os.environ['apikey']
# url = os.environ['url']

apikey="SZb8z5gQ1Cw0PPgZUWLuLpWmr8jbNzpPH4dSF5d40zMg"
url="https://api.us-south.language-translator.watson.cloud.ibm.com/instances/66014d5d-1251-4af2-8b14-3bd9ba024de9"

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(english_text):
    """convert english to French"""
    if english_text is None:
        return 'null value entered'
    translation = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    """convert french to English"""
    if french_text is None:
        return 'null value entered'
    translation = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
