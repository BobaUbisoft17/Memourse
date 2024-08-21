"""empty message

Revision ID: bec61a4d8d4b
Revises: 31b14561e851
Create Date: 2024-08-21 18:58:55.954286

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bec61a4d8d4b'
down_revision: Union[str, None] = '31b14561e851'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chapter', schema=None) as batch_op:
        batch_op.alter_column('avatar',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chapter', schema=None) as batch_op:
        batch_op.alter_column('avatar',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###
