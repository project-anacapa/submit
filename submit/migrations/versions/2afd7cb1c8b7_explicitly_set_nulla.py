"""Explicitly set nullable attribute on all foreign keys

Revision ID: 2afd7cb1c8b7
Revises: 520ecfd63df2
Create Date: 2013-01-28 13:59:38.462407

"""

# revision identifiers, used by Alembic.
revision = '2afd7cb1c8b7'
down_revision = '520ecfd63df2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('buildfile', u'project_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('buildfile', u'file_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('executionfile', u'project_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('executionfile', u'file_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column(u'submissiontofile', u'file_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(u'submissiontofile', u'file_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('executionfile', u'file_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('executionfile', u'project_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('buildfile', u'file_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('buildfile', u'project_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    ### end Alembic commands ###
