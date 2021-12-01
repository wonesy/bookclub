import produce from 'immer'
import create, { SetState, State, StateCreator } from 'zustand'
import { emptyMemberState, Member, MemberState } from './member'

const immer =
    <T extends State, U extends State>(
        config: StateCreator<T, (fn: (draft: T) => void) => void, U>
    ): StateCreator<T, SetState<T>, U> =>
    (set, get, api) =>
        config(fn => set(produce(fn) as (state: T) => T), get, api)

export type AppState = {
    memberState: MemberState
    addCurrentMember: (m: Member) => void
}

export const emptyAppState: Pick<AppState, 'memberState'> = {
    memberState: emptyMemberState
}

export const useStore = create<AppState>(
    immer((set, get) => ({
        ...emptyAppState,

        addCurrentMember: (m: Member) => set(state => (state.memberState.current = m))
    }))
)
