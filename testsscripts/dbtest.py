from sqlalchemy import create_engine, text

db_connection_string = "mysql+mysqlconnector://ctmkifw1jq461uz3jvee:pscale_pw_x8678RcfjqVIBW6bzKZGqcea5PlzqOwDOujahJ75Gbl@aws.connect.psdb.cloud/dvcasemanagement"

engine = create_engine(db_connection_string)

s0 ="SELECT LAST_INSERT_ID()"

s1 = text(
    "INSERT INTO CaseIndex (title,incidentDate,location,report) Values (:title, :incidentDate, :location, :report) RETURNING id")

s2 = text(
    "INSERT INTO CaseIndex (title,incidentDate,location,report) Values ('test', '2022-07-01', 'Perth', 'Stuff');")
s3 = text("SELECT LAST_INSERT_ID();")

with engine.connect() as conn:
  conn.execute(s2)
  a = conn.execute(s3).all()[0][0]
  res = conn.execute(text("SELECT * from CaseIndex where id = :id"), parameters = dict(id = a))
  conn.commit()
  
  #b = a.all()
 # print(a)

#with engine.connect() as conn:
#  s = text(
#    "INSERT INTO CaseIndex (title,incidentDate,location,report) Values (:title, #:incidentDate, :location, :report) RETURNING CaseIndex.id")
#  newreportrecord = conn.execute(s,
#                                 parameters=dict(title='test',
#                                                 incidentDate='2022-07-01',
#                                                 location='Perth',
#                                                 report='lotsoftext'))

#print(newreportrecord.inserted_primary_key)