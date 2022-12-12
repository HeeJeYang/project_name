import { BrowserRouter, Route, Routes } from "react-router-dom";

import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

// FontAwesome
import { library } from "@fortawesome/fontawesome-svg-core";
import { faGoogle } from "@fortawesome/free-brands-svg-icons";
import { faUser, faLock } from "@fortawesome/free-solid-svg-icons";

// Pages
import Main from "./pages/Main";
import Login from "./pages/Login";

// Components
import Container from "react-bootstrap/Container";
import MyHeader from "./components/MyHeader";

library.add(faUser, faLock, faGoogle);

function App() {
  return (
    <BrowserRouter>
      <Container fluid className="App">
        <MyHeader />
        <Routes>
          <Route path="/" element={<Main />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </Container>
    </BrowserRouter>
  );
}

export default App;
