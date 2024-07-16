from flask import Flask    
from flask_cors import CORS
from controller.DynamicController import app as dc 


# Inicia o aplicativo Flask
app = Flask(__name__)
# Habilita CORS para todas as rotas
CORS(app)

# Torna os endpoints acessiveis através do aplicativo Flask
app.register_blueprint(dc)

if __name__ == "__main__":
    # Inicia o servidor Flask
    app.run(debug=True)