import {signInUserApi} from "./services/api.js";

const API_BASE_URL = "http://127.0.0.1:8000";

async function signIn(data){
	const validation = await signInUserApi(data);
	if(validation.success === true){
		console.log("Redirigiendo al dashboard");
		setTimeout(() => {
			window.location.href = `${API_BASE_URL}/dashboard`;
		}, 3000);
	} else {
		alert(validation.message || validation.error);
	}
}

document.addEventListener("DOMContentLoaded", () => {
	const signInBtn = document.getElementById("sign-in-btn");
	signInBtn.addEventListener("click", () => {
		const username = document.getElementById("login__username").value;
		const pass = document.getElementById("login__password").value;
		const data = {
			"username": username,
			"pass": pass
		};

		signIn(data);
	});
});