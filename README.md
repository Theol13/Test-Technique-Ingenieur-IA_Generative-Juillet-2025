#  Chatbot IA Générative avec Recherche Web – Partie 1 – Test Technique Juillet 2025

## Partie 1 – Développement d’un Chatbot avec accès Internet

L’objectif de cette première partie était de concevoir un chatbot capable d’interroger un modèle de langage (LLM) tout en intégrant des résultats de recherche web récents afin de fournir des réponses enrichies, pertinentes et actualisées.

> Requête test à implémenter :
> *“Quels sont les derniers développements en IA générative annoncés cette semaine ? Donne-moi 3 exemples concrets avec leurs sources.”*

Le projet inclut :
- Une API REST backend construite avec **FastAPI**
- Une logique de **recherche web automatique via SerpAPI**
- Deux modes de génération :
  - Un modèle cloud via **OpenRouter**
  - Un modèle local via **Hugging Face Transformers**

---

##  Stack technique

| Composant      | Outil utilisé                                       |
|----------------|-----------------------------------------------------|
| **Langage**    | Python 3.10+                                        |
| **Framework API** | FastAPI + Uvicorn                              |
| **Recherche Web** | `SerpAPI`                                       |
| **LLM Cloud**  | `qwen/qwen2.5-vl-32b-instruct:free`, puis `openchat/openchat-3.5` |
| **LLM Local**  | `microsoft/phi-2` via HuggingFace Transformers     |
| **Frontend**   | React (Create React App)

---

##  Fonctionnalités principales

-  **Recherche web en direct via SerpAPI**
-  **Deux modes de génération** :
  - `/ask` → appel au LLM via OpenRouter (cloud)
  - `/ask-local` → appel à un LLM local exécuté en Python
-  **Prompt enrichi** : les résultats web sont injectés dans le contexte du modèle
-  **Sécurisation** des clés API avec `.env`
-  **Interface Swagger** pour tester facilement l’API
-  **Interface React** fonctionnelle côté utilisateur

---

##  Exemple de fonctionnement

Requête envoyée :
```json
{
  "prompt": "Quels sont les derniers développements en IA générative cette semaine ?"
}
```

Processus :
1. Recherche web automatique (SerpAPI)
2. Résumé des 3 meilleurs résultats (titre, URL, extrait)
3. Construction d’un prompt enrichi
4. Envoi au modèle (cloud ou local)
5. Réponse générée et retournée à l’utilisateur

---

##  Structure du projet

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── openrouter_service.py
│   ├── local_model_service.py
│   └── web_search.py
├── .env
├── .gitignore
├── requirements.txt

frontend/
├── public/
├── src/
│   ├── App.jsx
│   └── index.js
```

---

##  Installation backend

```bash
git clone https://github.com/ton-pseudo/ton-repo.git
cd ton-repo/backend
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows
pip install -r requirements.txt
```

###  Ajouter le fichier `.env`

```env
OPENROUTER_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
SERPAPI_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

###  Lancer le backend

```bash
uvicorn app.main:app --reload
```

Swagger disponible sur : http://127.0.0.1:8000/docs

---

##  Lancer le frontend

```bash
cd ../frontend
npm install
npm start
```

Accessible sur : http://localhost:3000

---

##  Fonctionnement interne

1. Appel à `search_web(prompt)` via SerpAPI
2. Résultats injectés dans un prompt enrichi
3. Envoi au modèle (OpenRouter ou local)
4. Génération de réponse basée sur les sources

---

##  Exemple de prompt généré

```
Voici des informations trouvées en ligne :

[1] OpenAI annonce GPT-5 - https://openai.com/gpt5
OpenAI prévoit de sortir GPT-5 avec une capacité multimodale améliorée...

[2] Google lance Gemini 1.5 - https://blog.google/ai/gemini
Le modèle Gemini introduit une architecture plus modulaire...

[3] Stability AI sort Stable LM 2 - https://stability.ai/news
StableLM 2 permet un meilleur contrôle générationnel...

À partir de ces sources, réponds à la question suivante de manière synthétique et précise :
Quels sont les derniers développements en IA générative cette semaine ?
```

## Partie 2 – Questions théoriques sur le chatbot avec accès internet

Dans le cadre de ce projet, je propose un plan de déploiement sur Azure conçu pour répondre aux exigences d’un grand groupe en matière de scalabilité, de sécurité, de fiabilité et de maintenabilité. L’objectif est d’anticiper une mise en production réaliste et professionnelle, en structurant chaque étape du déploiement et en justifiant les choix techniques retenus.

La solution développée repose sur deux composants bien distincts. D’une part, un backend en Python (FastAPI) chargé de la logique métier, des appels au LLM via OpenRouter, et de la recherche web via une API comme SerpAPI ou DuckDuckGo. D’autre part, un frontend en React destiné à fournir à l’utilisateur une interface claire et ergonomique pour interagir avec le chatbot.

Je recommande une séparation stricte entre le frontend et le backend, car elle garantit deux avantages majeurs. D’abord, cela permet une scalabilité indépendante de chaque composant : en cas de forte charge sur l’API (par exemple un pic de requêtes vers OpenRouter), seul le backend devra être renforcé. Ensuite, cela assure une séparation nette des responsabilités : le frontend se concentre sur l’affichage et l’expérience utilisateur, tandis que le backend gère les traitements, les appels API, les erreurs et la sécurité. Cette architecture modulaire facilite également les mises à jour, les tests et la maintenance.

Pour héberger cette solution sur Azure, je préconise la création des ressources suivantes :

1. **Azure App Service** (Plan Standard S1) pour le backend Python. Ce service permet un déploiement simple, une montée en charge automatique, une intégration native avec Key Vault et Application Insights, et offre une disponibilité de 99,95 %. Le plan gratuit ne propose pas ces fonctionnalités critiques. Le plan S1 constitue donc un bon compromis entre performance et coût, estimé à 77,939 euros par mois.

2. **Azure Static Web Apps** (Plan Standard) pour le frontend React. Ce service fournit un hébergement statique performant, via un CDN global, avec déploiement automatisé depuis GitHub, certificat SSL intégré et compatibilité avec les domaines personnalisés. Le plan Standard est adapté à une diffusion fiable et sécurisée, avec un coût de 84,558 euros par mois.

3. **Azure Key Vault** (niveau Standard) pour stocker de manière sécurisée les secrets, tels que les clés API utilisées par le backend. L'accès aux secrets s’effectue via une **Managed Identity** configurée sur App Service. Cette méthode permet d’éviter tout mot de passe ou clé dans le code source. À raison de deux lectures de secret par requête (OpenRouter et SerpAPI), avec une hypothèse de 2 000 requêtes par jour, on atteint 4 000 lectures par jour, soit 120 000 lectures par mois. Le tarif étant de 0,026 € pour 10 000 opérations, le coût mensuel est de 0,312 €.

4. **Azure Application Insights** pour le monitoring du backend. Ce service permet de collecter automatiquement les erreurs, les exceptions, les temps de réponse et les journaux d’activité. En moyenne, chaque requête génère une quinzaine d’événements (appels API, logs d’entrée/sortie, erreurs potentielles, etc.). Avec 2 000 requêtes par jour, cela représente environ 30 000 événements quotidiens, soit entre 0,5 et 0,9 Go de données par mois. Le quota gratuit de 5 Go/mois permet de couvrir ces besoins sans surcoût.

En ce qui concerne la gestion des accès, je propose de suivre une logique de moindre privilège. Les rôles “Contributor” seraient affectés aux développeurs sur le groupe de ressources Azure, tandis que l’accès aux secrets serait restreint via un rôle “Key Vault Reader” attribué à l’App Service via une identité managée. GitHub Actions disposerait d’un accès délégué à App Service et Static Web Apps via un service principal sécurisé ou OpenID Connect, pour automatiser les déploiements sans manipulation manuelle de clés.

La mise en production serait automatisée via GitHub Actions. Le pipeline du backend inclurait une étape de **linting** avec *flake8*, afin de garantir la conformité du code aux standards Python (structure, lisibilité, conventions). Ensuite, les **tests unitaires** seraient exécutés via *pytest*, pour valider les comportements critiques (gestion des erreurs, cohérence des réponses, etc.). En cas de succès, le déploiement serait automatiquement déclenché vers Azure App Service. Le frontend suivrait un pipeline similaire : build React puis déploiement sur Static Web Apps.

Pour garantir la stabilité de l’application en production, Application Insights assurerait une supervision continue. Des alertes seraient configurées pour remonter les anomalies critiques (erreurs 5xx, lenteurs, exceptions non gérées). La gestion des erreurs serait centralisée dans le backend : chaque appel critique serait encapsulé dans un bloc `try/except`, permettant de logguer les incidents (type d’exception, code retour, temps écoulé, etc.), tout en renvoyant un message utilisateur clair.

Enfin, une stratégie de sauvegarde et de reprise serait mise en place. Le code est versionné sur GitHub, les secrets sont centralisés dans Key Vault, et la configuration Azure est exportable via CLI. En cas de besoin, une restauration rapide serait possible à partir de scripts Terraform ou ARM. Les journaux pourraient également être archivés dans Azure Blob Storage pour conservation longue durée.

Cette architecture repose sur des composants découplés, maintenables et évolutifs. Elle offre une séparation claire des responsabilités, une sécurité robuste, une supervision fiable et un déploiement entièrement automatisé. Le tout pour un coût total estimé à **162,809 euros par mois**, ce qui reste cohérent et justifié pour un déploiement professionnel au sein d’un grand groupe.


## Partie 3 – Vision Language Models

**Remarque** : La partie technique des Vision Language Models n’a pas pu être réalisée faute de matériel compatible (GPU avec au moins 8 Go de VRAM). Cette section présente donc uniquement l’approche théorique détaillée.

### 1. Extraction multimodale

Le pipeline commence par une étape d’extraction où l’on identifie les blocs de texte ainsi que les éléments visuels du document. Chaque image est associée à son paragraphe ou à sa légende la plus proche en utilisant des règles de proximité et de structure (par exemple, une image insérée entre deux paragraphes sera liée au paragraphe précédent). Ce couplage image + texte est indispensable pour la compréhension contextuelle.

### 2. Encodage avec un VLM

Chaque couple image + texte est ensuite envoyé à un **Vision Language Model** (par exemple : Qwen-VL, BLIP-2, Kosmos-2). Ce modèle prend les deux modalités en entrée et génère un **embedding unifié**, c’est-à-dire une représentation vectorielle unique qui capture à la fois le contenu visuel, le contenu textuel, et surtout leur lien sémantique.

Contrairement à une approche qui vectorise séparément texte et image, puis fusionne les deux vecteurs, l’encodage unifié permet d’obtenir directement une représentation cohérente et intégrée.

### 3. Indexation vectorielle

Les vecteurs produits par le VLM sont stockés dans une base vectorielle (telle que FAISS, Qdrant ou Weaviate). Chaque vecteur est enrichi de métadonnées (page, source, type de contenu, etc.) permettant une recherche plus fine. Les documents sont découpés en chunks multimodaux pour garantir la granularité des recherches.

### 4. Recherche et génération (RAG)

Lorsqu’un utilisateur pose une question en langage naturel, celle-ci est encodée avec le **même VLM** que celui utilisé pour les documents. La base vectorielle est interrogée par similarité pour identifier les chunks multimodaux les plus proches sémantiquement.

Les résultats sont ensuite concaténés et transmis comme **contexte** à un **modèle génératif** (par exemple GPT, Mistral, Qwen), qui peut alors produire une réponse ancrée dans les documents, en tenant compte à la fois du texte et des éléments visuels.

## Avantages de l’approche

- **Cohérence sémantique** : l’encodage unifié garantit que les relations entre texte et image sont conservées dès l’entrée du modèle.
- **Simplicité du pipeline** : un seul modèle est utilisé pour encoder les documents et les requêtes.
- **Pertinence des réponses** : le LLM accède à des contextes riches et structurés, même lorsqu’ils reposent sur des éléments visuels.
- **Scalabilité** : les vecteurs peuvent être précalculés et stockés, et chaque étape du pipeline peut être containerisée ou orchestrée séparément.
