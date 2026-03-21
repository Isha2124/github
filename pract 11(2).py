import matplotlib.pyplot as plt

# Data (number of recruitments)
companies = ["Microsoft","Google","Amazon","IBM","Deloitte","Capgemini","ATOS","Amdocs"]
recruitments = [120, 150, 180, 100, 90, 140, 80, 110]

# a) Bar Chart
plt.bar(companies, recruitments)
plt.title("Company Recruitment Data")
plt.xlabel("Companies")
plt.ylabel("Number of Recruitments")
plt.xticks(rotation=30)
plt.show()

# b) Pie Chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

# c) Customized Pie Chart
colors = ["red","blue","green","yellow","purple","orange","pink","cyan"]
explode = [0,0,0.1,0,0,0,0,0]   # highlight Amazon

plt.pie(recruitments, labels=companies, autopct='%1.1f%%',
        colors=colors, explode=explode, shadow=True)
plt.title("Customized Pie Chart")
plt.show()

# d) Doughnut Chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
centre_circle = plt.Circle((0,0))