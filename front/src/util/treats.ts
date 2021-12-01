import { Member } from '../state/member'

export function toMember(data: any): Member | undefined {
    if (!data) return undefined
    return {
        username: data['username'],
        firstName: data['first_name'],
        lastName: data['last_name']
    } as Member
}
