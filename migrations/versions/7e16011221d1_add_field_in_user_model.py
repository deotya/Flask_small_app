"""add field in User model

Revision ID: 7e16011221d1
Revises: b2b9f0097300
Create Date: 2025-02-22 12:58:05.703533

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e16011221d1'
down_revision = 'b2b9f0097300'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('test')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('test', sa.VARCHAR(length=100), nullable=False))

    # ### end Alembic commands ###
