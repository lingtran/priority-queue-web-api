"""empty message

Revision ID: 02_add_created_at_to_jobs
Revises: 01_initial
Create Date: 2021-07-08 03:27:04.043877

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '02_add_created_at_to_jobs'
down_revision = '01_initial'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column(
        'jobs',
        sa.Column('created_at', sa.DateTime(), nullable=False),
    )

def downgrade():
    op.drop_column('jobs', 'created_at')
