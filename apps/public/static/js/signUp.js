import {signUpUserApi} from "./services/api.js";

const APP_BASE_URL = "http://127.0.0.1:8000"

async function signUpUser(userData){
	const user = await signUpUserApi(userData);
	if (user.success === true) {
		window.location.href = `${APP_BASE_URL}/dashboard/`;
	} else if (user.success === false) {
		alert(user.message || user.error)
	}
}

document.addEventListener("DOMContentLoaded", () => {
	const submitBtn = document.getElementById("submit__btn");
	submitBtn.addEventListener("click", () => {
		const username = document.getElementById("login__username").value;
		const name = document.getElementById("login__name").value;
		const lastName = document.getElementById("login__lastname").value;
		const email = document.getElementById("login__email").value;
		const pass = document.getElementById("login__password").value;
		const position = document.getElementById("login__position").value;

		const data = {
			"username": username,
			"name": name,
			"last_name": lastName,
			"email": email,
			"pass": pass,
			"position": position
		};

		signUpUser(data);

	})
})