import { TokenPair } from '../auth'
import { loadTokens, storeTokens } from '../local_storage'
import { useStore } from '../store'

export function useTokens() {
    const store = useStore()

    const setTokens = (tp: TokenPair | undefined) => {
        store.setTokenPair(tp)
        storeTokens(tp)
    }

    const getTokens = (): TokenPair | undefined => {
        const tokens = store.getTokenPair()
        if (tokens !== undefined) return tokens

        const loadedTokens = loadTokens()
        if (loadedTokens === undefined) return loadedTokens

        store.setTokenPair(loadedTokens)
        return loadedTokens
    }

    const tokens = getTokens()

    return { tokens, setTokens }
}
