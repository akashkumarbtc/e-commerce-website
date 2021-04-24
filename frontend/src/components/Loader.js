import React from "react";
import { Spinner } from "react-bootstrap";

const Loader = () => {
  return (
    <Spinner
      animatation="border"
      role="status"
      style={{
        height: "100px",
        width: "100px",
        margin: "auto",
        display: "block",
        color: "white",
      }}
    >
      <span className="sr-only">Loading ... </span>
    </Spinner>
  );
};

export default Loader;
