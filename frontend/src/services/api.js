import axios from 'axios'


const BASE_URL = process.env.REACT_APP_API_URL


async function getApi(route, auth='') {
    let response_status = 400
    return fetch(
        BASE_URL + route,
        {
            headers: new Headers({
                Authorization: auth,
            })
        }
    )
    .then(response => {
        response_status = response.status
        return response.json()
    })
    .then(data => {
        return {data, response_status}
    })
}


async function deleteApi(route, formData, token='') {
    let response_status = 400
    return fetch(
        BASE_URL + route,
        {
            credentials: 'same-origin',
            method: 'DELETE',
            body: JSON.stringify(formData),
            headers: new Headers({
                'Authorization': token,
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            })
        }
    )
    .then(response => {
        response_status = response.status
        return response.json()
    })
    .then(data => {
        return {data, response_status}
    })
}


async function postApi(route, formData, token='') {
    let response_status = 400
    return fetch(
        BASE_URL + route,
        {
            credentials: 'same-origin',
            method: 'POST',
            body: JSON.stringify(formData),
            headers: new Headers({
                'Authorization': token,
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            })
        }
    )
    .then(response => {
        response_status = response.status
        return response.json()
    })
    .then(data => {
        return {data, response_status}
    })
}


async function postFormDataApi(route, formData, auth='') {
    let response_status = 400
    return fetch(
        BASE_URL + route,
        {
            credentials: 'same-origin',
            method: 'POST',
            body: formData,
            headers: new Headers({
                'Authorization': auth,
            })
        }
    )
    .then(response => {
        response_status = response.status
        return response.json()
    })
    .then(data => {
        return {data, response_status}
    })
}


async function googleLogin(accesstoken) {
    const { data } = await postApi(
        'rest-auth/google/',
        { access_token: accesstoken }
    )
    return data
}

const axiosRequest = axios.create({
	baseURL: BASE_URL,
})



export {
    getApi,
    deleteApi,
    postApi,
    postFormDataApi,
    googleLogin,
    axiosRequest
}