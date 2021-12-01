export type Member = {
    username: string
    firstName?: string
    lastName?: string
}

export type MemberState = {
    current?: Member
    members: Record<string, Member>
}

export const emptyMemberState: MemberState = {
    members: {}
}
