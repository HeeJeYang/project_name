import { BrowserRouter, Route, Routes } from "react-router-dom";

import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

// Pages
import Main from "./pages/Main";

// Components
import Container from "react-bootstrap/Container";
import MyHeader from "./components/MyHeader";

function App() {
  return (
    <BrowserRouter>
      <Container fluid className="App">
        <MyHeader />
        <Routes>
          <Route path="/" element={<Main />} />
        </Routes>
      </Container>
    </BrowserRouter>
  );
}

export default App;
