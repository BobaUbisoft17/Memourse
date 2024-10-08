"""empty message

Revision ID: a532f0b44c60
Revises: cba935ef0a83
Create Date: 2024-08-31 12:48:26.897241

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a532f0b44c60'
down_revision: Union[str, None] = 'cba935ef0a83'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('course', schema=None) as batch_op:
        batch_op.add_column(sa.Column('chapters_sequense', sa.JSON(), server_default='[]', nullable=False))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('course', schema=None) as batch_op:
        batch_op.drop_column('chapters_sequense')

    # ### end Alembic commands ###
