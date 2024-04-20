"""db init

Revision ID: c9fe0a2fe975
Revises: 
Create Date: 2024-04-20 11:03:04.763665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9fe0a2fe975'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('locations',
    sa.Column('location_id', sa.String(length=200), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('location_id')
    )
    op.create_table('products',
    sa.Column('product_id', sa.String(length=200), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('product_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('productmovements',
    sa.Column('movement_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('qty', sa.Integer(), nullable=True),
    sa.Column('from_location', sa.Integer(), nullable=True),
    sa.Column('to_location', sa.Integer(), nullable=True),
    sa.Column('movement_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['from_location'], ['locations.location_id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.product_id'], ),
    sa.ForeignKeyConstraint(['to_location'], ['locations.location_id'], ),
    sa.PrimaryKeyConstraint('movement_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('productmovements')
    op.drop_table('user')
    op.drop_table('products')
    op.drop_table('locations')
    # ### end Alembic commands ###
