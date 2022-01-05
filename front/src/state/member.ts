import { Club } from './clubs'

export type Member = {
    username: string
    firstName?: string
    lastName?: string
    email?: string
    clubs: Club[]
}

export type MemberState = {
    current?: Member
    members: Record<string, Member>
}

export const emptyMemberState: MemberState = {
    members: {}
}
