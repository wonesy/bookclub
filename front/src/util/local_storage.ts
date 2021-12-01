import { TokenPair } from '../state/auth'

export const LOCAL_STORAGE_TOKEN_KEY = 'auth_tokens'

export function storeTokens(tokenPair: TokenPair | undefined) {
    window.localStorage.setItem(LOCAL_STORAGE_TOKEN_KEY, JSON.stringify(tokenPair))
}

export function loadTokens(): TokenPair | undefined {
    const item = window.localStorage.getItem(LOCAL_STORAGE_TOKEN_KEY)
    if (!item || item == 'undefined') return undefined

    try {
        const tokens: TokenPair = JSON.parse(item)
        return tokens
    } catch {
        console.error('Failure to parse token from local storage')
    }

    return undefined
}
