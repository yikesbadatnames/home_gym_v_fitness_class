# -------------------------------
#Importing Dependencies
# -------------------------------
import csv
import os
# Organisation Libraries --------
import pandas as pd
import numpy as np

# SQL Libraries -----------------
from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import inspect
from sqlalchemy import text
from config import password
from sqlalchemy import extract