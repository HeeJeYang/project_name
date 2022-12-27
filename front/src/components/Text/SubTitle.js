// 나중에 title과 subtitle 합쳐보기

import styled from "styled-components";

const SubTitle = ({ content }) => {
  return <Component>{content}</Component>;
};

const Component = styled.div`
  margin: 15px;
  font-size: 14px;

  // font-weight: bold;
`;

export default SubTitle;
