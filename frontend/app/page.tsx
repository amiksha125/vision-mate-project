

import Camera from "./components/Camera";

export default function Home() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen gap-6">
      <h1 className="text-4xl font-bold">
        VisionMate
      </h1>

      <Camera />
    </main>
  );
}