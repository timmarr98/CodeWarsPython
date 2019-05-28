def calculate_years(principal, interest, tax, desired):
  years = 0
  if(principal == desired):
       return 0
  else:
         while principal < desired:
              principalYear = (principal*interest)
              taxYear = principalYear*tax
              principal = principal + principalYear - taxYear
              years+=1
         return years   
