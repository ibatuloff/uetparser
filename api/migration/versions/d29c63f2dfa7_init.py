"""init

Revision ID: d29c63f2dfa7
Revises: 
Create Date: 2025-07-09 10:54:42.557420

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd29c63f2dfa7'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jobs',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('data', sa.String(), nullable=False),
    sa.Column('status', sa.Enum('ISSUED', 'FINISHED', name='jobstatus'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('jobsdata',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('itemcode', sa.String(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('data', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'itemcode', 'url')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('jobsdata')
    op.drop_table('jobs')
    # ### end Alembic commands ###
