"""Create tables words, documents, word_documents

Revision ID: e9def34a0c6b
Revises: 
Create Date: 2024-04-09 13:07:00.297512

"""
import uuid
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e9def34a0c6b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ###
    op.create_table(
        'words',
        sa.Column(
            'id',
            sa.Uuid(),
            primary_key=True,
            default=uuid.uuid4
        ),
        sa.Column(
            'word',
            sa.String(255),
            unique=True,
            index=True,
            nullable=False
        ), 
        sa.Column(
            'count_in_all_documents',
            sa.Integer(),
            default=1,
            nullable=False
        )
    )

    op.create_table(
        'documents',
        sa.Column(
            'id',
            sa.Uuid(),
            primary_key=True,
            default=uuid.uuid4
        ),
        sa.Column(
            'title',
            sa.String(255),
            nullable=False
        ),
        sa.Column(
            'count_words',
            sa.Integer(),
            nullable=False
        ),
        sa.Column(
            'published',
            sa.DateTime(),
            server_default=sa.func.now(),
            nullable=False
        )
    )

    op.create_table(
        'word_document',
        sa.Column(
            'id',
            sa.Uuid(),
            primary_key=True,
            default=uuid.uuid4
        ),
        sa.Column(
            'document_id',
            sa.Uuid(),
            sa.ForeignKey('documents.id', ondelete='CASCADE'),
            index=True,
            nullable=False
        ),
        sa.Column(
            'word_id',
            sa.Uuid(),
            sa.ForeignKey('words.id', ondelete='CASCADE'),
            index=True,
            nullable=False
        ),
        sa.Column(
            'count_in_document',
            sa.Integer,
            nullable=False
        )
    )
    # ###


def downgrade() -> None:
    # ###
    op.drop_table('word_document')
    op.drop_table('documents')
    op.drop_table('words')
    # ###
