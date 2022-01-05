import * as React from 'react'
import { apiRequest } from '../api/api_request'
import * as auth from '../auth-provider'
import { useAsync } from '../util/hooks/use_async'

type AuthContextProps = {
    user?: { accessToken: string; refreshToken?: string; username: string }
    isLoading?: boolean
    status?: string
    login?: (creds: { username: string; password: string }) => void
    logout?: () => void
    error?: any
    children?: React.ReactNode
}

const AuthContext = React.createContext<AuthContextProps | undefined>(undefined)

function AuthProvider(props: AuthContextProps) {
    const {
        data: user,
        status,
        run,
        error,
        setData,
        setError,
        isSuccess,
        isError,
        isIdle,
        isLoading
    } = useAsync()

    React.useEffect(() => {
        // get user from token in local storage, if present
        // do once per mount
        // setData(auth.checkLoggedIn())
        run(auth.checkLoggedIn())
    }, [])

    const login = React.useCallback(
        (creds: { username: string; password: string }) => {
            auth.login(creds)
                .then(user => {
                    setData(user)
                    setError(null)
                })
                .catch(setError)
        },
        [setData]
    )

    const logout = React.useCallback(() => {
        auth.logout().finally(() => {
            setData(null)
            setError(null)
        })
    }, [setData, setError])

    const value = React.useMemo(
        () => ({ user, login, logout, error, status }),
        [login, logout, user, error, isLoading, status]
    )

    if (isLoading || isIdle) {
        return null
    }

    // if success...
    return <AuthContext.Provider value={value}>{props.children}</AuthContext.Provider>
}

function useAuth() {
    const context = React.useContext(AuthContext)
    if (context === undefined) {
        throw new Error(`useAuth must be used within a AuthProvider`)
    }
    return context
}

function useAuthClient() {
    const { user } = useAuth()
    const token = user?.accessToken
    return React.useCallback((endpoint, data) => apiRequest(endpoint, data, token), [token])
}

export { AuthProvider, useAuth, useAuthClient }
