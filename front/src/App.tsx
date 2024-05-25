import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";
import Loader from "./components/loader/Loader";

const backendURL = "http://localhost:8080/";

function App() {
  const [count, setCount] = useState(0);

  const fetchAPI = async () => {
    const response = await axios.get(backendURL);
    console.log(response.data);
  };

  useEffect(() => {
    fetchAPI();
  }, []);

  return (
    <>
      {Loader()}
      {false && (
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
