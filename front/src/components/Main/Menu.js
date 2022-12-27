// Components
import MenuSection from "./MenuSection";
import MenuRecommend from "./MenuRecommend";

const MenuSectionInfo = {
  left_top: {
    type: "left_top",
    title: "레시피",
    content: "클릭 시 레시피 페이지로 이동합니다.",
    page: "/recipe",
  },
  right_top: {
    type: "right_top",
    title: "재료를 통한 레시피 검색",
    content: "클릭 시 재료를 통한 레시피 검색 페이지로 이동합니다.",
    page: "/search-recipe",
  },
  left_bottom: {
    type: "left_bottom",
    title: "나만의 식단",
    content: "클릭 시 나만의 식단 페이지로 이동합니다.",
    page: "/",
  },
  right_bottom: {
    type: "right_bottom",
    title: "커뮤니티",
    content: "클릭 시 커뮤니티 페이지로 이동합니다.",
    page: "/community",
  },
};

const Menu = () => {
  return (
    <section className="Menu">
      <MenuRecommend />
      <div className="MenuSection_wrapper">
        <MenuSection {...MenuSectionInfo["left_top"]} />
        <MenuSection {...MenuSectionInfo["right_top"]} />
      </div>
      <div className="MenuSection_wrapper">
        <MenuSection {...MenuSectionInfo["left_bottom"]} />
        <MenuSection {...MenuSectionInfo["right_bottom"]} />
      </div>
    </section>
  );
};

export default Menu;
