#!/usr/bin/env python3
""" inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """Function"""
    documents = mongo_collection.insert_one(kwargs)
    return documents.inserted_id
