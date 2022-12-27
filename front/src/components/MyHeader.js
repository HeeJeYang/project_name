// Components
import { Link, useNavigate } from "react-router-dom";
import HeaderMenu from "./HeaderMenu";

const MyHeader = () => {
  const navigate = useNavigate();

  return (
    <header className="MyHeader">
      <div className="header_info">
        <div className="header_logo" onClick={() => navigate("/")}>
          <img
            src={`${process.env.PUBLIC_URL}/assets/ssafy_logo.png`}
            alt="header_logo"
          />
        </div>
        <div className="header_search_bar">
          <input placeholder="검색창" />
        </div>
        <div className="header_profile_menu">
          <button
            type="button"
            className="btn btn-light dropdown-toggle"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            <img
              className="header_profile_image"
              src={`${process.env.PUBLIC_URL}/assets/ssafy_logo.png`}
              alt="profile_image"
            />
          </button>
          <ul className="dropdown-menu dropdown-menu-end">
            <li>
              <Link className="dropdown-item" to="/profile">
                프로필 보기
              </Link>
            </li>
            <li>
              <Link className="dropdown-item" to="/edit">
                개인정보 수정
              </Link>
            </li>
            <li>
              <hr className="dropdown-divider" />
            </li>
            <li>
              <div className="dropdown-item" onClick={() => {}}>
                로그아웃
              </div>
            </li>
          </ul>
        </div>
      </div>
      <HeaderMenu />
    </header>
  );
};

export default MyHeader;
