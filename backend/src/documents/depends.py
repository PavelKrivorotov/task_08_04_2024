from fastapi import HTTPException, status
from fastapi import Depends, Path

from sqlalchemy.orm import Session

from main.databse import get_connect
from documents.models import Document


def check_document_exists(
    id: str = Path(regex='[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'),
    db: Session = Depends(get_connect)
):
    
    document = db.get(Document, id)
    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Document {0} not found'.format(id)
        )

