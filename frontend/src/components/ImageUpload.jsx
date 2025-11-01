import React, { useState } from "react";
import axios from "axios";

function ImageUpload({ onResult, onImageSelect }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  // when user selects file
  const handleFileChange = (e) => {
    const selected = e.target.files[0];
    if (selected) {
      setFile(selected);
      onImageSelect(selected);
    }
  };

  // when user clicks upload
  const handleUpload = async () => {
    if (!file) {
      alert("Please select an image first!");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      const response = await axios.post("http://127.0.0.1:5000/predict", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      onResult(response.data.prediction);
    } catch (error) {
      console.error(error);
      alert("Error connecting to Flask backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="upload-box">
      <input type="file" accept="image/*" onChange={handleFileChange} />
      <br />

      {/* 🖼️ Show preview if file is selected */}
      {file && (
        <div style={{ marginTop: "15px" }}>
          <img
            src={URL.createObjectURL(file)}
            alt="Preview"
            style={{
              width: "200px",
              height: "200px",
              objectFit: "cover",
              borderRadius: "10px",
              border: "2px solid #4caf50",
            }}
          />
        </div>
      )}

      <br />
      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Detecting..." : "Upload & Detect"}
      </button>
    </div>
  );
}

export default ImageUpload;
