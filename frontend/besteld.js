fetch("http://127.0.0.1:8000")
	.catch(console.error)
	.then(v => v.json())
	.then(v => {
		console.debug(v)
	});
