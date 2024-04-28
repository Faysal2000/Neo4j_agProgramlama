from neo4j import GraphDatabase
import json


URI = "bolt://localhost:7687"
AUTH = ("faysalelbeg", "Faysal2000@")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()