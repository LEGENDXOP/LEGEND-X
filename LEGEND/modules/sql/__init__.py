import re
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import os, sys
from LEGEND import DB_URI, LEGENDX22, telethn
if LEGENDX22 == 1100231654:
   print ("LEGENDX22 ADDED SIR ")
else:
   print ("YOU REMOVED LEGEND X NOW SEE")
   os.execl(sys.executable, sys.executable, *sys.argv)
   telethn.disconnect()

def start() -> scoped_session:
    engine = create_engine(DB_URI, client_encoding="utf8")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()
