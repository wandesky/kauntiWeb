class Permit(object):
    # Dummy permit data
    permits = [
        {
            "permitID": "TCG-SBP-2018-2019-2033",
            "customer": "Williams Cyber Cafe",
            "businessType": "Computer Services",
            "amountPaid": 20000,
            "posta": "51 Lodwar",
            "businessAddress": "Highway Towers",
            "building": "rental",
            "plotNumber": "LR5421",
            "fiscalYear": "2019/2020",
            "validFrom": "01 January 2019 12:00",
            "validTill": "31 December 2019 11:59 PM",
            "issuedBy": "ted",
            "issuedOn": "9 March 2019 1:59 PM",
            "invoiceNumber": "INV-2200",
            "business": "TCG/2018/2019/1000"
        },
        {
            "permitID": "TCG-SBP-2018-2019-1020",
            "customer": "Oti's Workshop",
            "businessType": "Furniture and Repairs",
            "amountPaid": 15000,
            "posta": "12 Lodwar",
            "businessAddress": "Jua Kali Market",
            "building": "market",
            "plotNumber": "LR102",
            "fiscalYear": "2019/2020",
            "validFrom": "01 January 2019 12:00",
            "validTill": "31 December 2019 11:59 PM",
            "issuedBy": "ben",
            "issuedOn": "18 February 2019 1:59 PM",
            "invoiceNumber": "INV-3325",
            "business": "TCG/2018/2019/1001"
        },
        {
            "permitID": "TCG-SBP-2018-2019-1224",
            "customer": "Wajenzi wa Wakanda",
            "businessType": "Construction",
            "amountPaid": 30000,
            "posta": "2244 Wakanda-Lodwar",
            "businessAddress": "Wakanda Center",
            "building": "isolated",
            "plotNumber": "LR1550",
            "fiscalYear": "2019/2020",
            "validFrom": "01 January 2019 12:00",
            "validTill": "31 December 2019 11:59 PM",
            "issuedBy": "ken",
            "issuedOn": "15 February 2019 1:59 PM",
            "invoiceNumber": "INV-3324",
            "business": "TCG/2018/2019/1002"
        },
        {
            "permitID": "TCG-SBP-2018-2019-1278",
            "customer": "Okoti Engineers",
            "businessType": "Construction",
            "amountPaid": 30000,
            "posta": "2244 Kitale",
            "businessAddress": "Mjengo Towers",
            "building": "isolated",
            "plotNumber": "LR1526",
            "fiscalYear": "2019/2020",
            "validFrom": "01 January 2019 12:00",
            "validTill": "31 December 2019 11:59 PM",
            "issuedBy": "ken",
            "issuedOn": "10 February 2019 1:59 PM",
            "invoiceNumber": "INV-3323",
            "business": "TCG/2018/2019/1003"
        },
        {
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
            "business": "TCG/2018/2019/1004"
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
        if len(orders) == 0:
            return {"permitID": "invalid"}
        else:
            return orders[0]

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
