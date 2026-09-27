# matplotlib- Visualization
# i.   A line chart showing the subject 1 marks of all students
# ii.  A bar chart comparing subject1, subject2 and subject 3 marks of all students
# iii. A pie chart showing the contribution of each student’s total marks
# iv.  Draw the histogram of subject 2 marks
# v.   Draw the scatter plot between subject 1 and subject 2 marks
# vi.  Using subplots, create a single figure containing any 4 graphfrom the above questions.
#      Arrange the charts in a 2 × 2 grid and give each subplot an appropriate title and
#      axis labels. Customize the graph by adding title, X-axis label, Y-axis label, legend,
#      different marker styles

import numpy as np
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

# -------------------------------------------------------
# Student data
# -------------------------------------------------------

students = np.array(["A", "B", "C", "D", "E", "F", "G", "H"])

subject1 = np.array([78, 65, 88, 72, 90, 56, 81, 69])
subject2 = np.array([82, 70, 85, 68, 92, 60, 75, 73])
subject3 = np.array([75, 68, 90, 70, 88, 64, 79, 71])

# Calculate total marks
total = subject1 + subject2 + subject3

# -------------------------------------------------------
# i. Line Chart - Subject 1 marks
# -------------------------------------------------------

plt.figure(figsize=(8, 5))
plt.plot(students, subject1, marker='o', linestyle='-', label='Subject 1')
plt.title("Subject 1 Marks of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.savefig("Figures/pgm1-matplotlib-LineChart.png")
plt.show()

# -------------------------------------------------------
# ii. Bar Chart - Compare all three subjects
# -------------------------------------------------------

x = np.arange(len(students))
width = 0.25

plt.figure(figsize=(10, 6))

plt.bar(x - width, subject1, width, label='Subject 1')
plt.bar(x, subject2, width, label='Subject 2')
plt.bar(x + width, subject3, width, label='Subject 3')

plt.title("Comparison of Subject Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(x, students)
plt.legend()
plt.savefig("Figures/pgm1-matplotlib-BarChart.png")
plt.show()

# -------------------------------------------------------
# iii. Pie Chart - Contribution of each student's total marks
# -------------------------------------------------------

plt.figure(figsize=(8, 8))
plt.pie(total, labels=students, autopct='%1.1f%%')
plt.title("Contribution of Each Student's Total Marks")
plt.savefig("Figures/pgm1-matplotlib-PieChart.png")
plt.show()

# -------------------------------------------------------
# iv. Histogram - Subject 2 marks
# -------------------------------------------------------

plt.figure(figsize=(8, 5))
plt.hist(subject2, bins=5, edgecolor='black')
plt.title("Distribution of Subject 2 Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.savefig("Figures/pgm1-matplotlib-Histogram.png")
plt.show()

# -------------------------------------------------------
# v. Scatter Plot - Subject 1 vs Subject 2
# -------------------------------------------------------

plt.figure(figsize=(8, 5))
plt.scatter(subject1, subject2, marker='o',s=80, label='Students')
plt.title("Subject 1 vs Subject 2 Marks")
plt.xlabel("Subject 1 Marks")
plt.ylabel("Subject 2 Marks")
plt.legend()
plt.grid(True)
plt.savefig("Figures/pgm1-matplotlib-Scatterplot.png")
plt.show()


# -------------------------------------------------------
# vi. Subplots - 2 x 2 grid four graphs in a single figure
# -------------------------------------------------------

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# ---- Subplot 1: Line chart ----

axes[0, 0].plot(students, subject1, marker='o', linestyle='-', label='Subject 1')
axes[0, 0].set_title("Subject 1 Marks")
axes[0, 0].set_xlabel("Students")
axes[0, 0].set_ylabel("Marks")
axes[0, 0].legend()
axes[0, 0].grid(True)

# ---- Subplot 2: Bar chart ----

axes[0, 1].bar(x - width, subject1, width, label='Subject 1')
axes[0, 1].bar(x, subject2, width, label='Subject 2')
axes[0, 1].bar(x + width, subject3, width, label='Subject 3')
axes[0, 1].set_title("Subject-wise Marks Comparison")
axes[0, 1].set_xlabel("Students")
axes[0, 1].set_ylabel("Marks")
axes[0, 1].set_xticks(x)
axes[0, 1].set_xticklabels(students)
axes[0, 1].legend()

# ---- Subplot 3: Histogram ----

axes[1, 0].hist(subject2, bins=5, edgecolor='black')
axes[1, 0].set_title("Subject 2 Marks Distribution")
axes[1, 0].set_xlabel("Marks")
axes[1, 0].set_ylabel("Number of Students")

# ---- Subplot 4: Scatter plot ----

axes[1, 1].scatter(subject1, subject2, marker='o', s=80, label='Students')
axes[1, 1].set_title("Subject 1 vs Subject 2")
axes[1, 1].set_xlabel("Subject 1 Marks")
axes[1, 1].set_ylabel("Subject 2 Marks")
axes[1, 1].legend()
axes[1, 1].grid(True)

# Overall title
fig.title("Student Marks Analysis", fontsize=16)

# Adjust spacing
#plt.tight_layout()
plt.savefig("Figures/pgm1-matplotlib-Subgraph.png")
plt.show()