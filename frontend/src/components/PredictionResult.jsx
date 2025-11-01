import React from "react";

function PredictionResult({ result, image }) {
  if (!result) return null;

  return (
    <div className="result-box">
      <h2>🩺 Prediction Result</h2>

      {image && (
        <img
          src={URL.createObjectURL(image)}
          alt="Uploaded Crop"
          className="result-image"
        />
      )}

      <p className="result-text">{result}</p>
    </div>
  );
}

export default PredictionResult;
