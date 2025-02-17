"""empty message

Revision ID: 0ab118eefccd
Revises: 64e5bb84839a
Create Date: 2023-11-03 13:36:30.100209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ab118eefccd'
down_revision = '64e5bb84839a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('stock_budget', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('stock_budget')

    # ### end Alembic commands ###
