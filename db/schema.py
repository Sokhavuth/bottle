import sqlalchemy as db
from .connection import engine

metadata_obj = db.MetaData()

User = db.Table(
    'User',                                        
    metadata_obj,  
    db.Column('id', db.String, primary_key=True),  
    db.Column('name', db.String, nullable=False),                                
    db.Column('email', db.String, unique=True, nullable=False), 
    db.Column('password', db.String, nullable=False),  
    db.Column('role', db.String, nullable=False), 
    db.Column('thumb', db.String),    
    db.Column('content', db.String),
    db.Column('date', db.String, nullable=False),                              
)

Post = db.Table(
    'Post',                                        
    metadata_obj,  
    db.Column('id', db.String, primary_key=True),  
    db.Column('title', db.String, nullable=False),                                
    db.Column('content', db.String), 
    db.Column('categories', db.String, nullable=False),  
    db.Column('thumb', db.String), 
    db.Column('date', db.String, nullable=False),    
    db.Column('videos', db.String),
    db.Column('author', db.String, nullable=False), 
    db.Column('expiration', db.DateTime),                              
)

Category = db.Table(
    'Category',                                        
    metadata_obj,  
    db.Column('id', db.String, primary_key=True),  
    db.Column('title', db.String, nullable=False),                                
    db.Column('thumb', db.String, nullable=False), 
    db.Column('date', db.String, nullable=False),                         
)

Page = db.Table(
    'Page',                                        
    metadata_obj,  
    db.Column('id', db.String, primary_key=True),  
    db.Column('title', db.String, nullable=False),  
    db.Column('content', db.String, nullable=False),                              
    db.Column('thumb', db.String), 
    db.Column('date', db.String, nullable=False),                         
)

Setting = db.Table(
    'Setting',                                        
    metadata_obj,  
    db.Column('id', db.String, primary_key=True),  
    db.Column('title', db.String, nullable=False),  
    db.Column('description', db.String), 
    db.Column('dashboard', db.Integer, nullable=False),  
    db.Column('frontend', db.Integer, nullable=False),  
    db.Column('categories', db.Integer, nullable=False),   
    db.Column('playlist', db.Integer, nullable=False),                         
    db.Column('thumb', db.String), 
    db.Column('date', db.String, nullable=False),                         
)

metadata_obj.create_all(engine)