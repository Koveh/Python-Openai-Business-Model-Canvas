import ast
import openai
from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates')

openai.api_key = "sk-NCl9ebUEbOu1T3BlbkFJ1peagkXsv2N2bOuvr1RI"

def generate_bmc_dictionary():
    with open("audio2.m4a", "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)

    text = transcript.text
    print (text)

    
    prompt = (
        f"take the given text:\n\n{text}\n\n"
        "make a business model canvas based on the ideas that is described above. Give as an output: python dictionary format with following keys and values as the list of strings with precise 4-10 word description for each of business model canvas element: \n"
        '{"key_partners": ["___",  "___", "___"], "key_activities": ["___",  "___", "___"], "key_resources": ["___",  "___", "___"], "value_propositions": ["___",  "___", "___"], "customer_relationships": ["___",  "___", "___"], "channels": ["___",  "___", "___"], "customer_segments": ["___",  "___", "___"], "cost_structure": ["___",  "___", "___"], "revenue_streams": ["___",  "___", "___"]})'
    )

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=3500,
        n=1,
        stop=None,
        temperature=0.5,
    )

    bmc_dictionary = ast.literal_eval(response.choices[0].text.strip())
    print(bmc_dictionary)
    return bmc_dictionary



@app.route('/')
def bmc():
    bmc_data = generate_bmc_dictionary()
    return render_template('bmc.html', bmc=bmc_data)


if __name__ == '__main__':
    app.run(debug=True)
