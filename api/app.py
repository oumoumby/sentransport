import json
from flask import Flask, jsonify
from flask_cors import CORS
import requests
app = Flask(__name__)
CORS(app)

# Charger les données depuis le fichier JSON
with open("lignes_ddd.json", "r") as f:
    lignes = json.load(f)

@app.route("/")
def accueil():
    return jsonify({
        "message": "Bienvenue sur l'API SenTransport !",
        "endpoints": ["/lignes", "/lignes/<id>"]
    })

@app.route("/lignes")
def get_lignes():
    return jsonify(lignes)

@app.route("/lignes/<int:ligne_id>")
def get_ligne(ligne_id):
    ligne = next(
        (l for l in lignes if l["id"] == ligne_id),
        None
    )
    if ligne is None:
        return jsonify({"erreur": "Ligne non trouvée"}), 404
    return jsonify(ligne)

@app.route("/arrets")
def get_arrets():
    arrets = set()
    for ligne in lignes:
        arrets.update(ligne["listeArrets"])
    return jsonify({"les arrets": list(arrets)})

@app.route("/stats")
def get_stats():
    total_lignes = len(lignes)
    total_arrets = sum(len(ligne["listeArrets"]) for ligne in lignes)
    ligne_avec_le_plus_d_arrets = max(lignes, key=lambda ligne: len(ligne["listeArrets"]))
    return jsonify({
        "nombre_de_lignes": total_lignes,
        "nombre_d_arrets": total_arrets,
        "ligne_avec_le_plus_d_arrets": ligne_avec_le_plus_d_arrets
    })

@app.route("/lignes/recherche")
def recherche_lignes():
    q = request.args.get("q", "").lower()
    return jsonify([
        ligne for ligne in lignes
        if q in ligne["depart"].lower() or q in ligne["arrivee"].lower()
    ])

if __name__ == "__main__":
    app.run(debug=True, port=5000)