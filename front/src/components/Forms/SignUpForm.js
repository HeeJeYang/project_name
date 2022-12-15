import axios from "axios";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

// Components
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

const SignUpForm = ({ handleResponseSuccess }) => {
  const [errorMessage, setErrorMessage] = useState();
  const [signUpInfo, setSignUpInfo] = useState({
    username: "",
    nickname: "",
    password1: "",
    password2: "",
  });

  const handleInputValue = (key) => (e) => {
    setSignUpInfo({ ...signUpInfo, [key]: e.target.value });
  };

  const handleSignUp = () => {
    if (
      !signUpInfo.username ||
      !signUpInfo.nickname ||
      !signUpInfo.password1 ||
      !signUpInfo.password2
    ) {
      return setErrorMessage("빈 칸을 채워주세요.");
    }
    axios({
      method: "post",
      url: `${process.env.REACT_APP_SERVER_URL}/accounts/signup/`,
      data: {
        username: signUpInfo.username,
        nickname: signUpInfo.nickname,
        password1: signUpInfo.password1,
        password2: signUpInfo.password2,
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
    <form className="SignUpForm" onSubmit={(e) => e.preventDefault()}>
      <div className="signup_form_title">
        <h2>SIGNUP</h2>
      </div>
      <div className="signup_form_input">
        <FontAwesomeIcon icon="fa-solid fa-user" />
        <input
          type="text"
          placeholder="아이디"
          autoComplete="username"
          onChange={handleInputValue("username")}
        />
      </div>
      <div className="signup_form_input">
        <FontAwesomeIcon icon="fa-solid fa-user" />
        <input
          type="text"
          placeholder="닉네임"
          autoComplete="nickname"
          onChange={handleInputValue("nickname")}
        />
      </div>
      <div className="signup_form_input">
        <FontAwesomeIcon icon="fa-solid fa-lock" />
        <input
          type="password"
          placeholder="비밀번호"
          autoComplete="current-password"
          onChange={handleInputValue("password1")}
        />
      </div>
      <div className="signup_form_input">
        <FontAwesomeIcon icon="fa-solid fa-lock" />
        <input
          type="password"
          placeholder="비밀번호 확인"
          autoComplete="check-password"
          onChange={handleInputValue("password2")}
        />
      </div>
      <div>
        <span>{errorMessage}</span>
      </div>
      <div className="signup_form_button_wrapper">
        <div className="signup_form_button">
          <button type="submit" variant="secondary" onClick={handleSignUp}>
            가입하기
          </button>
        </div>
        <div className="signup_form_button">
          <button onClick={() => navigate("/login")} variant="secondary">
            취소
          </button>
        </div>
      </div>
    </form>
  );
};

export default SignUpForm;
