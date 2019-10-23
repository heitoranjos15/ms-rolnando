import json
from ibm_watson import AssistantV2, SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


class Watson:
    def __init__(self, api_key, assistant_id=None):
        self.authenticator = IAMAuthenticator(api_key)
        if assistant_id:
            self.service = AssistantV2(
                version='2019-02-28',
                authenticator=self.authenticator
            )
            self.service.set_service_url(
                'https://gateway.watsonplatform.net/assistant/api')
            self.assistant_id = assistant_id
            self.session = self.create_session()

    def create_session(self):
        response = self.service.create_session(
            assistant_id=self.assistant_id
        ).get_result()
        return response

    def get_answer(self, question):
        response = self.service.message(
            assistant_id=self.assistant_id,
            session_id=self.session.get('session_id'),
            input={
                'message_type': 'text',
                'text': question
            }
        ).get_result()
        return response.get('output').get('generic')[0].get('text')

    def get_question(self):
        speech_to_text = SpeechToTextV1(
            authenticator=self.authenticator
        )
        speech_to_text.set_service_url(
            'https://stream.watsonplatform.net/speech-to-text/api')
        with open('./file.wav', 'rb') as audio_file:
            speech_recognition_results = speech_to_text.recognize(
                audio=audio_file,
                content_type='audio/wav',
                word_alternatives_threshold=0.9,
                keywords=['if', 'oque e', 'do while'],
                keywords_threshold=0.5
            ).get_result()
        return speech_recognition_results.get('results')[0].get('alternatives')[0].get('transcript')
