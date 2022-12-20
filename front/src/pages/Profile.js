import { Link } from "react-router-dom";

const Profile = () => {
  return (
    <div className="Profile">
      <div className="profile_user_box">
        <div className="profile_user_image">
          <img
            src={`${process.env.PUBLIC_URL}/assets/ssafy_logo.png`}
            alt="user_image"
          />
        </div>
        <div className="profile_user_info">
          <div className="profile_user_name_box">
            <span className="profile_user_name fs-3 fw-bold">홍길동</span>
            <span className="profile_user_name">honghong22</span>
          </div>
          <div className="profile_user_introduction">
            동에 번쩍~! 서에 번쩍~!
          </div>
        </div>
      </div>
      <div className="profile_nav">
        <ul className="nav nav-tabs">
          <li className="nav-item">
            <div className="nav-link active" aria-current="page">
              대시보드
            </div>
          </li>
          <li className="nav-item">
            <Link className="nav-link" to="/edit">
              내 정보 관리
            </Link>
          </li>
        </ul>
      </div>
      <div className="profile_dashboard">
        <div className="profile_dashboard_category">찜한 레시피</div>
        <div className="profile_dashboard_category">최근 작성한 게시물</div>
      </div>
    </div>
  );
};

export default Profile;
