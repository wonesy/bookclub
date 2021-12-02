// pretend this is firebase, netlify, or auth0's code.
// you shouldn't have to implement something like this in your own app

import jwt_decode from 'jwt-decode'

const localStorageKey = '__auth_provider_token__'

type Credentials = {
    username: string
    password: string
}

type LoginResponse = {
    access_token: string
    refresh_token: string
    token_type: string
}

type DecodedToken = {
    sub: string
    exp: string
}

async function getToken() {
    // if we were a real auth provider, this is where we would make a request
    // to retrieve the user's token. (It's a bit more complicated than that...
    // but you're probably not an auth provider so you don't need to worry about it).
    return window.localStorage.getItem(localStorageKey)
}

function checkLoggedIn() {
    const token = window.localStorage.getItem(localStorageKey)
    if (token) {
        const decoded: DecodedToken = jwt_decode(token)
        return decoded.sub
    }
    return null
}

async function handleUserResponse(resp: LoginResponse) {
    window.localStorage.setItem(localStorageKey, resp.access_token)
    const decoded: DecodedToken = jwt_decode(resp.access_token)
    return decoded.sub
}

function login({ username, password }: Credentials) {
    return client('login', { username, password }).then(handleUserResponse)
}

function register({ username, password }: Credentials) {
    return client('register', { username, password }).then(handleUserResponse)
}

async function logout() {
    window.localStorage.removeItem(localStorageKey)
}

// an auth provider wouldn't use your client, they'd have their own
// so that's why we're not just re-using the client
const authURL = 'http://localhost:8000/auth'

async function client(endpoint: string, data: any) {
    const config = {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'Content-Type': 'application/json' }
    }

    return window.fetch(`${authURL}/${endpoint}`, config).then(async response => {
        const data = await response.json()
        if (response.ok) {
            return data
        } else {
            return Promise.reject(data)
        }
    })
}

export { client, getToken, login, register, logout, checkLoggedIn, localStorageKey }
