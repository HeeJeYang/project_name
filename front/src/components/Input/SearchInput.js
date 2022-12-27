import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import styled from "styled-components";

const SearchInput = () => {
  return (
    <Component className="input-group mb-3">
      <input
        type="text"
        class="form-control"
        placeholder="레시피 검색"
        aria-label="Recipient's username"
        aria-describedby="button-addon2"
      />
      <button
        class="btn btn-outline-secondary"
        type="button"
        id="button-addon2"
      >
        <FontAwesomeIcon icon="fa-solid fa-magnifying-glass" />
      </button>
    </Component>
  );
};

const Component = styled.div`
  margin: 0 auto;
  margin-top: 20px;
  margin-bottom: 20px;
  width: 400px;
`;

export default SearchInput;
