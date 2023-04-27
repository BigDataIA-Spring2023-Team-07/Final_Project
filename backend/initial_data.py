from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, TEXT, Identity, inspect, select, update,insert
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
from datetime import datetime

config={'DB_USER_NAME':'postgres',
        'DB_PASSWORD':'shubh',
        'DB_ADDRESS':'localhost',
        'DB_NAME':'final_project'}

engine=create_engine('postgresql://'+str(config.get('DB_USER_NAME'))+':'+str(config.get('DB_PASSWORD'))+'@'+str(config.get('DB_ADDRESS'))+':5432/'+str(config.get('DB_NAME')))

connection = engine.connect()
metadata = MetaData()
user_data = Table('User_Details', metadata, autoload_with=engine)

# Print the column names
print(user_data.columns.keys())

# Print full table metadata
print(repr(metadata.tables['User_Details']))

query = insert(user_data) 
values_list = [{'UserID':'dhanush@gmail.com', 'Password':'abcd', 'Name':'Dhanush', 'Plan':'Basic'},
               {'UserID':'nishant@gmail.com', 'Password':'abcd', 'Name':'Nishant', 'Plan':'Standard'},
               {'UserID':'shubham@gmail.com', 'Password':'abcd', 'Name':'Shubham', 'Plan':'Premium'}
               ]

ResultProxy = connection.execute(query,values_list)
query=select(user_data.c.UserID,user_data.c.Password,user_data.c.Name,user_data.c.Plan)
results = connection.execute(query).fetchall()
connection.commit()
print(results)

user_activity = Table('user_activity', metadata, autoload_with=engine)

# Print the column names
print(user_activity.columns.keys())

# # Print full table metadata
print(repr(metadata.tables['user_activity']))

query = insert(user_activity) 
values_list = [{'UserID':'dhanush@gmail.com', 'Source':'Boston', 'Destination':'New York', 'S_Date':'2023/05/01', 'E_Date':'2023/05/15', 'Duration':'5', 'Budget':'2500' , 'TotalPeople':'4', 'PlacesToVisit': 'Edge,Central Park, xyz','time_stamp':datetime.utcnow(),'hit_count':0},
               {'UserID':'nishant@gmail.com', 'Source':'Boston', 'Destination':'New York', 'S_Date':'2023/05/01', 'E_Date':'2023/05/15', 'Duration':'5', 'Budget':'2500' , 'TotalPeople':'4', 'PlacesToVisit': 'Edge,Central Park, xyz','time_stamp':datetime.utcnow(),'hit_count':0},
               {'UserID':'shubham@gmail.com', 'Source':'Boston', 'Destination':'San francisco', 'S_Date':'2023/05/05', 'E_Date':'2023/05/15', 'Duration':'10', 'Budget':'3500' , 'TotalPeople':'2', 'PlacesToVisit': 'Golden Gate Bridge,xyz','time_stamp':datetime.utcnow(),'hit_count':0},
               {'UserID':'dhanush@gmail.com', 'Source':'New york', 'Destination':'Boston', 'S_Date':'2023/06/01', 'E_Date':'2023/06/15', 'Duration':'5', 'Budget':'2500' , 'TotalPeople':'4', 'PlacesToVisit': 'Boston Commons, Northeastern University, seaport','time_stamp':datetime.utcnow(),'hit_count':0},
               ]

ResultProxy = connection.execute(query,values_list)
query=select(user_activity.c.UserID,user_activity.c.Source,user_activity.c.Destination,user_activity.c.S_Date,user_activity.c.E_Date,user_activity.c.Duration,user_activity.c.Budget,user_activity.c.TotalPeople,user_activity.c.PlacesToVisit,user_activity.c.time_stamp,user_activity.c.hit_count)
results = connection.execute(query).fetchall()
connection.commit()
print(results)


plan = Table('plan', metadata, autoload_with=engine)

# Print the column names
print(plan.columns.keys())

# # Print full table metadata
print(repr(metadata.tables['plan']))

query = insert(plan) 
values_list = [{'plan_name':'Basic', 'api_limit':10},
               {'plan_name':'Standard', 'api_limit':25},
               {'plan_name':'Premium', 'api_limit':50}
               ]

ResultProxy = connection.execute(query,values_list)
query=select(plan.c.plan_name,plan.c.api_limit)
results = connection.execute(query).fetchall()
connection.commit()
print(results)


aoi = Table('AOI', metadata, autoload_with=engine)

# Print the column names
print(aoi.columns.keys())

# # Print full table metadata
print(repr(metadata.tables['AOI']))

query = insert(aoi) 
values_list = [{'UserID':'dhanush@gmail.com', 'Interest':'tourist attraction, hiking'},
               {'UserID':'nishant@gmail.com', 'Interest':'tourist attraction, hiking, food'},
               {'UserID':'shubham@gmail.com', 'Interest':'tourist attraction, hiking, museums'}
               ]

ResultProxy = connection.execute(query,values_list)
query=select(aoi.c.UserID,aoi.c.Interest)
results = connection.execute(query).fetchall()
connection.commit()
print(results)