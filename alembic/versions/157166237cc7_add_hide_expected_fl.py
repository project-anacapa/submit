"""Add hide_expected flag to TestCase.

Revision ID: 157166237cc7
Revises: 29c521f4449c
Create Date: 2013-04-09 12:21:20.069723

"""

# revision identifiers, used by Alembic.
revision = '157166237cc7'
down_revision = '29c521f4449c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('testcase', sa.Column('hide_expected', sa.Boolean(), server_default=u'0', nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('testcase', 'hide_expected')
    ### end Alembic commands ###
