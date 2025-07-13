# 💬 Chatbot IA Générative avec Recherche Web – Test Technique Juillet 2025

## 🎯 Objectif du projet

Ce projet a été réalisé dans le cadre d’un test technique pour un poste d’**Ingénieur IA Générative**.  
L’objectif était de développer un **chatbot capable d’interroger un LLM** tout en intégrant dynamiquement des **résultats de recherche web récents**, afin de fournir des réponses contextualisées et à jour.

> ✅ Requête test attendue :
> *“Quels sont les derniers développements en IA générative annoncés cette semaine ? Donne-moi 3 exemples concrets avec leurs sources.”*

Le projet inclut :
- Une API REST backend construite avec **FastAPI**
- Une logique de **recherche web automatique**
- Deux modes de génération :
  - Un modèle cloud via **OpenRouter**
  - Un modèle local via **Hugging Face Transformers**

---

## 🧱 Stack technique

| Composant      | Outil utilisé                                       |
|----------------|-----------------------------------------------------|
| **Langage**    | Python 3.10+                                        |
| **Framework API** | FastAPI + Uvicorn                              |
| **Recherche Web** | `duckduckgo_search` (API gratuite DuckDuckGo)  |
| **LLM Cloud**  | `qwen/qwen2.5-vl-32b-instruct:free` (OpenRouter)   |
| **LLM Local**  | `microsoft/phi-2` via HuggingFace Transformers     |
| **Frontend**   | *(à venir)* – prévu en React                       |

---

## 🚀 Fonctionnalités principales

- 🔎 **Recherche web dynamique** : intégration des résultats dans les prompts
- 🤖 **Double mode de réponse** :
  - `/ask` → via modèle distant (OpenRouter)
  - `/ask-local` → via modèle local (Hugging Face)
- 🧠 **Prompt enrichi** : les résultats web sont injectés dans la requête du LLM
- 🔐 **Sécurité** : les clés API sont stockées dans un fichier `.env` non versionné
- 🧪 **Interface Swagger** pour tester facilement l’API

---

## 🧪 Exemple de fonctionnement

Requête envoyée :
```json
{
  "prompt": "Quels sont les derniers développements en IA générative cette semaine ?"
}
```

Processus :
1. Recherche web automatique (DuckDuckGo)
2. Résumé des 3 meilleurs résultats (titre, URL, extrait)
3. Construction d’un **prompt enrichi**
4. Envoi au modèle (local ou distant)
5. Réponse générée et retournée à l’utilisateur

---

## 📂 Structure du projet

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
```

---

## ⚙️ Installation du projet

### 🧱 1. Cloner le dépôt
```bash
git clone https://github.com/ton-pseudo/ton-repo.git
cd ton-repo/backend
```

### 🐍 2. Créer un environnement virtuel Python
```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows
```

### 📦 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 🔐 4. Ajouter le fichier `.env`
```env
OPENROUTER_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

---

## ▶️ Lancement de l’API

```bash
uvicorn app.main:app --reload
```

Swagger : http://127.0.0.1:8000/docs

---

## 📤 Endpoints disponibles

### `/ask` – version cloud (OpenRouter)
```json
POST /ask
{
  "prompt": "Quelle est l'utilité de l'IA générative dans la médecine ?"
}
```

### `/ask-local` – version locale (Phi-2)
```json
POST /ask-local
{
  "prompt": "Quels sont les avantages de l’IA en éducation ?"
}
```

---

## 🔎 Fonctionnement interne

1. Appel à `search_web(prompt)`
2. Résultats injectés dans un prompt enrichi
3. Envoi au modèle (cloud ou local)
4. Réponse générée à partir des sources web

---

## 📌 Exemple de prompt généré

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

---

## 💡 Bonus techniques inclus

| Élément                            | Implémenté |
|------------------------------------|------------|
| Intégration des résultats web      | ✅         |
| Modèle cloud via OpenRouter        | ✅         |
| Modèle local via Hugging Face      | ✅         |
| Fonctionnement hors-ligne          | ✅         |
| Swagger UI                         | ✅         |
| Séparation `.env` / `.gitignore`  | ✅         |

---

## 📚 Améliorations prévues

- 🌐 Frontend React
- ☁️ Déploiement Azure (Partie 2)
- 🖼️ Intégration VLM (Partie 3)

---

## 👤 Réalisé par

**Théo Labat**  
Test Technique – Ingénieur IA Générative – Juillet 2025

---

## 📝 Remarques

- Aucune clé API n’est versionnée
- Aucune solution payante n’a été utilisée
- Toutes les hypothèses sont documentées dans ce fichier