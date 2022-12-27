import styled from "styled-components";

// 클릭되어 있을 시와 아닐 시로 구분

const FilterButton = ({ content, color }) => {
  return (
    <Component type="button" className={`btn btn-outline-${color}`}>
      {content}
    </Component>
  );
};

const Component = styled.button`
  cursor: pointer;

  margin-top: 10px;
  margin-bottom: 25px;
  margin-left: 10px;
  margin-right: 10px;
`;

export default FilterButton;
