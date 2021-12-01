import produce from 'immer'
import create, { SetState, State, StateCreator } from 'zustand'
import { devtools } from 'zustand/middleware'
import { AuthState, TokenPair } from './auth'
import { emptyAuthState } from './auth'
import { loadTokens, storeTokens } from './local_storage'
import { emptyMemberState, Member, MemberState } from './member'

const immer =
    <T extends State, U extends State>(
        config: StateCreator<T, (fn: (draft: T) => void) => void, U>
    ): StateCreator<T, SetState<T>, U> =>
    (set, get, api) =>
        config(fn => set(produce(fn) as (state: T) => T), get, api)

export type AppState = {
    authState: AuthState
    memberState: MemberState
    // auth
    setTokenPair: (t: TokenPair | undefined) => void
    getTokenPair: () => TokenPair | undefined

    // member
    addCurrentMember: (m: Member) => void
    addMemberDetails: (m: Member | Member[]) => void
}

export const emptyAppState: {
    memberState: MemberState
    authState: AuthState
} = {
    memberState: emptyMemberState,
    authState: emptyAuthState
}

export const useStore = create<AppState>(
    devtools(
        immer((set, get) => ({
            ...emptyAppState,

            // auth
            setTokenPair: (t: TokenPair | undefined) =>
                set(state => {
                    storeTokens(t)
                    state.authState.tokens = t
                }),
            getTokenPair: () => get().authState.tokens,

            // member
            addCurrentMember: (m: Member) => set(state => (state.memberState.current = m)),
            addMemberDetails: (m: Member | Member[]) =>
                set(state => {
                    if (Array.isArray(m)) {
                        m.forEach(c => (state.memberState.members[c.username] = c))
                    } else {
                        state.memberState.members[m.username] = m
                    }
                })
        }))
    )
)
