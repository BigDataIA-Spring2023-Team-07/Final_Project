from pydantic import BaseModel
from typing import Union
from typing import List

class top_attractions(BaseModel):
    city: str
    types: str

class optimal_pairs(BaseModel):
    locations: list

class final_cost(BaseModel):
    start_date_val: str
    end_date_val: str
    num_days_val: int
    adults_number_val: int
    num_rooms_val: str
    des_id: str
    type_des: str
    type_val: str
    origin_val: str
    destination_val: str
    budget_val: int

class TokenClass(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None

class UserData(BaseModel):
    Username: str
    Password: str
    Name: str
    Plan: str
    AOI: List[str]

class ForgotPassword(BaseModel):
    Username: str
    Password: str
    
class top_attractions(BaseModel):
    city: str
    types: str

class optimal_pairs(BaseModel):
    locations: list

class final_cost(BaseModel):
    start_date_val: str
    end_date_val: str
    num_days_val: int
    adults_number_val: int
    num_rooms_val: str
    des_id: str
    type_des: str
    type_val: str
    origin_val: str
    destination_val: str
    budget_val: int

class TokenClass(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None