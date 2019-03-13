class Permit(object):
    permits = [
        {
            # Dummy permit data
            "permitID": "TCG-SBP-2018-2019-1276",
            "customer": "XYZ Company",
            "businessType": "Hotel and Catering",
            "amountPaid": 25000,
            "posta": "2244 Nairobi",
            "businessAddress": "XYZ Premises",
            "building": "isolated",
            "plotNumber": "LR2020",
            "fiscalYear": "2019/2020",
            "validFrom": "01 January 2019 12:00",
            "validTill": "31 December 2019 11:59 PM",
            "issuedBy": "ken",
            "issuedOn": "10 March 2019 1:59 PM",
            "invoiceNumber": "INV-3322",
        },

        {
            # Dummy parcel data
            "parcel_id": 0,
            "permitID": "jj",
            "placedBy": 0,
            "weight": "2kg",
            "weightmetric": "dummyweightmetric",
            "sentOn": "dummysentOn",
            "deliveredOn": "dummydeliveredOn",
            "status": "dummystatus",
            "parcel_from": "dummyparcel_from",
            "parcel_to": "dummyparcel_to",
            "currentlocation": "dummycurrentlocation"
        },
        {
            # Dummy parcel data
            "parcel_id": 0,
            "permitID": "jk",
            "placedBy": 0,
            "weight": "4kg",
            "weightmetric": "dummyweightmetric",
            "sentOn": "dummysentOn",
            "deliveredOn": "dummydeliveredOn",
            "status": "dummystatus",
            "parcel_from": "dummyparcel_from",
            "parcel_to": "dummyparcel_to",
            "currentlocation": "dummycurrentlocation"
        }
    ]

    def __init__(self, placedBy, weight, weightmetric, sentOn, deliveredOn, status, parcel_from, parcel_to, currentlocation):
        self.parcel_id = len(Permit.permits)
        self.placedBy = placedBy
        self.weight = weight
        self.weightmetric = weightmetric
        self.sentOn = sentOn
        self.deliveredOn = deliveredOn
        self.status = status
        self.parcel_from = parcel_from
        self.parcel_to = parcel_to
        self.currentlocation = currentlocation


    def get_all_parcels(self = None):
        return Permit.permits

    # Previous method to retrieve specific permit
    # def get_specific_parcel(self = None, parcel_id = None):
    #     return Permit.permits[parcel_id]

    # Retrieving info about speficic permit
    def get_specific_parcel(self = None, permit_id = None):
        orders = []
        for item in Permit.permits:
            if item["permitID"] == permit_id:
                orders.append(item)
        # orders.append(next((item for item in Parcel.parcels if item["placedBy"] == user_id), None))
        # the above line could have been cool, but again it only captures the first positive dictionary
        return orders

    def get_orders_by_specific_user(self = None, user_id = None):
        orders = []
        for item in Permit.permits:
            if item["placedBy"] == user_id:
                orders.append(item)
        # orders.append(next((item for item in Parcel.parcels if item["placedBy"] == user_id), None))
        # the above line could have been cool, but again it only captures the first positive dictionary
        return orders

    def post_parcel(self):
        Permit.permits.append(
            {
                "id": len(Permit.permits),
                "placedBy": self.placedBy,
                "weight": self.weight,
                "weightmetric": self.weightmetric,
                "sentOn": self.sentOn,
                "deliveredOn": self.deliveredOn,
                "status": self.status,
                "parcel_from": self.parcel_from,
                "parcel_to": self.parcel_to,
                "currentlocation": self.currentlocation
            }
        )
        return "success"
