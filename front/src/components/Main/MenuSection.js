const MenuSection = ({ type, title, content }) => {
  return (
    <div className="MenuSection">
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
