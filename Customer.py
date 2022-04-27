# Bobo Yan
# 4/23/2022
# 3900 activity 7 Object Oriented Python Exercise

class Customer():
    def __init__(self, cust_num, fname, lname, company, street, city, state, zipcode):
        self.cust_ID = int(cust_num)
        self.fname = fname
        self.lname = lname
        self.company = company
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode


    def __str__(self):
        return self.fname + " " + self.lname
        #+ str(self.cust_fullAddress))

    def cust_name(self):
        return self.fname, self.lname

    def cust_fullAddress(self):
        return self.street, self.city, self.state, self.zipcode



    def cust_ID(self):
        return self.cust_ID

    def cust_company(self):
        return self.company

