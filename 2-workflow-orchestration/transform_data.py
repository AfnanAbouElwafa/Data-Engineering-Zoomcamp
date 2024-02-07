if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd
vendor_id = []

@transformer
def transform(data, *args, **kwargs):
    
    # Remove rows where the passenger count is equal to 0
    tf_data = data[data['passenger_count'] > 0]

    # Remove rows where the the trip distance is equal to zero
    tf_data = tf_data[tf_data['trip_distance'] > 0]

    # Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date.
    tf_data['lpep_pickup_date'] = tf_data['lpep_pickup_datetime'].dt.date

    #the existing values of VendorID in the dataset 
    global vendor_id
    vendor_id = tf_data['VendorID'].unique().tolist()
    print(vendor_id)

    #Count how many columns need to be renamed to snake case
    c = 0
    for col in tf_data.columns:
        if '_' not in col and col[0].isupper():
            print(col)
            c+=1
    print(f"{c} columns need to be renamed to snake case")

    #Rename columns in Camel Case to Snake Case, e.g. VendorID to vendor_id
    tf_data.columns = (tf_data.columns
                .str.replace('(?<=[a-z])(?=[A-Z])', '_', regex=True)
                .str.lower()
             )

    return tf_data


@test
def test_passenger_count(output, *args) -> None:
    
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are trips with 0 passengers'


@test
def test_trip_distance(output, *args) -> None:
    
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are trips with distance = 0'

@test
def test_vendor_id(output, *args) -> None:
    
    assert output['vendor_id'].isin(vendor_id).all() == True, 'Not all vendor_ids are one of the existing values'
