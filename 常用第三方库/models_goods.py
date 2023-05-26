# coding: utf-8
from sqlalchemy import Column, DateTime, Float, ForeignKey, Index, Integer, JSON
from sqlalchemy.dialects.mysql import DATETIME, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata


class Banner(Base):
    __tablename__ = 'banner'
    id = Column(Integer, primary_key=True)
    add_time = Column(DateTime, nullable=False)
    is_deleted = Column(TINYINT(1), nullable=False)
    update_time = Column(DateTime, nullable=False)
    image = Column(VARCHAR(200), nullable=False)
    url = Column(VARCHAR(200), nullable=False)
    index = Column(Integer, nullable=False)


class Brand(Base):
    __tablename__ = 'brands'

    id = Column(Integer, primary_key=True)
    add_time = Column(DateTime, nullable=False)
    is_deleted = Column(TINYINT(1), nullable=False)
    update_time = Column(DateTime, nullable=False)
    name = Column(VARCHAR(50), nullable=False, unique=True)
    logo = Column(VARCHAR(200))


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    add_time = Column(DateTime, nullable=False)
    is_deleted = Column(TINYINT(1), nullable=False)
    update_time = Column(DateTime, nullable=False)
    name = Column(VARCHAR(20), nullable=False)
    parent_category_id = Column(ForeignKey('category.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    level = Column(Integer, nullable=False)
    is_tab = Column(TINYINT(1), nullable=False)

    parent_category = relationship('Category', remote_side=[id])


class Inventory(Base):
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True)
    add_time = Column(DATETIME(fsp=3))
    update_time = Column(DATETIME(fsp=3))
    deleted_at = Column(DATETIME(fsp=3))
    is_deleted = Column(TINYINT(1))
    goods = Column(Integer, index=True)
    stocks = Column(Integer)
    version = Column(Integer)


class Good(Base):
    __tablename__ = 'goods'

    id = Column(Integer, primary_key=True)
    add_time = Column(DateTime, nullable=False)
    is_deleted = Column(TINYINT(1), nullable=False)
    update_time = Column(DateTime, nullable=False)
    category_id = Column(ForeignKey('category.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    brand_id = Column(ForeignKey('brands.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    on_sale = Column(TINYINT(1), nullable=False)
    goods_sn = Column(VARCHAR(50), nullable=False)
    name = Column(VARCHAR(100), nullable=False)
    click_num = Column(Integer, nullable=False)
    sold_num = Column(Integer, nullable=False)
    fav_num = Column(Integer, nullable=False)
    market_price = Column(Float, nullable=False)
    shop_price = Column(Float, nullable=False)
    goods_brief = Column(VARCHAR(200), nullable=False)
    ship_free = Column(TINYINT(1), nullable=False)
    images = Column(JSON, nullable=False)
    desc_images = Column(JSON, nullable=False)
    goods_front_image = Column(VARCHAR(200), nullable=False)
    is_new = Column(TINYINT(1), nullable=False)
    is_hot = Column(TINYINT(1), nullable=False)

    brand = relationship('Brand')
    category = relationship('Category')


class Goodscategorybrand(Base):
    __tablename__ = 'goodscategorybrand'
    __table_args__ = (
        Index('goodscategorybrand_category_id_brand_id', 'category_id', 'brand_id', unique=True),
    )

    id = Column(Integer, primary_key=True)
    add_time = Column(DateTime, nullable=False)
    is_deleted = Column(TINYINT(1), nullable=False)
    update_time = Column(DateTime, nullable=False)
    category_id = Column(ForeignKey('category.id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False,
                         index=True)
    brand_id = Column(ForeignKey('brands.id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)

    brand = relationship('Brand')
    category = relationship('Category')
