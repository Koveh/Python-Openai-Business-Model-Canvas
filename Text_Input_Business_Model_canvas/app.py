import ast
import openai
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')


openai.api_key = "sk-YOUR_API_KEY"


def generate_bmc_dictionary(text):

    prompt = (
        f"take the given text:\n\n{text}\n\n"
        "Make a Business Model Canvas based on the text above. Give as an output: python dictionary format with following keys and values as the list of strings. Each point ___ must have 3-10 word description: \n"
        '{"key_partners": ["___",  "___", "___"], "key_activities": ["___",  "___", "___"], "key_resources": ["___",  "___", "___"], "value_propositions": ["___",  "___", "___"], "customer_relationships": ["___",  "___", "___"], "channels": ["___",  "___", "___"], "customer_segments": ["___",  "___", "___"], "cost_structure": ["___",  "___", "___"], "revenue_streams": ["___",  "___", "___"]})'
    )

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=3450,
        n=1,
        stop=None,
        temperature=0.5,
    )

    bmc_dictionary = ast.literal_eval(response.choices[0].text.strip())
    print(bmc_dictionary)
    return bmc_dictionary


@app.route('/', methods=['GET', 'POST'])
def bmc():
    if request.method == 'POST':
        text = request.form['text']
        bmc_data = generate_bmc_dictionary(text)
        return render_template('bmc.html', bmc=bmc_data)
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)
