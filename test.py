from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
my_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=my_api_key)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages =[
        {"role":"system", "content":"Eres un detector de texto peligroso para niños. Tomas como input un mensaje o trozo de texto y lo clasificas entre las siguientes clases: \n-OFP: mensajes con contenido ofensivo dirigido directo al receptor.\n-OFG: mensajes con contenido ofensivo a un grupo de personas de cualquier índole.]\n-NO: Texto no ofensivo ni peligroso.\n-NOE: No ofensivo ni peligroso, pero explícito en su contenido.\n-GP: posible grooming hacia el sujeto.\nSolo respondes con el nombre de la clase."},
        {"role":"user", "content":"Zurdo de mierda"}
    ]
)

print(completion.choices[0].message)