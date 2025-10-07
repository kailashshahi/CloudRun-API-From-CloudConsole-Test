from fastapi import FastAPI
from pydantic import BaseModel
from typing import Type
import json
import os
from fastapi.middleware.cors import CORSMiddleware


class Student(BaseModel):
    id:str
    name:str
    address:str
    email:str
    


app=FastAPI()
# if your frontend domain is known, replace "*" with the actual origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



data=[{
        "id":"101",
        "name":"kailash singh",
        "address":"gurgoan",
        "email":"kailash.singh@indixpert.com"
        
    },
     {
        "id":"102",
        "name":"Indixpert",
        "address":"gurgoan",
        "email":"Indixpert@gmail.com"
        
    }
]

@app.get("/")
def CheckServerStatus():
    return {"message":"Indixpert - API- Server is working and active........","statuscode":200}

@app.get("/test")
def GetStudentRegistration(studentid:str,email:str):
    try:
        if not studentid.isdigit():
            return {"error":"student id is not integer"}
          
        output={"message":"success","statuscode":200,"id":studentid,"email":email} 
        return output
    except Exception as e:
        return {"ERROR":e}

