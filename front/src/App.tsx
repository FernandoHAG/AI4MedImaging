import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";
import Loader from "./components/loader/Loader";

const backendURL = "http://localhost:8080/";

function App() {
  const [count, setCount] = useState(0);
  const [loading, setLoading] = useState(true);

  const fetchAPI = async () => {
    try {
      const response = await axios.get(backendURL);
      if (response.data == "OK") {
        setLoading(false);
      } else {
        setTimeout(fetchAPI, 1000);
      }
    } catch (error) {
      console.error(error);
      setTimeout(fetchAPI, 1000);
    }
  };

  useEffect(() => {
    const intervalId = setTimeout(fetchAPI, 1000);
    return () => clearInterval(intervalId);
  }, []);

  return (
    <>
      {loading ? (
        <Loader />
      ) : (
        <>
          <h1>Vite + React</h1>
          <div className="card">
            <button onClick={() => setCount((count) => count + 1)}>
              count is {count}
            </button>
          </div>
        </>
      )}
    </>
  );
}

export default App;
