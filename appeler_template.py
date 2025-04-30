#Installer la bibliothèque Elasticsearch pour Python

#pip install elasticsearch
#-------------Code Python pour appeler le template---------
import time
from elasticsearch import Elasticsearch

# Connexion à Elasticsearch
es = Elasticsearch("http://localhost:9200")  # Remplace l'URL si nécessaire

# Paramètres pour le template
params = {
    "start_date": "2025-02-01T00:00:00",
    "end_date": "2025-02-28T23:59:59",
    "cdr_type": "moc"
}

# Mesurer le temps d'exécution
start_time = time.time()  # Enregistrer le temps de début

# Appel au template '_search/template'
try:
    response = es.search_template(
        index="name_index",  
        body={
            "id": "count_served_isdn",
            "params": params
        }
    )
    end_time = time.time()  # Enregistrer le temps de fin

    # Calculer la durée d'exécution
    execution_time = end_time - start_time
    print(f"Temps d'exécution : {execution_time:.4f} secondes")
    
    # Affichage de la réponse
    print(response)

except Exception as e:
    print(f"Erreur lors de l'appel au template : {e}")
