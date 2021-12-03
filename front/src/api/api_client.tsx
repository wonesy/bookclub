import axios, { AxiosPromise, AxiosRequestConfig, AxiosResponse } from 'axios'
import * as auth from '../auth-provider'

const apiURL = 'http://localhost:8000'

async function apiClient(
    endpoint: string,
    data?: Record<string, any>,
    token?: string,
    customHeaders?: Record<string, string>
): Promise<AxiosResponse<any, any>> {
    const config: AxiosRequestConfig = {
        url: `${apiURL}/${endpoint}`,
        data: data,
        method: data ? 'POST' : 'GET',
        headers: {
            Authorization: token ? `Bearer ${token}` : '',
            'Content-Type': 'application/json',
            ...customHeaders
        }
    }

    return axios
        .request(config)
        .then(async response => {
            return response.data
        })
        .catch(async error => {
            console.log(error.response)
            if (error.response.status === 401) {
                await auth.logout()
                // refresh page
                window.location.assign(window.location.toString())
                return Promise.reject({ message: 'Please re-authenticate' })
            }
        })
}

export { apiClient }
