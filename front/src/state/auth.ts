export type TokenPair = {
    accessToken: string
    refreshToken: string
}

export type AuthState = {
    tokens: TokenPair | undefined
}

export const emptyAuthState: AuthState = {
    tokens: undefined
}
