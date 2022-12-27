import styled from "styled-components";

// Components
import Title from "../components/Text/Title";
import SubTitle from "../components/Text/SubTitle";
import SearchInput from "../components/Input/SearchInput";
import FilterButton from "../components/Button/FilterButton";
import CommunityCard from "../components/Card/CommunityCard";

const Community = () => {
  return (
    <Wrapper>
      <Title content={"자유 게시판"} />
      <SubTitle content={"자유롭게 자신만의 레시피를 서로 공유해보기"} />
      <SearchInput />
      {/* map으로 줄일 수 있겠는데? */}
      <FilterBox>
        <FilterButton content={"전체"} color={"primary"} />
        <FilterButton content={"나만의 레시피"} color={"danger"} />
        <FilterButton content={"분리수거 하는 방법"} color={"secondary"} />
        <FilterButton content={"TV에 나오는 레시피"} color={"info"} />
        <FilterButton content={"편의점 꿀 조합"} color={"success"} />
      </FilterBox>
      <div class="row row-cols-1 row-cols-sm-2 row-cols-md-4 g-4">
        {/* 반복문 고려 */}
        <CommunityCard
          category={"나만의 레시피"}
          title={"떡볶이에 쫄면을 넣어서 맛있는 쫄볶이 만드는 법"}
        />
        <CommunityCard
          category={"나만의 레시피"}
          title={"떡볶이에 쫄면을 넣어서 맛있는 쫄볶이 만드는 법"}
        />
        <CommunityCard
          category={"나만의 레시피"}
          title={"떡볶이에 쫄면을 넣어서 맛있는 쫄볶이 만드는 법"}
        />
        <CommunityCard
          category={"나만의 레시피"}
          title={"떡볶이에 쫄면을 넣어서 맛있는 쫄볶이 만드는 법"}
        />
        <CommunityCard
          category={"나만의 레시피"}
          title={"떡볶이에 쫄면을 넣어서 맛있는 쫄볶이 만드는 법"}
        />
        <CommunityCard
          category={"나만의 레시피"}
          title={"떡볶이에 쫄면을 넣어서 맛있는 쫄볶이 만드는 법"}
        />
        <CommunityCard
          category={"나만의 레시피"}
          title={"떡볶이에 쫄면을 넣어서 맛있는 쫄볶이 만드는 법"}
        />
        <CommunityCard
          category={"나만의 레시피"}
          title={"떡볶이에 쫄면을 넣어서 맛있는 쫄볶이 만드는 법"}
        />
      </div>
    </Wrapper>
  );
};

const Wrapper = styled.div`
  display: block;
  width: 100%;
  height: 200vh;
  background-color: #ececec;
  text-align: center;

  padding-top: 40px;
  padding-bottom: 40px;
  padding-left: 40px;
  padding-right: 40px;
`;

const FilterBox = styled.div`
  display: flex;
  justify-content: center;
`;

export default Community;
