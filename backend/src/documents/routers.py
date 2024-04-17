from fastapi import APIRouter
from fastapi import Depends, Path
from fastapi import UploadFile
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse, Response

from sqlalchemy.orm import Session

from main.databse import get_connect

from documents.crud import document_crud
from documents.depends import check_document_exists
from documents.filters import Filter


router = APIRouter()


@router.post('/upload')
def upload_document(
    file: UploadFile,
    db: Session = Depends(get_connect)
) -> JSONResponse:
    
    if file.content_type != 'text/plain':
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Allowed only `text/plain` files!'
        )

    res = document_crud.create(db, file)
    return JSONResponse(content=res, status_code=status.HTTP_201_CREATED)


@router.get(
    '/document/{id}',
    dependencies=[Depends(check_document_exists)]
)
def retrieve_document(
    id: str = Path(regex='[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'),
    db: Session = Depends(get_connect)
) -> JSONResponse:

    res = document_crud.retrieve(db, id)
    return JSONResponse(content=res, status_code=status.HTTP_200_OK)


@router.get('/documents')
def list_documents(
    filter: Filter = Depends(),
    db: Session = Depends(get_connect)
) -> JSONResponse:

    res = document_crud.list(db, filter)
    return JSONResponse(content=res, status_code=status.HTTP_200_OK)


@router.delete(
    '/document/remove/{id}',
    dependencies=[Depends(check_document_exists)]
)
def remove_document(
    id: str = Path(regex='[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'),
    db: Session = Depends(get_connect)
) -> Response:
    
    res = document_crud.delete(db, id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get(
    '/words/{id}',
    dependencies=[Depends(check_document_exists)]
)
def list_words_of_document(
    id: str = Path(regex='[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'),
    filter: Filter = Depends(),
    db: Session = Depends(get_connect)
) -> JSONResponse:

    res = document_crud.list_words_of_document(db, id, filter)
    return JSONResponse(content=res, status_code=status.HTTP_200_OK)

