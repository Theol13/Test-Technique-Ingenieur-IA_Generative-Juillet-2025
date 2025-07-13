import { useState } from "react";

function App() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");
  const [mode, setMode] = useState("cloud");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!prompt) return;
    setLoading(true);
    setResponse("Chargement...");

    const endpoint = mode === "cloud" ? "ask" : "ask-local";

    try {
      const res = await fetch(`http://127.0.0.1:8000/${endpoint}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt }),
      });

      const data = await res.json();
      setResponse(data.response || "Aucune réponse");
    } catch (err) {
      setResponse("Erreur lors de l’appel au backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>Chatbot IA Générative</h1>

      <textarea
        rows={4}
        cols={60}
        placeholder="Pose ta question ici..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <div style={{ margin: "1rem 0" }}>
        <label>
          <input
            type="radio"
            name="mode"
            value="cloud"
            checked={mode === "cloud"}
            onChange={() => setMode("cloud")}
          />
          Cloud
        </label>
        <label style={{ marginLeft: "1rem" }}>
          <input
            type="radio"
            name="mode"
            value="local"
            checked={mode === "local"}
            onChange={() => setMode("local")}
          />
          Local
        </label>
      </div>

      <button onClick={handleSubmit} disabled={loading}>
        Envoyer
      </button>

      <h3>Réponse :</h3>
      <pre style={{ background: "#f4f4f4", padding: "1rem" }}>{response}</pre>
    </div>
  );
}

export default App;