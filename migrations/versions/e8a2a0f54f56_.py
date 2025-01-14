"""empty message

Revision ID: e8a2a0f54f56
Revises: 7c45790a3ef1
Create Date: 2024-12-11 20:05:04.711971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8a2a0f54f56'
down_revision = '7c45790a3ef1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('peoble')
    op.drop_table('planets')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='planets_pkey')
    )
    op.create_table('peoble',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='peoble_pkey')
    )
    # ### end Alembic commands ###
