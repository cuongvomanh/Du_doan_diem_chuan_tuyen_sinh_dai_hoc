const express = require('express');
const app = express();
const multer  = require('multer');
const upload = multer({ dest: 'upload/' });
const PythonShell = require('python-shell');

const processUpload = upload.fields([{
	name: 'f1',
	maxCount: 1
}, {
	name: 'f2',
	maxCount: 1
}, {
	name: 'f3',
	maxCount: 1
}]);

app.post('/process', processUpload, (req, res) => {
	const { f1, f2, f3 } = req.files;
	const shellOption = {
		mode: 'text',
		scriptPath: __dirname,
		args: [f1[0].filename, f2[0].filename, f3[0].filename]
	}
	PythonShell.run('./service.py', shellOption, (err, result) => {
		if (err) throw err;
		res.json({
			msg: result
		});
	});
});

app.use(express.static(__dirname));

const port = 8080;
app.listen(port, () => {
	console.log("Server is listening on port " + port);
});
