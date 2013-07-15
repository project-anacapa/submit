"""Added points and points possible to Submission.

Revision ID: 49bc0cea7873
Revises: 2aa111418585
Create Date: 2013-07-14 17:25:35.263843

"""

# revision identifiers, used by Alembic.
revision = '49bc0cea7873'
down_revision = '2aa111418585'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('submission', sa.Column('points_possible', sa.Integer(), server_default=u'0', nullable=False))
    op.add_column('submission', sa.Column('points', sa.Integer(), server_default=u'0', nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('submission', 'points')
    op.drop_column('submission', 'points_possible')
    ### end Alembic commands ###
