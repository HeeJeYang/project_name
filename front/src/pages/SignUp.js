import React from "react";
import { useMediaQuery } from "react-responsive";

// Components
import SignUpForm from "../components/Forms/SignUpForm";

const SignUp = () => {
  const isBigScreen = useMediaQuery({ query: "(min-width: 768px)" });
  const isSmallScreen = useMediaQuery({ query: "(max-width: 768px)" });
  return (
    <div className="SignUp">
      {isBigScreen && (
        <div className="big_screen">
          <div className="signup_poster_wrapper">
            <img
              src={`${process.env.PUBLIC_URL}/assets/poster/poster1.png`}
              alt="signup_poster"
            />
          </div>
          <div className="signup_form_wrapper">
            <SignUpForm />
          </div>
        </div>
      )}
      {isSmallScreen && (
        <div className="small_screen">
          <div className="signup_form_wrapper">
            <SignUpForm />
          </div>
        </div>
      )}
    </div>
  );
};

export default SignUp;
