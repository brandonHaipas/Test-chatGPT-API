from utils import get_completion
from flask import Flask, jsonify, request
from app import app, DEBUG


@app.route('/classify', methods=['POST'])
def submit():
    
    #request contiene el texto a clasificar
    json_data = request.json
    text = json_data.get('message')
    
    
    prompt = f"""Eres un detector de texto potencialmente peligroso para niños. 
    Tienes que clasificar el texto entregado por el usuario entre 
    las siguientes categorias:
    -OFP: Mensajes con contenido ofensivo dirigido directo al receptor.
    -OFG: Mensajes con contenido ofensivo a un grupo de personas de cualquier índole.
    -NO: Texto no ofensivo ni peligroso.
    -NOE: No ofensivo ni peligroso, pero explícito en su contenido.
    -GP: Posible grooming hacia el sujeto.

    Ejemplos de interacción:

    user: Zurdo de mierda.

    gpt: OFP

    user: Los mapuches son todos flojos!

    gpt: OFG

    Debes entregar solamente la clase.
    """
    openai_response = get_completion(prompt, text)
    if DEBUG:
        print(openai_response)
    return jsonify({'class_name': openai_response})

if __name__ == "__main__":
    app.run(port=5001, debug=DEBUG)
