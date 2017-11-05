
# coding: utf-8

# In[97]:


# Import Dependencies
import csv
import os.path


# In[98]:


# Files to load and output (Remember to change these)
bank_csv = os.path.join('..','Resources', 'budget_data_1.csv')
new_data_output = os.path.join('..', 'output' , 'bank_revenue_1.txt')


# In[104]:


# Set empty list variables
total_months = 0
total_revenue = 0
prior_revenue = 0
month = []
change_month = []
revenue = []
total_revenue = 0


with open(bank_csv, newline="") as bank_data:
    csvreader = csv.reader(bank_data, delimiter=',')

    next(csvreader, None)
    for row in csvreader:
        

        total_months = total_months + 1
        total_revenue = total_revenue + float(row[1])

        
        revenue_change = float(row[1]) - prior_revenue
        prior_revenue = float(row[1])
        revenue_change_list = revenue_change_list + [revenue_change]
        change_month = change_month + [row[0]]

revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

# Print Summary
summary = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: {total_revenue}\n"
    f"Average Revenue Change: {revenue_avg:.2f}\n"
    f"Greatest Increase in Revenue: {greatest_increase[1]}\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[1]}\n")

# Print the output (to terminal)
print(summary)

# Export the results to text file
with open(new_data_output, "w", newline="") as txt_file:
    txt_file.write(output)




# In[77]:


# Generate Output Summary
#output = (
 #   f"\nFinancial Analysis\n"
  #  f"----------------------------\n"
   # f"Total Months: {total_months}\n"
    #f"Total Revenue: ${total_revenue}\n"
    #f"Average Revenue Change: ${revenue_avg}\n"
    ##f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    #f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
#print(output)

# Export the results to text file
#with open(new_data_output, "w") as txt_file:
 #   txt_file.write(output)

