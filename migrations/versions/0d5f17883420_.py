"""empty message

Revision ID: 0d5f17883420
Revises: ae8ca5bc4af8
Create Date: 2024-12-11 20:32:46.057260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d5f17883420'
down_revision = 'ae8ca5bc4af8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=80), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('people', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###
