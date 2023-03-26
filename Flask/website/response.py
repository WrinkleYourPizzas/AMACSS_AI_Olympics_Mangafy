"""
response.py
-----------------
Answers users question in the chat
"""

import openai
import os
openai.api_key = os.environ.get("OPENAI_API_KEY")        # YOUR API KEY GOES HERE (replace)

# In this function, you will accept a question from the user and generate a response using GPT
def answer_question(user_question):
    """
    Answer to questions in the chatbox
    :param user_question: Question of user in the chat
    """

    # TODO: generate response based on user_question and return as a single string
    return ""

# In this function, you will generate an image based on the user prompt
def generate_image(prompt):
    try:
        # TODO: generate one image which relates to prompt, and return the url of the image as a string
        return ""
    except:
        # DO NOT DELETE!
        return ""