import { atom } from 'jotai'
import { Member } from './member'

// Contains all information about the logged in user aka 'me'
export const meAtom = atom<Member | null>(null)
