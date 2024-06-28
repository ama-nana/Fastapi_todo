"""initial

Revision ID: eeeda5e9819f
Revises: 
Create Date: 2024-06-27 11:16:45.236992

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eeeda5e9819f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('is_completed', sa.Boolean(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('views', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_todos_created_at'), 'todos', ['created_at'], unique=False)
    op.create_index(op.f('ix_todos_id'), 'todos', ['id'], unique=False)
    op.create_index(op.f('ix_todos_title'), 'todos', ['title'], unique=False)
    op.create_index(op.f('ix_todos_updated_at'), 'todos', ['updated_at'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_todos_updated_at'), table_name='todos')
    op.drop_index(op.f('ix_todos_title'), table_name='todos')
    op.drop_index(op.f('ix_todos_id'), table_name='todos')
    op.drop_index(op.f('ix_todos_created_at'), table_name='todos')
    op.drop_table('todos')
    # ### end Alembic commands ###
