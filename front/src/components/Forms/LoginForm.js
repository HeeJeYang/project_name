import axios from "axios";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

// Components
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

const LoginForm = ({ handleResponseSuccess }) => {
  const [errorMessage, setErrorMessage] = useState();
  const [loginInfo, setLoginInfo] = useState({
    username: "",
    password: "",
  });

  const handleInputValue = (key) => (e) => {
    setLoginInfo({ ...loginInfo, [key]: e.target.value });
  };

  const handleLogin = () => {
    if (!loginInfo.username || !loginInfo.password) {
      return setErrorMessage("아이디와 비밀번호를 입력하세요.");
    }
    axios({
      method: "post",
      url: `${process.env.REACT_APP_SERVER_URL}/accounts/login/`,
      data: {
        username: loginInfo.username,
        password: loginInfo.password,
      },
    })
      .then((res) => {
        // 저장해야 함
        console.log(res);
        navigate("/");
      })
      .catch((err) => {
        console.log("로그인 에러: ", err);
      });
  };

  const navigate = useNavigate();

  return (
    <form className="LoginForm" onSubmit={(e) => e.preventDefault()}>
      <div className="login_form_title">
        <h2>LOGIN</h2>
      </div>
      <div className="login_form_username">
        <FontAwesomeIcon icon="fa-solid fa-user" />
        <input
          type="text"
          placeholder="아이디"
          autoComplete="username"
          onChange={handleInputValue("username")}
        />
      </div>
      <div className="login_form_password">
        <FontAwesomeIcon icon="fa-solid fa-lock" />
        <input
          type="password"
          placeholder="비밀번호"
          autoComplete="current-password"
          onChange={handleInputValue("password")}
        />
      </div>
      <div>
        <span>{errorMessage}</span>
      </div>
      <div className="login_form_button">
        <button type="submit" variant="secondary" onClick={handleLogin}>
          로그인
        </button>
      </div>
      <div className="login_form_button">
        <button onClick={() => navigate("/signup")} variant="secondary">
          회원가입
        </button>
      </div>
      <div className="login_form_option_line">
        <div className="line"></div>
        <div className="text">OR</div>
        <div className="line"></div>
      </div>
      <div className="login_form_button">
        {/* <Button>구글로 로그인</Button> */}
        <button variant="light">
          <FontAwesomeIcon icon="fa-brands fa-google" />
          <span> 구글로 로그인</span>
        </button>
      </div>
    </form>
  );
};

export default LoginForm;
