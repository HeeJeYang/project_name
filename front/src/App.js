import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./App.css";

// Pages
import Home from "./pages/Home";

// Components
import MyHeader from "./components/MyHeader";

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <MyHeader />
        <h2>App.js</h2>
        <Routes>
          <Route path="/" element={<Home />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
