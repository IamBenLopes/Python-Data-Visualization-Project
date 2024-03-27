# Benjamin Lopes
# Data Visualization Project

print("We have importated the data set and processing the inforamtion. This will take 1-2 mins. Please wait.")

import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt


# 1.) Open Student Data Sheet
dv_univ_sd = pd.read_excel('Generic University Data Updated.xlsx', sheet_name='Student Data')
print("Sheet: 'Student Data' was read into a pandas dataframe!")

# 2.) Print the dimension of the dataset
print("The shape is ", dv_univ_sd.shape,".\n")

# 3.) Print the top 5 rows of the dataset and the bottom 5 rows.
print(dv_univ_sd.head())
print("\n",dv_univ_sd.tail())

# 4.) Drop [Aid type, ID, Pell Grant Amount, Postal Code, City} from the sheet
dv_univ_sd.drop(['Aid Type', 'City', 'ID','Pell Grant Amount', 'Postal Code'], axis=1, inplace=True)
print("\nI dropped 'Aid Type', 'City', 'ID','Pell Grant Amount', 'Postal Code' from the colomns")

# 5.) Print the top 5 rows and see how the data set was changed
print("\n",dv_univ_sd.head())

# 6.) Filtering information based on the criteria
columns_to_display = ['Academic Year', 'Current GPA', 'Ethnicity', 'Gender', 'First Name', 'Last Name', 'Program', 'SAT', 'Scholarship Amount', 'School', 'State']

# 6a.) Show the scholarship information (the whole row: year, GPA, Ethnicity, Gender, Name, Program, SAT, Scholarship Amount, School, State) for California
california_students = dv_univ_sd[dv_univ_sd['State'] == 'California']
print("\nCalifornia Students:")
print(california_students[columns_to_display])

# 6b.) Show the scholarship information (the whole row: year, GPA, Ethnicity, Gender, Name, Program, SAT, Scholarship Amount, School, State) for Female Students
female_students = dv_univ_sd[dv_univ_sd['Gender'] == 'female']
print("\nFemale Students:")
print(female_students[columns_to_display])



# 7.) Open School Sheet
print("\nWe will now open the school sheet and complete steps 7-12.")
dv_univ_sch = pd.read_excel('Generic University Data Updated.xlsx', sheet_name='Schools')
print("\nSheet: 'Schools' was read into a pandas dataframe!")

# 8/9.) Define new variable: year, to combine years from 2008-2018
year_columns = [year for year in range(2008, 2019)]
# 8/9.) Add the Total column to the sheet
dv_univ_sch['Total'] = dv_univ_sch[year_columns].sum(axis=1)

# 10.) Plot a line graph of the scholarship amount from the School of Business between 2008-2018 
Business_and_Management = dv_univ_sch[dv_univ_sch['School'] == 'Business and Management']

# 11.) Add Title, ylable, xlable
# For all the plots, I choose to save the file because with out doing so I wasn't able to see all of the graphs when i did plt.show

scholarship_amounts = Business_and_Management[year_columns]
plt.figure(figsize=(10, 6))
plt.plot(year_columns, scholarship_amounts.values[0], marker='o', linestyle='-')
plt.title('Scholarship Amount from Business and Management (2008-2018)')
plt.xlabel('Year')
plt.ylabel('Scholarship Amount')
plt.grid(True)
plt.savefig('Business_and_Management_plot.png')  
plt.close()  
print("\nFile Saved: Business_and_Management_plot.png")


# 12.) Plot a line graph of scholarship amounts from the five schools, which one has the highest amount of scholarship in 2018
five_schools = ['Health Sciences', 'Social Sciences', 'Arts and Humanities', 'Business and Management', 'Engineering']

plt.figure(figsize=(10, 6))
highest_scholarship_2018 = 0
highest_scholarship_school = None

for school in five_schools:
    school_data = dv_univ_sch[dv_univ_sch['School'] == school]
    if not school_data.empty:
        scholarship_amounts = school_data[year_columns]
        plt.plot(year_columns, scholarship_amounts.values[0], marker='o', linestyle='-', label=school)
        if scholarship_amounts[2018].values[0] > highest_scholarship_2018:
            highest_scholarship_2018 = scholarship_amounts[2018].values[0]
            highest_scholarship_school = school

plt.title('Scholarship Amounts from Five Schools (2008-2018)')
plt.xlabel('Year')
plt.ylabel('Scholarship Amount')
plt.grid(True)
plt.legend()
plt.savefig('Five_Schools_plot.png')
plt.close()
print("\nFile Saved: Five_Schools_plot.png")
print(f"\nThe school with the highest scholarship amount in 2018 is {highest_scholarship_school} with {highest_scholarship_2018}.")

# 1.) Open Program Sheet
print("\nWe will now open the program sheet and complete the final 5 steps.")
dv_univ_prog = pd.read_excel('Generic University Data Updated.xlsx', sheet_name='Programs')
print("\nSheet: 'Programs' was read into a pandas dataframe!")

# 2.) Add the Total column
year_columns = [year for year in range(2008, 2019)]
dv_univ_prog['Total'] = dv_univ_prog[year_columns].sum(axis=1)

# 3.) Compare the trend of top 5 program that have the highest amount of scholarship between 2008-2018
top_5_programs = dv_univ_prog.nlargest(5, 'Total')
top5 = top_5_programs.set_index('Program')[year_columns].T

# 4.) Plot an Area graph (stacked)
top5.plot(kind='area', alpha=0.25, stacked=True, figsize=(20, 10))
plt.title('Scholarship Trend of Top 5 Programs (2008-2018)')
plt.ylabel('Scholarship Amount')
plt.xlabel('Years')
plt.savefig('Stacked_Graph_Top5.png')
plt.close()
print("\nFile Saved: Stacked_Graph_Top5.png")

dv_univ_prog.set_index('Program', inplace=True)

# 5.) What is the scholarship amount distribution for Computer Science, Information Management, and Business Administration between 2008-2018
specific_programs = ['Computer Science', 'Information Management', 'Business Administration']
program_data = dv_univ_prog.loc[specific_programs, year_columns].transpose()
dv_univ_prog.head()
# 5a.) Plot the histogram graph
print("\nNow we will plot the histogram graph for the specific programs")
program_data.plot(kind='hist', figsize=(10, 6))
plt.title('Histogram of Scholarship Amount for Three Programs from 2008-2018')
plt.ylabel('Number of Years')
plt.xlabel('Scholarship Amount')
plt.savefig('Histogram_Programs_Top5.png')
plt.close()
print("\nFile Saved: Histogram_Programs_Top5.png")

print("Have a moment to check out the custom graphs generated based on the data set entered!")