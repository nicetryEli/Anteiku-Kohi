from datetime import datetime


class StaffEntity:
    id: int
    full_name: str
    phone_number: str
    email: str
    address: str
    updated_at: datetime
    joined_at: datetime
    is_active: bool
    hashed_password: str
    refresh_token: str | None

    def __init__(self, id: int, full_name: str, phone_number: str, email: str, address: str, updated_at: datetime, joined_at: datetime, is_active: bool, hashed_password: str, refresh_token: str | None):
        self.id = id
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.updated_at = updated_at
        self.joined_at = joined_at
        self.is_active = is_active
        self.hashed_password = hashed_password
        self.refresh_token = refresh_token
