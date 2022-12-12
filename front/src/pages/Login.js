import LoginForm from "../components/Forms/LoginForm";

const Login = () => {
  return (
    <div className="Login">
      <div className="login_poster_wrapper">
        <img
          src={`${process.env.PUBLIC_URL}/assets/poster/poster1.png`}
          alt="login_poster"
        />
      </div>
      <div className="login_form_wrapper">
        <LoginForm />
      </div>
    </div>
  );
};

export default Login;
