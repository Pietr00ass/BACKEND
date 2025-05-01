from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas import CryptoRequest
from ..services.crypto import encrypt_file, decrypt_file
from ..dependencies import get_db

router = APIRouter()

@router.post('/encrypt')
def api_encrypt(req: CryptoRequest, db: Session = Depends(get_db)):
    try:
        path = encrypt_file(req.filepath, req.remove_original)
        return { 'path': path }
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post('/decrypt')
def api_decrypt(req: CryptoRequest, db: Session = Depends(get_db)):
    try:
        path = decrypt_file(req.filepath, req.remove_original)
        return { 'path': path }
    except Exception as e:
        raise HTTPException(400, str(e))
