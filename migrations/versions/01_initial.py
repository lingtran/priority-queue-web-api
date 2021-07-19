"""empty message

Revision ID: 01_initial
Revises: None
Create Date: 2021-07-07 03:27:04.043877

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql as psql


# revision identifiers, used by Alembic.
revision = '01_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('jobs',
        sa.Column('id', psql.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('priority', sa.Integer(), nullable=False),
        sa.Column('submitterId', sa.Integer(), nullable=False)
    )


def downgrade():
    op.drop_table('jobs')
