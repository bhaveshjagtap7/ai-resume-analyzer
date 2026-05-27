import { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("resume", file);

    const res = await fetch( {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setResult(data);
  };

  return (
    <div className="container">
      <h1 className="title">AI Resume Analyzer</h1>

      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <br />

      <button onClick={handleUpload}>Upload Resume</button>

      {result && (
        <div className="result">
          <div className="score">Score: {result.score}/100</div>

          <div className="skills">
            <h4>Skills:</h4>
            {result.skills.map((s, i) => (
              <span key={i} className="skill-item">
                {s}
              </span>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
