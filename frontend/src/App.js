import React, { useState } from "react";
import Header from "./components/Header";
import ImageUpload from "./components/ImageUpload";
import PredictionResult from "./components/PredictionResult";
import "./App.css";

function App() {
  const [result, setResult] = useState("");
  const [image, setImage] = useState(null);

  return (
    <div className="App">
      <Header />
      <ImageUpload onResult={setResult} onImageSelect={setImage} />
      <PredictionResult result={result} image={image} />
    </div>
  );
}

export default App;
