class loanCal():

        def __init__(self):
            print("Welcome to Loan Calculator")

        # compute the total payment.
        def Payment_Computation(self):
                month = self.Getting_Payment_in_Monthly(
                    float(self.amt.get()),
                    float(self.Int_for_Annual.get()) / 1200,
                    int(self.yrs.get()))

                self.mon_payment.set(format(month, '10.2f'))

                tot = float(self.mon_payment.get()) * 12 * int(self.yrs.get())

                self.tot_payment.set(format(tot, '10.2f'))

        def Getting_Payment_in_Monthly(self, Amount_Loan, mon_rate_interest, no_of_yrs):
                 month = Amount_Loan * mon_rate_interest / (1- 1 / (1 + mon_rate_interest) ** (no_of_yrs * 12))
                 return month