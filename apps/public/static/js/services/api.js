const API_BASE_URL = "https://web-production-b0fee.up.railway.app/API-v1"

export async function signUpUserApi(userData) {
	try{
		const response = await fetch(`${API_BASE_URL}/auth/register`, {
			method: "POST",
			headers: {
				"Content-Type": "application/json"
			},
			body: JSON.stringify(userData)
		});
		const result = await response.json();
		if (!response.ok) {
			if (response.status === 409) {
				console.error(result);
			}
			return {"success": false,"message": "Response error"};
		}

		const context = {"success": true, "message": "User sucessfully uploaded"};
		console.log(context);
		return context

	} catch (error) {
		return {"success": false,"error": error};
	}
}


export async function signInUserApi(userData) {
	try{
		const response = await fetch(`${API_BASE_URL}/auth/login`, {
			method: "POST",
			headers: {
				"Content-Type": "application/json"
			},
			body: JSON.stringify(userData)
		});
		const result = await response.json();

		if (!response.ok) {
			if (response.status === 401) {
				return {"success": false, "message": result.message};
			} else if (response.status === 409) {
				return {"success": false, "message": result.message}
			}else if (response.status === 405) {
				console.error(result.message);
			}else if (response.status === 404){
				return {"success": false, "message": result.message};
			}else if (response.status === 500) {
				console.error(result.message);
			}
		}

		const context = {"success": true, "message": "Valid credentials"};
		console.log(context);
		return context;

	} catch (error) {
		const context = {"success": false, "error": error};
		console.error(error);
		return context;
	}
}