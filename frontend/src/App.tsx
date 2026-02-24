import { useEffect, useState } from "react";

import "./App.css";

function App() {
  const [health, setHealth] = useState<string | null>(null);

  useEffect(() => {
    const getHealthCheck = async () => {
      const response = await fetch("http://localhost:8000/health");
      const data = await response.json();
      setHealth(data.status);
    };

    getHealthCheck();
  }, []);

  return (
    <>
      <div>Response: {health}</div>
    </>
  );
}

export default App;
