import { useNavigate } from "react-router-dom";

const MenuSection = ({ type, title, content, page }) => {
  const navigate = useNavigate();
  return (
    <div
      className="MenuSection"
      onClick={() => {
        console.log("clicked");
        navigate(page);
      }}
    >
      <div className={["menu", `menu_${type}`].join(" ")}>
        <div>
          <div className="menu_title">{title}</div>
          <div className="menu_content">{content}</div>
        </div>
      </div>
    </div>
  );
};

export default MenuSection;
