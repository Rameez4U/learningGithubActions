'''
MER-35 Lambda: Sage API

AWS lambda for incremental sage process

'''
import os
import json
import boto3
from sageintacctsdk import SageIntacctSDK

def init_sage_connection(sender_id,sender_password,user_id,company_id,user_password):
    connection = SageIntacctSDK(
        sender_id=sender_id,
        sender_password=sender_password,
        user_id=user_id,
        company_id=company_id,
        user_password=user_password
    )
    return connection

def readIncremental(Dimension):
    table_name = 'IncrementalProcess'
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    response = table.get_item(
        Key={
            'Dimension': Dimension,
        }
    )

    item = response.get('Item', None )

    return item

def updateIncremental(Dimension, createDate, ModifiedDate):
    '''
    :param Dimension: Name of Dimension
    :param createDate: Max createDate in recent Run
    :param ModifiedDate: Max ModifiedDate in recent Run
    :return: Success Message
    '''

    print("We are updating Dimension -> ", Dimension )
    table_name = 'IncrementalProcess'
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    table.put_item(
        Item={
            'Dimension': Dimension,
            'createDate': createDate,
            'ModifiedDate': ModifiedDate,
        }
    )

    print( "Success Fulling Update it")

def loadDiminsion(connection, Dimension):

    item = readIncremental(Dimension)
    if item:
        pass
    else:
        response = connection.__getattribute__(Dimension).read_all()


def lambda_handler(event, context):
    sender_id = os.environ.get("SENDER_ID", "")
    sender_password = os.environ.get("SENDER_PASSWORD", "")
    user_id = os.environ.get("USER_ID", "")
    company_id = os.environ.get("COMPANY_ID", "")
    user_password = os.environ.get("USER_PASSWORD", "")


    connection = init_sage_connection(sender_id,sender_password,user_id,company_id,user_password)



    get_initial_contacts(table_name)


class Data:
    def __init__(self):
        self.dhruvil = "Dhr"

class Name():
    def __init__(self, name ):
        self.name = Data()

name = Name( "s")
a = name.__getattribute__("name")
