"""empty message

Revision ID: 6e443b9718f8
Revises: 76372e8c5e8e
Create Date: 2023-11-15 12:41:25.411366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e443b9718f8'
down_revision = '76372e8c5e8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('portfolios', schema=None) as batch_op:
        batch_op.drop_column('current_value')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('expense_budget', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('expense_budget')

    with op.batch_alter_table('portfolios', schema=None) as batch_op:
        batch_op.add_column(sa.Column('current_value', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###
