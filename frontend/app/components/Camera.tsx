"use client";

import { useRef, useState } from "react";
import axios from "axios";

export default function Camera() {

  const videoRef = useRef<HTMLVideoElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);

  const [description, setDescription] = useState("");
  const [audioUrl, setAudioUrl] = useState("");

  const startCamera = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });

    if (videoRef.current) {
      videoRef.current.srcObject = stream;
    }
  };

  const captureFrame = async () => {
    const canvas = canvasRef.current;
    const video = videoRef.current;

    if (!canvas || !video) return;

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const ctx = canvas.getContext("2d");
    ctx?.drawImage(video, 0, 0);

    canvas.toBlob(async (blob) => {
      if (!blob) return;

      const formData = new FormData();
      formData.append("file", blob, "frame.jpg");

      const res = await axios.post(
        "http://127.0.0.1:8000/analyze-frame",
        formData
      );

      setDescription(res.data.description);
      setAudioUrl("http://127.0.0.1:8000" + res.data.audio_url);
    });
  };

  return (
    <div className="flex flex-col items-center gap-6">

      <video
        ref={videoRef}
        autoPlay
        className="w-[500px] rounded-lg border"
      />

      <div className="flex gap-4">

        <button
          onClick={startCamera}
          className="bg-blue-500 text-white px-4 py-2 rounded"
        >
          Start Camera
        </button>

        <button
          onClick={captureFrame}
          className="bg-green-500 text-white px-4 py-2 rounded"
        >
          Analyze Scene
        </button>

      </div>

      <p className="text-lg font-semibold text-center">
        {description}
      </p>

      {audioUrl && (
        <audio controls autoPlay>
          <source src={audioUrl} type="audio/mp3" />
        </audio>
      )}

      <canvas ref={canvasRef} className="hidden" />

    </div>
  );
}