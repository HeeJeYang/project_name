import Button from "react-bootstrap/Button";
import { Form } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

const LoginForm = () => {
  return (
    <Form className="LoginForm">
      <div className="login_form_title">
        <h2>LOGIN</h2>
      </div>
      <div className="login_form_username">
        <FontAwesomeIcon icon="fa-solid fa-user" />
        <Form.Control
          type="text"
          placeholder="아이디"
          autoComplete="username"
        />
      </div>
      <div className="login_form_password">
        <FontAwesomeIcon icon="fa-solid fa-lock" />
        <Form.Control
          type="password"
          placeholder="비밀번호"
          autoComplete="current-password"
        />
      </div>
      <div className="login_form_button">
        <Button variant="secondary">로그인</Button>
      </div>
      <div className="login_form_button">
        <Button variant="secondary">회원가입</Button>
      </div>
      <div className="login_form_option_line">
        <div className="line"></div>
        <div className="text">OR</div>
        <div className="line"></div>
      </div>
      <div className="login_form_button">
        {/* <Button>구글로 로그인</Button> */}
        <Button variant="light">
          <FontAwesomeIcon icon="fa-brands fa-google" />
          <span> 구글로 로그인</span>
        </Button>
      </div>
    </Form>
  );
};

export default LoginForm;
