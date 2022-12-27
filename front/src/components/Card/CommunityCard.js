import styled from "styled-components";
import CardText from "../Text/CardText";

const CommunityCard = ({ category, title }) => {
  return (
    <div class="col">
      <div class="card">
        <CardImg
          src={`${process.env.PUBLIC_URL}/assets/ssafy_logo.png`}
          class="card-img-top"
          alt="ssafy_logo"
        />
        <div class="card-body">
          <Category>[{category}]</Category>
          <CardText class="card-title" content={title} />
        </div>
      </div>
    </div>
  );
};

const CardDiv = styled.div`
  text-align: center;
`;

const Category = styled.div`
  color: grey;
  font-size: 8px;
  text-align: start;

  margin-bottom: 10px;
`;

const CardImg = styled.img`
  width: 80%;
  height: 80%;
  display: block;
  margin: 0 auto;
`;

export default CommunityCard;
