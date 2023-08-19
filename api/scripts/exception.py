from fastapi import APIRouter, Depends, HTTPException


def exception_404(message):
     return{
         'meta': {
             'code': 404,
             'message':message
         },
         'data':{
             'products':111
         }
     }

def exception_401():
    pass


def exception_202():
    pass