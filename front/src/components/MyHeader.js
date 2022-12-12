// Components
import { useNavigate } from "react-router-dom";
import HeaderMenu from "./HeaderMenu";

const MyHeader = () => {
  const navigate = useNavigate();

  return (
    <header className="MyHeader">
      <div className="header_info">
        <div className="header_logo">
          <img
            src={`${process.env.PUBLIC_URL}/assets/ssafy_logo.png`}
            alt="header_logo"
          />
        </div>
        <div className="header_search_bar">
          <input placeholder="검색창" />
        </div>
        <div className="header_profile_menu">
          <div onClick={() => navigate("/login")}>테스트</div>
        </div>
      </div>
      <HeaderMenu />
    </header>
  );
};

export default MyHeader;
