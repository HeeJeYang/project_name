import { Link } from "react-router-dom";

const Edit = () => {
  return (
    <div className="Edit">
      <div className="edit_user_box">
        <div className="edit_user_image">
          <img
            src={`${process.env.PUBLIC_URL}/assets/ssafy_logo.png`}
            alt="user_image"
          />
        </div>
        <div className="edit_user_profile">
          <div className="edit_user_name_box">
            <span className="edit_user_name fs-3 fw-bold">홍길동</span>
            <span className="edit_user_name">honghong22</span>
          </div>
          <div className="edit_user_introduction">동에 번쩍~! 서에 번쩍~!</div>
        </div>
      </div>
      <div className="edit_nav">
        <ul className="nav nav-tabs">
          <li className="nav-item">
            <Link className="nav-link" to="/profile">
              대시보드
            </Link>
          </li>
          <li className="nav-item">
            <div className="nav-link active" aria-current="page">
              내 정보 관리
            </div>
          </li>
        </ul>
      </div>
      <div className="edit_user_info">
        <div className="edit_user_info_wrapper">
          <div className="edit_user_info_box">
            <div className="edit_user_profile_image_change_box">
              <div className="edit_user_profile_image_preview">
                <img
                  src={`${process.env.PUBLIC_URL}/assets/ssafy_logo.png`}
                  alt="profile_image_proview"
                />
              </div>
              <div className="edit_user_profile_change_image_box"></div>
            </div>
            <div></div>
            <div></div>
            <textarea></textarea>
            <div></div>
            <div></div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Edit;
