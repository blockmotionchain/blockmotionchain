from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "BlockMotionChain Server está ativo!", 200

@app.route('/receber_bloco', methods=['POST'])
def receber_bloco():
    dados = request.json
    if not dados:
        return jsonify({"erro": "Dados inválidos"}), 400
        
    print("\n--- NOVO BLOCO RECEBIDO NA BLOCKMOTIONCHAIN ---")
    print(f"ID: #{dados.get('id')}")
    print(f"Eixos: X={dados.get('x')}, Y={dados.get('y')}, Z={dados.get('z')}")
    print(f"Momento: {dados.get('momento')}")
    print(f"Hash Anterior: {dados.get('hash_anterior')}")
    print(f"Hash Atual: {dados.get('hash_atual')}")
    
    return jsonify({"status": "sucesso", "mensagem": "Bloco registrado com sucesso!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  
