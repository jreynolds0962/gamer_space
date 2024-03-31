"""make developer column fk

Revision ID: 4167ba04cfaa
Revises: 799e38feaba7
Create Date: 2024-03-31 20:19:05.414259

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '4167ba04cfaa'
down_revision: Union[str, None] = '799e38feaba7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('games', 'developer',
               existing_type=mysql.VARCHAR(length=255),
               type_=sa.Integer(),
               existing_nullable=True)
    op.create_foreign_key(None, 'games', 'developers', ['developer'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'games', type_='foreignkey')
    op.alter_column('games', 'developer',
               existing_type=sa.Integer(),
               type_=mysql.VARCHAR(length=255),
               existing_nullable=True)
    # ### end Alembic commands ###