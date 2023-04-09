import openai
from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates')


openai.api_key = "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"

# insert your text here
text = '''Well, if I were to bring this idea to life, I think there could be a significant demand for a password-keeping watch, especially among individuals who value security and convenience. I could potentially market this watch to professionals, entrepreneurs, and other individuals who need to manage a lot of passwords for work or personal use.

In terms of pricing, I would have to consider the costs of manufacturing, marketing, and distribution. Since this would be a niche product, I would likely need to price it higher than a traditional watch to make a profit. However, I would have to strike a balance between affordability and profitability to make sure the product is accessible to a wider range of customers.

I think the key to success would be a strong marketing strategy, particularly in the digital space. I would need to create a buzz around the product and highlight its unique features to stand out from other smartwatches on the market. I would also need to partner with key influencers and thought leaders to promote the product and generate interest.

In terms of costs, I would need to factor in the costs of research and development, manufacturing, marketing, and distribution. I would also need to consider the costs of ongoing support and maintenance for the product.

Overall, while there may be some challenges associated with bringing this product to market, I think it has the potential to be a profitable and innovative solution to a common problem. With the right strategy and execution, I believe this password-keeping watch could be a success.
'''

def generate_bmc_dictionary(text):

    prompt = (
        f"take the given text:\n\n{text}\n\n"
        f"make a business model canvas based on the ideas that is described above. Give as an output: python dictionary format with following keys and values as the list of strings with different example for each of business model canvas element: \n"
        f'dict("key_partners": ["___", "___"], "key_activities": ["___", "___"], "key_resources": ["___", "___"], "value_propositions": ["___", "___"], "customer_relationships": ["___", "___"], "channels": ["___", "___"], "customer_segments": ["___", "___"], "cost_structure": ["___", "___"], "revenue_streams": ["___", "___"])'
    )

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=4097,
        n=1,
        stop=None,
        temperature=0.5,
    )

    bmc_dictionary = eval(response.choices[0].text.strip())
    print(bmc_dictionary)
    return bmc_dictionary

@app.route('/')
def bmc():
    bmc_data = generate_bmc_dictionary(text)
    return render_template('bmc.html', bmc=bmc_data)


if __name__ == '__main__':
    app.run(debug=True)