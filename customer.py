from tabulate import tabulate
import math

class CustomerMembership:
    data_membership = {
        'Sumbul': 'Platinum', 
        'Ana': 'Gold', 
        'Cahya': 'Platinum'
        }


    def __init__(self, username, membership = None):
        self.username = username
        # self.monthly_expense = monthly_expense
        # self.monthly_income = monthly_income
        self.membership = membership

    def show_benefit(self):
        benefit = [
                    ["Platinum", "15%", "Benefit Gold + Silver + Cashback max. 30%"],
                    ["Gold", "10%", "Benefit Silver + Voucher Ojek Online"],
                    ["Silver", "8%", "Voucher Makanan"],
                ]

        benefit_headers = ["Membership", "Discount", "Another Benefit"]

        print('Paccommerce Membership Benefit')
        print(tabulate(benefit,benefit_headers,tablefmt ='github',stralign = 'center'))

    def show_requirements(self):
        self.requirements = [
            ['Platinum', 8, 15],
            ['Gold', 6, 10],
            ['Silver', 5, 7]
        ]

        requirements_headers = ['Membership', 'Monthly Expense (juta)', 'Monthly Income (juta)']

        print('Requirements Membership PacCommerce')
        print(tabulate(self.requirements, requirements_headers, tablefmt='github', stralign = 'center'))

    def predict_membership(self, monthly_expense, monthly_income):
        for data in self.requirements:
            if 'Platinum' in data:
                expense_platinum = data[1]
                income_platinum = data[2]

                r_user_platinum = (((monthly_expense - expense_platinum) ** 2) + ((monthly_income - income_platinum) ** 2)) ** 0.5
                print(r_user_platinum)
            
            if 'Gold' in data:
                expense_gold = data[1]
                income_gold = data[2]

                r_user_gold = (((monthly_expense - expense_gold) ** 2) + ((monthly_income - income_gold) ** 2)) ** 0.5
                print(r_user_gold)

            if 'Silver' in data:
                expense_silver = data[1]
                income_silver = data[2]

                r_user_silver = (((monthly_expense - expense_silver) ** 2) + ((monthly_income - income_silver) ** 2)) ** 0.5
                print(r_user_silver)

        if r_user_platinum > r_user_gold:
            if r_user_gold > r_user_silver:
                member = 'Silver'
                self.data_membership[self.username] = member
                return(f'Predict membership: {member}')
            else:
                member = 'Gold'
                self.data_membership[self.username] = member
                return(f'Predict membership: {member}')
        elif r_user_platinum < r_user_gold:
            if r_user_platinum < r_user_silver:
                member = 'Platinum'
                self.data_membership[self.username] = member
                return(f'Predict membership: {member}')
            else:
                member = 'Silver'
                self.data_membership[self.username] = member
                return(f'Predict membership: {member}')

    def calculate_price(membership, list_harga_barang):
        print(1)