"""empty message

Revision ID: 2d9e9856397d
Revises: 0783e7c84e04
Create Date: 2022-04-11 00:42:29.640306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d9e9856397d'
down_revision = '0783e7c84e04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('itemName', sa.String(), nullable=False),
    sa.Column('itemDescription', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('condition', sa.String(), nullable=False),
    sa.Column('size', sa.String(), nullable=False),
    sa.Column('contactInfo', sa.String(), nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    # ### end Alembic commands ###
