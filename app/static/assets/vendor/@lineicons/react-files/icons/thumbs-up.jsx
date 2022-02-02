import React from 'react';

function ThumbsUp(props) {
	const title = props.title || "thumbs up";

	return (
		<svg height="64" width="64" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
	<title>{title}</title>
	<g fill="#000000">
		<path d="M61 26.6c-2.5-5.6-11.4-5.4-16.7-5.3h-.7c.5-2.8 1.9-11.9.5-14.7C43 4.5 41 3.2 38.5 3c-2.5-.2-4.7.9-6.1 3.1-5.9 9.2-11.6 15.4-13.8 17.7-.2.2-.5.2-.7.2H5.6c-2.4 0-4.4 2-4.4 4.4v23.7c0 2.4 2 4.4 4.4 4.4H15l.7.5c2.7 1.8 8.4 3.1 16.5 3.8 1.3.1 2.3.1 3.6.1 6.9 0 13.5-1.7 18.1-4.7 8.5-5.5 11-20.9 7.1-29.6zM4.8 52.1V28.4c0-.5.4-.9.9-.9h6.2V53H5.7c-.5 0-.9-.4-.9-.9zM52 53.4c-4 2.6-9.9 4.1-16.1 4.1-1.2 0-2.1 0-3.2-.1-10.4-1-13.9-2.6-14.9-3.2l-1.1-.8c-.3-.2-.7-.3-1-.3h-.3V27.5H18c1.2 0 2.3-.5 3.2-1.3 2.2-2.3 8.1-8.7 14.2-18.2.6-1.1 1.6-1.6 2.8-1.5 1.3.1 2.3.7 2.8 1.8.4.9.4 5.6-.9 12.9l-.4 1.6c-.1.5 0 1.1.3 1.5.3.4.8.7 1.4.7h2.9c4.1-.1 11.8-.3 13.4 3.2 3.3 7.1 1.1 20.7-5.7 25.2z"/>
	</g>
</svg>
	);
};

export default ThumbsUp;