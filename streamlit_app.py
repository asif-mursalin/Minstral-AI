# %%
import os
os.environ["MISTRAL_API_KEY"] = "LoXIODO6VkldB64uwva76l1zDpIz6cfu"
print(f"MISTRAL_API_KEY: {os.environ.get('MISTRAL_API_KEY')}")

# %%
api_key = os.getenv("MISTRAL_API_KEY")

# %%
import os
from mistralai import Mistral, UserMessage
def mistral(user_message, model="mistral-small-latest", is_json=False):
    model = "mistral-large-latest"
    client = Mistral(api_key=api_key)
    messages = [
        UserMessage(content=user_message),
    ]
    chat_response = client.chat.complete(
        model=model,
        messages=messages,
    )
    return chat_response.choices[0].message.content

# %%
mistral("hello, what can you do?")

# %%
prompt = """
You are a bank customer service bot.
Your task is to assess customer intent and categorize customer
inquiry after <<<>>> into one of the following predefined categories:
card arrival
change pin
exchange rate
country support
cancel transfer
charge dispute
If the text doesn't fit into any of the above categories,
classify it as:
customer service
You will only respond with the predefined category.
Do not provide explanations or notes.
###
Here are some examples:
Inquiry: How do I know if I will get my card, or if it is lost? I am concerned about the delivery process and would like to ensure that I will receive my ca
Category: card arrival
Inquiry: I am planning an international trip to Paris and would like to inquire about the current exchange rates for Euros as well as any associated fees fo
Category: exchange rate
Inquiry: What countries are getting support? I will be traveling and living abroad for an extended period of time, specifically in France and Germany, and w
Category: country support
Inquiry: Can I get help starting my computer? I am having difficulty starting my computer, and would appreciate your expertise in helping me troubleshoot th
Category: customer service
###
<<<
Inquiry: {inquiry}
>>>
Category:
"""

# %%
response = mistral(f"Please correct the spelling and grammar of \
this prompt and return a text that is the same prompt,\
with the spelling and grammar fixed: {prompt}")

# %%
print(response)

# %%
mistral(
response.format(
inquiry="I am inquiring about the availability of your cards in the EU")
)

# %%
medical_notes = """
A 60-year-old male patient, Mr. Johnson, presented with symptoms
of increased thirst, frequent urination, fatigue, and unexplained
weight loss. Upon evaluation, he was diagnosed with diabetes,
confirmed by elevated blood sugar levels. Mr. Johnson's weight
is 210 lbs. He has been prescribed Metformin to be taken twice daily
with meals. It was noted during the consultation that the patient is
a current smoker.
"""

# %%
prompt = f"""
Extract information from the following medical notes:
{medical_notes}
Return json format with the following JSON schema:
{{
    "age": {{
        "type": "integer"
    }},
    "gender": {{
        "type": "string",
        "enum": ["male", "female", "other"]
    }},
    "diagnosis": {{
        "type": "string",
        "enum": ["migraine", "diabetes", "arthritis", "acne"]
    }},
    "weight": {{
        "type": "integer"
    }},
    "smoking": {{
        "type": "string",
        "enum": ["yes", "no"]
    }}
}}
"""    

# %%
response = mistral(prompt, is_json=True)
print(response)

# %%
email = """
Dear mortgage lender,
What's your 30-year fixed-rate APR, how is it compared to the 15-year
fixed rate?
Regards,
Anna
"""

# %%
prompt = f"""
You are a mortgage lender customer service bot, and your task is to
create personalized email responses to address customer questions.
Answer the customer's inquiry using the provided facts below. Ensure
that your response is clear, concise, and directly addresses the
customer's question. Address the customer in a friendly and
professional manner. Sign the email with "Lender Customer Support."
# Facts
30-year fixed-rate: interest rate 6.403%, APR 6.484%
20-year fixed-rate: interest rate 6.329%, APR 6.429%
15-year fixed-rate: interest rate 5.705%, APR 5.848%
10-year fixed-rate: interest rate 5.500%, APR 5.720%
7-year ARM: interest rate 7.011%, APR 7.660%
5-year ARM: interest rate 6.880%, APR 7.754%
3-year ARM: interest rate 6.125%, APR 7.204%
30-year fixed-rate FHA: interest rate 5.527%, APR 6.316%
30-year fixed-rate VA: interest rate 5.684%, APR 6.062%
# Email
{email}
"""

# %%
response = mistral(prompt)
print(response)

# %%
newsletter = """
European AI champion Mistral AI unveiled new large language models and formed an alliance with Microsoft. 

What’s new: Mistral AI introduced two closed models, Mistral Large and Mistral Small (joining Mistral Medium, which debuted quietly late last year). Microsoft invested $16.3 million in the French startup, and it agreed to distribute Mistral Large on its Azure platform and let Mistral AI use Azure computing infrastructure. Mistral AI makes the new models available to try for free here and to use on its La Plateforme and via custom deployments.

Model specs: The new models’ parameter counts, architectures, and training methods are undisclosed. Like the earlier, open source Mistral 7B and Mixtral 8x7B, they can process 32,000 tokens of input context. 

Mistral Large achieved 81.2 percent on the MMLU benchmark, outperforming Anthropic’s Claude 2, Google’s Gemini Pro, and Meta’s Llama 2 70B, though falling short of GPT-4. Mistral Small, which is optimized for latency and cost, achieved 72.2 percent on MMLU.
Both models are fluent in French, German, Spanish, and Italian. They’re trained for function calling and JSON-format output.
Microsoft’s investment in Mistral AI is significant but tiny compared to its $13 billion stake in OpenAI and Google and Amazon’s investments in Anthropic, which amount to $2 billion and $4 billion respectively.
Mistral AI and Microsoft will collaborate to train bespoke models for customers including European governments.
Behind the news: Mistral AI was founded in early 2023 by engineers from Google and Meta. The French government has touted the company as a home-grown competitor to U.S.-based leaders like OpenAI. France’s representatives in the European Commission argued on Mistral’s behalf to loosen the European Union’s AI Act oversight on powerful AI models. 

Yes, but: Mistral AI’s partnership with Microsoft has divided European lawmakers and regulators. The European Commission, which already was investigating Microsoft’s agreement with OpenAI for potential breaches of antitrust law, plans to investigate the new partnership as well. Members of President Emmanuel Macron’s Renaissance party criticized the deal’s potential to give a U.S. company access to European users’ data. However, other French lawmakers support the relationship.

Why it matters: The partnership between Mistral AI and Microsoft gives the startup crucial processing power for training large models and greater access to potential customers around the world. It gives the tech giant greater access to the European market. And it gives Azure customers access to a high-performance model that’s tailored to Europe’s unique regulatory environment.

We’re thinking: Mistral AI has made impressive progress in a short time, especially relative to the resources at its disposal as a startup. Its partnership with a leading hyperscaler is a sign of the tremendous processing and distribution power that remains concentrated in the large, U.S.-headquartered cloud companies.
"""

# %%
prompt = f"""
You are a commentator. Your task is to write a report on a newsletter.
When presented with the newsletter, come up with interesting questions to ask,
and answer each question.
Afterward, combine all the information and write a report in the markdown
format.
# Newsletter:
{newsletter}
# Instructions:
## Summarize:
In clear and concise language, summarize the key points and themes
presented in the newsletter.
## Interesting Questions:
Generate three distinct and thought-provoking questions that can be
asked about the content of the newsletter. For each question:
- After "Q: ", describe the problem
- After "A: ", provide a detailed explanation of the problem addressed
in the question.
- Enclose the ultimate answer in <>.
## Write a analysis report
Using the summary and the answers to the interesting questions,
create a comprehensive report in Markdown format.
"""

# %%
response = mistral(prompt)
print(response)

# %%



