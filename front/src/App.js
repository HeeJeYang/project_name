import { BrowserRouter, Route, Routes } from "react-router-dom";

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";
import "./App.css";

// FontAwesome
import { library } from "@fortawesome/fontawesome-svg-core";
import { faGoogle } from "@fortawesome/free-brands-svg-icons";
import { faUser, faLock } from "@fortawesome/free-solid-svg-icons";

// Pages
import Main from "./pages/Main";
import Login from "./pages/Login";
import SignUp from "./pages/SignUp";
import Profile from "./pages/Profile";
import Edit from "./pages/Edit";

// Components
import MyHeader from "./components/MyHeader";

library.add(faUser, faLock, faGoogle);

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <div className="container">
          <MyHeader />
          <Routes>
            <Route path="/" element={<Main />} />
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<SignUp />} />
            <Route path="/profile" element={<Profile />} />
            <Route path="/edit" element={<Edit />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;
