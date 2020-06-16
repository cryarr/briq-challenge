import React from "react";

//this function should return a form input, but i dont know where this is being passed through to
function input(props) {
	return (
		<div classname="starinput">
			<form>
				<LargeInput label="Enter star rating"
							type="star"
							value={props.rating}
							onChange={e => props.updateRating(e.target.value)}
				/>
			</form>
		</div>
	
	);
}
