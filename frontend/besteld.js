fetch("https://chirper.pockethost.io/api/health")
	.catch(console.error)
	.then(v => v.json())
	.then(v => {
		console.debug(v)
	});
