import React from "react";

function Rating({ value, text, color }) {
  const stars = [];

  for (let i = 1; i <= 5; i++) {
    if (value >= i) {
      stars.push(<i key={i} style={{ color }} className="fas fa-star"></i>);
    } else if (value >= i - 0.5) {
      stars.push(
        <i key={i} style={{ color }} className="fas fa-star-half-alt"></i>
      );
    } else {
      stars.push(<i key={i} style={{ color }} className="far fa-star"></i>);
    }
  }

  return (
    <div>
      <span>{stars}</span>
      <span> {text && text} </span>
    </div>
  );
}

export default Rating;
