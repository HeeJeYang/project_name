import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./App.css";

// Components
import Home from "./pages/Home";

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <h2>App.js</h2>
        <Routes>
          <Route path="/" element={<Home />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
