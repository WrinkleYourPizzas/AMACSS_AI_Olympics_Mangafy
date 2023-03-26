from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for, Flask
# from flask_login import login_required, current_user
# from .models import Note
# from . import db
# from sqlalchemy.sql import func
import json
import string
import os

import openai
from PIL import Image   # pip install pillow
import requests         # pip install requests
from io import BytesIO

from .response import answer_question, generate_image
import random

# courseText
# quizQuestions
# response
# summary
# images

prompt = "default"
courseParagraphs = []
courseImages = []
openai.api_key = "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"
app = Flask(__name__)

# usually easier to keep the name the same as the file
views = Blueprint('views', __name__)

def jackIsAGenius(textInput):
    text_prompt = "Split the story summary below into 4 equal sections.\n" + textInput

    chatgpt_response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                    messages=[{
                                                        "role":
                                                        "user",
                                                        "content":
                                                        text_prompt
                                                    }],
                                                    temperature=0.1,
                                                    max_tokens=500,
                                                    top_p=0.95)

    response = chatgpt_response['choices'][0]['message']['content'].strip()
    sections = response.split("Section")
    print("fdsafdsa")
    for i in range(0, len(sections)):
        print(sections[i])
    print("fdsafdsa")

    for i in range(1, len(sections)):
        pre_img_prompt = "Draw a cartoon picture based on the story belong with as much detil as possible: " + sections[
        i]
        print("*****************************************************************")
        print(pre_img_prompt)
        print("")
        pre_img_responses = openai.Completion.create(model="text-davinci-003",
                                                    prompt=pre_img_prompt,
                                                    temperature=0.15,
                                                    max_tokens=300,
                                                    top_p=0.88,
                                                    best_of=1,
                                                    frequency_penalty=0.2,
                                                    presence_penalty=0)
        image_prompt = pre_img_responses['choices'][0]['text'].strip()
        print("lmao lmao")
        print(image_prompt)

        image_object = openai.Image.create(prompt=image_prompt,
                                        n=1,
                                        size="512x512")

        image_url = image_object['data'][0]['url']

        # See Image
        url_response = requests.get(image_url)
        image = Image.open(BytesIO(url_response.content))
        image

        # Save image as a jpg file
        name = 'new_image ' + str(i)
        image_name = name + '.jpg'

        if url_response.status_code == 200:
            with open(image_name, "wb") as f:
                f.write(url_response.content)
                print("\033[1;36m Image saved successfully")  # Color print code!
        else:
            print("Failed to download image")

    text_prompt = """generate the most click baited league of legends youtube title ever"""

    chatgpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": text_prompt}],
            temperature=0.1,
            max_tokens=50,
            top_p=0.95)

    response = chatgpt_response['choices'][0]['message']['content'].strip()

    print(response)

    # Create image prompt yourself
    image_prompt_ = """Describe artistic realistic illustration of apple pie"""

    # Let AI create image prompt
    entry = '''
    frighten you?" Ser Waymar Royce asked with just the hint of a smile.
    Gared did not rise to the bait. He was an old man, past fifty, and he had seen the lordlings come and go.
    "Dead is dead," he said. "We have no business with the dead."
    "Are they dead?" Royce asked softly. "What proof have we?"
    "Will saw them," Gared said. "If he says they are dead, that's proof enough for me."
    Will had known they would drag him into the quarrel sooner or later. He wished it had been later rather
    than sooner. "My mother told me that dead men sing no songs," he put in.
    "My wet nurse said the same thing, Will," Royce replied. "Never believe anything you hear at a woman's
    tit. There are things to be learned even from the dead." His voice echoed, too loud in the twilit forest.
    "We have a long ride before us," Gared pointed out. "Eight days, maybe nine. And night is falling."
    Ser Waymar Royce glanced at the sky with disinterest. "It does that every day about this time. Are you
    unmanned by the dark, Gared?
    '''

    pre_img_prompt = """Describe artistic realistic illustration of """ + entry

    pre_img_responses = openai.Completion.create(
        model="text-davinci-003",
        prompt=pre_img_prompt,
        temperature=0.15,
        max_tokens=300,
        top_p=0.88,
        best_of=1,
        frequency_penalty=0.2,
        presence_penalty=0)

    image_prompt = pre_img_responses['choices'][0]['text'].strip()

    print(image_prompt)

    image_object = openai.Image.create(
                prompt=image_prompt,
                n=1,
                size="512x512")

    image_url = image_object['data'][0]['url']

    # See Image
    url_response = requests.get(image_url)
    image = Image.open(BytesIO(url_response.content))
    image

    # Save image as a jpg file
    name = 'new_image 2'
    image_name = name + '.jpg'

    if url_response.status_code == 200:
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(app.root_path, 'static', "new_image 2.jpg")

        with open(image_name, "wb") as f:
        # with open("images/" + "new_image 2.jpg", "wb") as f:
            f.write(url_response.content)
            print("\033[1;36m Image saved successfully")    # Color print code!
    else:
        print("Failed to download image")

    return response

# homepage
@views.route('/', methods=['GET', 'POST'])

def home():
    input = '''"Snow White" is a classic fairy tale about a young princess who lives with her father, the king, and her wicked stepmother, who is jealous of Snow White's beauty. The stepmother orders her huntsman to take Snow White into the forest and kill her, but he cannot bring himself to do it and tells her to run away instead.

    Snow White takes refuge in a small cottage in the forest, where she meets seven friendly dwarfs who take her in and allow her to live with them. Meanwhile, the evil stepmother is informed by her magic mirror that Snow White is still alive and is the fairest in the land, which drives her into a furious rage.

    Determined to kill Snow White, the stepmother disguises herself as an old woman and offers Snow White a poisoned apple, which puts her into a deep sleep. The dwarfs, who are unable to revive her, place her in a glass coffin and guard it. A handsome prince comes across the glass coffin and falls in love with Snow White, kissing her and breaking the spell.

    Together, the prince and Snow White live happily ever after, while the stepmother meets a tragic end for her evil deeds.

    The story teaches children the importance of kindness, friendship, and love, while warning against the dangers of envy, jealousy, and selfishness. It is also a reminder that true beauty comes from within and that we should always treat others with kindness and respect.'''
    # dennyIsAGenius()
    # jackIsAGenius(input)
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    print("-------------------------------------------------------------------------------" + ROOT_DIR)
    return render_template('query.html', prompt="", courseParagraphs="", courseImages="")
    # return "hello"

@views.route('/generate-response', methods=['POST'])
def generate_response():
    prompt = json.loads(request.data)
    promptText = prompt['text']
    print(promptText)
    jackIsAGenius(promptText)
    return jsonify({"resp": answer_question(promptText), "image_url": generate_image(promptText)})
