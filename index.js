function getEl(id) {
	return document.getElementById(id);
}

getEl('form').onsubmit = e => {
	e.preventDefault();
	const f1 = getEl('nganh-khoi').files[0];
	const f2 = getEl('nganh-chi-chuan').files[0];
	const f3 = getEl('khoi-diem-sl').files[0];
	const form = new FormData();
	form.append('f1', f1);
	form.append('f2', f2);
	form.append('f3', f3);
	fetch('/process', {
		method: 'POST',
		credentials: 'same-origin',
		body: form
	})
	.then(response => response.json())
	.then(response => {
		renderData(response);
	})
	.catch(err => {
		console.error(err);
	})
}

function renderData(data) {
	console.log(data);
	// Process data here
	
}
