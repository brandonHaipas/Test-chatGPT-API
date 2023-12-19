from app import client

DEBUG = False

def get_completion(prompt, text,  model="gpt-3.5-turbo"):
    messages = [{"role": "system", "content": prompt},
                {"role":"user", "content": text}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content