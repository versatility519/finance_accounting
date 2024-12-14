## Project Installation

    python -m venv venv

    .\venv\Scripts\activate

    pip install -r requirements.txt

    python manage.py runserver

## API Documentation


### api/LedgerAccount 


#### GET
    [
        {
            "id": 1,
            "name": "Cash",
            "type": "debit",
            "type_status": "increase"
        },
        {
            "id": 2,
            "name": "Telephone",
            "type": "credit",
            "type_status": "decrease"
        },
        {
            "id": 3,
            "name": "Equipment",
            "type": "credit",
            "type_status": "decrease"
        }
    ]
#### POST
    {
        "name": "Cash",
        "type": "credit",
        "type_status": "decrease" 
    }
#### UPADTE
*api/LedgerAccount/2*

    {
        "name": "Inventory",
        "type": "credit",
        "type_status": "decrease" 
    }

#### DELETE
    api/LedgerAccount/2


### api/invoice 

#### GET
    [
        {
            "id": 1,
            "invoice_num": "INV_1",
            "date_created": "2022-01-24",
            "supplier": {
                "id": 2,
                "name": "william",
                "address": "san diego"
            },
            "items": {
                "id": 1,
                "name": "school",
                "description": "student",
                "unit": "55",
                "quantity": 53.0,
                "price": 33.0,
                "total_amount": 1749.0,
                "tax_group": 1
            },
            "required_date": "2023-01-24",
            "status": "Paid",
            "ship_to": "ship",
            "bill_to": "bill",
            "docs": {
                "id": 1,
                "name": "book",
                "docs": "thanks"
            },
            "terms": {
                "id": 1,
                "name": "store"
            },
            "tax": {
                "id": 2,
                "name": "tomas",
                "rate": 6.0,
                "description": "cool"
            }
        },
        {
            "id": 2,
            "invoice_num": "INV_2",
            "date_created": "2023-05-01",
            "supplier": {
                "id": 1,
                "name": "Food Delivery Company",
                "address": "texas"
            },
            "items": {
                "id": 2,
                "name": "Item B",
                "description": "Description of Item B",
                "unit": "us",
                "quantity": 3.0,
                "price": 15.0,
                "total_amount": 45.0,
                "tax_group": 1
            },
            "required_date": "2024-05-01",
            "status": "Paid",
            "ship_to": "ship",
            "bill_to": "bill",
            "docs": {
                "id": 1,
                "name": "book",
                "docs": "thanks"
            },
            "terms": {
                "id": 1,
                "name": "store"
            },
            "tax": {
                "id": 1,
                "name": "alex",
                "rate": 4.0,
                "description": "cool"
            }
        }
    ]
#### POST
    {
        "invoice_num": "INV_3",
        "date_created": "2023-05-01",
        "supplier": "1",
        "items": "2",
        "required_date": "2024-05-01",
        "status": "Paid",
        "ship_to": "ship",
        "bill_to": "bill",
        "docs":  "2",
        "terms":  "2",
        "tax":  "1"
    }

#### UPADTE
    
*api/invoices/2*

    {
        "invoice_num": "INV_2",
        "date_created": "2024-10-24",
        "supplier": {
            "id": 2,
            "name": "william",
            "address": "Houston"
        },
        "items": {
            "id": 1,
            "name": "school",
            "description": "student",
            "unit": "55",
            "quantity": 53.0,
            "price": 33.0,
            "total_amount": 1749.0,
            "tax_group": 1
        },
        "required_date": "2023-01-24",
        "status": "Paid",
        "ship_to": "ship",
        "bill_to": "bill",
        "docs": {
            "id": 1,
            "name": "book",
            "docs": "thanks"
        },
        "terms": {
            "id": 1,
            "name": "store"
        },
        "tax": {
            "id": 2,
            "name": "tomas",
            "rate": 6.0,
            "description": "cool"
        }
    }

#### DELETE
    api/invoices/2



### api/contacts 

#### GET
    [
        {
            "id": 1,
            "Fname": "Stefan",
            "Lname": "Tom",
            "email": "Tom@gmail.com",
            "phone": "123123123",
            "address": "New York, USA",
            "role": "admin",
            "supplier": {
                "id": 1,
                "name": "Food Delivery Company",
                "address": "texas"
            }
        },
        {
            "id": 2,
            "Fname": "Tony",
            "Lname": "Tre",
            "email": "Tre@gmail.com",
            "phone": "123456789",
            "address": "Houston, USA",
            "role": "manager",
            "supplier": {
                "id": 2,
                "name": "william",
                "address": "san diego"
            }
        }
    ]

#### POST
    {
        "Fname": "Fname Updated",
        "Lname": "Tom",
        "email": "Tom@gmail.com",
        "phone": "123123123",
        "address": "New York, USA",
        "role": "admin",
        "supplier": {
            "id": 2,
            "name": "updated supplier",
            "address": "Texas"
        }
    }
#### UPADTE
    {
        "Fname": "Fname Updated",
        "Lname": "Lname Updated",
        "email": "Updated@gmail.com",
        "phone": "123123123",
        "address": "New York, USA",
        "role": "admin",
        "supplier": {
            "id": 2,
            "name": "updated supplier",
            "address": "Texas"
        }
    }
#### DELETE
    api/contacts/3

### api/invoiceitems 

#### GET
    [
        {
            "id": 1,
            "name": "Item A",
            "description": "Description of Item A"
            "unit": "55",
            "quantity": 53.0,
            "price": 33.0,
            "total_amount": 1749.0,
            "tax_group": 1
        },
        {
            "id": 2,
            "name": "Item B",
            "description": "Description of Item B",
            "unit": "pcs",
            "quantity": 3.0,
            "price": 15.0,
            "total_amount": 45.0,
            "tax_group": 1
        },
        {
            "id": 3,
            "name": "Item C",
            "description": "Description of Item C",
            "unit": "us",
            "quantity": 3.0,
            "price": 15.0,
            "total_amount": 45.0,
            "tax_group": 1
        }
    ]

#### POST
        {
            "name": "New Item",
            "description": "Description of New Item",
            "unit": "kg",
            "quantity": 3.0,
            "price": 150.0,
            "tax_group":1
        }
#### UPADTE
    # When pk = 3, /api/invoiceitem/3

    #### From
        {
            "name": "Item C",
            "description": "Description of Item C",
            "unit": "us",
            "quantity": 3.0,
            "price": 15.0,
            "tax_group": 1
        }
          #### To
        {
            "name": "Updated Item C",
            "description": "Description of Updated Item C",
            "unit": "kg",
            "quantity": 3.0,
            "price": 15.0,
            "tax_group": 1
        }

#### DELETE
    When pk = 3, /api/invoiceitem/3

### api/suppliers 

#### GET
    [
        {
            "id": 1,
            "name": "Food Delivery Company",
            "address": "Texas"
        },
        {
            "id": 2,
            "name": "Info-tech Company",
            "address": "San diego"
        },
        {
            "id": 3,
            "name": "Car Manufacturing Company",
            "address": "Canada"
        }
    ]
#### POST
    {
        "name": "Food Delivery Company",
        "address": "New York"
    }
#### UPADTE
    api/suppliers/3
    
    {
        "name": "Car Manufacturing Company",
        "address": "Brazil"
    }
#### DELETE
    When pk = 3, api/suppliers/3
 


### api/transaction 

#### GET
    [
        {
            "id": 1,
            "name": "Transaction 1",
            "t_date": "2023-01-18",
            "amount": 10000.0,
            "description": "First transaction",
            "type": "debit",
            "journalID": 5
        },
        {
            "id": 2,
            "name": "Transaction 2",
            "t_date": "2022-05-18",
            "amount": 50.0,
            "description": "Second transaction",
            "type": "credit",
            "journalID": 4
        },
        {
            "id": 3,
            "name": "Transaction 3",
            "t_date": "2012-02-03",
            "amount": 100.0,
            "description": "Third transaction",
            "type": "debit",
            "journalID": 5
        },
        {
            "id": 4,
            "name": "Transaction 4",
            "t_date": "2024-10-18",
            "amount": 888.0,
            "description": "Forth transaction",
            "type": "credit",
            "journalID": 5
        }
    ]
#### POST
    {
        "name": "Transaction 5",
        "t_date": "2024-10-18",
        "amount": 4312.0,
        "description": "Fifth transaction",
        "type": "credit",
        "journalID": 5
    }
#### UPADTE
    api/transaction/5
    
    {
        "name": "Updated Transaction 5",
        "t_date": "2024-10-18",
        "amount": 4312.0,
        "description": "Fifth transaction",
        "type": "credit",
        "journalID": 5
    }
#### DELETE
    When pk = 3, api/transaction/3
 


### api/journals 

#### GET
    [
        {
            "id": 1,
            "name": "jounal 1",
            "status": "active",
            "s_date": "2024-10-18",
            "e_date": "2024-10-18",
            "number": 1,
            "transactions": [
                {
                    "id": 1,
                    "name": "Transaction 1",
                    "t_date": "2023-01-18",
                    "amount": 10000.0,
                    "description": "First transaction",
                    "type": "debit",
                    "journalID": 1
                }
            ],
            "total_debit": 10000.0,
            "total_credit": 0
        },
        {
            "id": 2,
            "name": "New jounal 3",
            "status": "active",
            "s_date": "2024-10-18",
            "e_date": "2024-10-18",
            "number": 55,
            "transactions": [],
            "total_debit": 0,
            "total_credit": 0
        },
        ... ... ...
    ]
     
#### POST
    {
        "name": "New jounal",
        "status": "active",
        "s_date": "2015-10-18",
        "e_date": "2024-10-18",
        "number": 123,
    }
#### UPADTE

*api/journal/5*
    
    {
        "name": "Change Journal Name",
        "status": "active",
        "s_date": "2024-10-18",
        "e_date": "2024-10-18",
        "number": ** 231 **,
        "transactions": [
            {
                "id": 3,
                "name": "Transaction 3",
                "t_date": "2012-02-03",
                "amount": 100.0,
                "description": "Third transaction",
                "type": "debit",
                "journalID": 5
            },
            {
                "id": 4,
                "name": "Transaction 4",
                "t_date": "2024-10-18",
                "amount": 888.0,
                "description": "Forth transaction",
                "type": "credit",
                "journalID": 5
            },
            {
                "id": 5,
                "name": "Updated Transaction 5",
                "t_date": "2024-10-20",
                "amount": 4312.0,
                "description": "Fifth transaction",
                "type": "credit",
                "journalID": 5
            }
        ],
        "total_debit": 100.0,
        "total_credit": 5200.0
    }
#### DELETE
    When pk = 3, api/journal/3
 