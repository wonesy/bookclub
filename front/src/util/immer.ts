import produce from "immer"
import { State, StateCreator, SetState } from "zustand"

const immerState =
    <T extends State, U extends State>(
        config: StateCreator<T, (fn: (draft: T) => void) => void, U>
    ): StateCreator<T, SetState<T>, U> =>
    (set, get, api) =>
        config(fn => set(produce(fn) as (state: T) => T), get, api)

export default immerState