from pydantic import BaseModel

class Invitation(BaseModel):
    club: int


class InvitationResponse(BaseModel):
    club: int
    token: str
