const express = require("express");
const path = require("path");

const app = express();

app.get("/model", (req, res) => {
	console.log("Model Server: Model requested by ML Server")

	res.sendFile(path.join(__dirname, "mobilenet.pth"));
});

app.listen(8000, () => {
	console.log("Model Server is running on port 8000");
});
