import styled from "styled-components";

const Title = ({ content }) => {
  return <Component>{content}</Component>;
};

const Component = styled.div`
  font-weight: bold;
  font-size: 28px;
`;

export default Title;
