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
          style={{
            width: "250px",
            height: "250px",
            objectFit: "cover",
            borderRadius: "10px",
            marginBottom: "15px",
          }}
        />
      )}

      <div className="result-content">
        <h3>🌿 Disease: {result.label}</h3>
        <p>
          <strong>Confidence:</strong> {result.confidence}%
        </p>

        {result.details && (
          <>
            <p>
              <strong>Description:</strong>{" "}
              {result.details.description || "No description available"}
            </p>
            <p>
              <strong>Solution:</strong>{" "}
              {result.details.solution || "No solution available"}
            </p>
          </>
        )}
      </div>
    </div>
  );
}

export default PredictionResult;
