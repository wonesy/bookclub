import axios, { AxiosPromise, AxiosRequestConfig, AxiosResponse } from 'axios'
import * as auth from '../auth-provider'

const apiURL = 'http://localhost:8000'

async function apiRequest(
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

    return await axios.request(config)
}

export { apiRequest }
