# CodeAlpha Task 3: Data Visualization

import pandas as pd
import matplotlib.pyplot as plt

# Load the medical appointments dataset
df = pd.read_csv("KaggleV2-May-2016.csv")

# Display the first five rows
print(df.head())

# Display the dataset size
print("\nDataset shape:", df.shape)


# Count appointment attendance
attendance_counts = df["No-show"].value_counts()

# Calculate percentages
attendance_percentages = (
    attendance_counts / attendance_counts.sum()
) * 100

# Set colors for each category
colors = ["#16A6A1", "#F07870"]

# Create the figure
fig, ax = plt.subplots(figsize=(10, 6))

# Draw the bars
bars = ax.bar(
    ["Attended", "Missed"],
    [
        attendance_counts.get("No", 0),
        attendance_counts.get("Yes", 0)
    ],
    color=colors,
    width=0.55
)

# Add a title and subtitle
fig.suptitle(
    "Medical Appointment Attendance",
    fontsize=18,
    fontweight="bold",
    x=0.12,
    ha="left"
)

ax.set_title(
    "Most scheduled appointments were attended",
    fontsize=11,
    color="#555555",
    loc="left",
    pad=15
)

# Label the axes
ax.set_xlabel("Appointment Status", fontsize=11)
ax.set_ylabel("Number of Appointments", fontsize=11)

# Add count and percentage labels above the bars
for bar, status in zip(bars, ["No", "Yes"]):
    count = attendance_counts.get(status, 0)
    percentage = attendance_percentages.get(status, 0)

    ax.annotate(
        f"{count:,}\n({percentage:.1f}%)",
        xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
        xytext=(0, 8),
        textcoords="offset points",
        ha="center",
        fontsize=11,
        fontweight="bold"
    )

# Style the chart
ax.set_facecolor("#F7F9FC")
fig.patch.set_facecolor("white")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

ax.tick_params(axis="y", length=0)
ax.grid(axis="y", linestyle="--", alpha=0.25)
ax.set_axisbelow(True)

# Add a footer
fig.text(
    0.12,
    0.02,
    "Source: Medical Appointment No Shows dataset",
    fontsize=9,
    color="#666666"
)

# Adjust spacing
plt.tight_layout(rect=[0.08, 0.06, 0.98, 0.90])

# Save the chart as an image
plt.savefig(
    "appointment_attendance.png",
    dpi=300,
    bbox_inches="tight"
)

# Display the chart
plt.show()


# Create age groups
age_bins = [0, 12, 18, 30, 45, 60, 75, 120]
age_labels = [
    "0-12", "13-18", "19-30", "31-45",
    "46-60", "61-75", "76+"
]

# Copy the data so the original remains unchanged
age_df = df.copy()

# Exclude the invalid negative age found during EDA
age_df = age_df[age_df["Age"] >= 0]

# Group patients by age
age_df["Age Group"] = pd.cut(
    age_df["Age"],
    bins=age_bins,
    labels=age_labels,
    include_lowest=True
)

# Calculate the percentage of missed appointments
age_df["Missed"] = (age_df["No-show"] == "Yes").astype(int)

no_show_rates = (
    age_df.groupby("Age Group", observed=False)["Missed"]
    .mean() * 100
)

# Create the chart
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(
    no_show_rates.index.astype(str),
    no_show_rates.values,
    color="#16A6A1",
    width=0.6
)

# Add the title and labels
ax.set_title(
    "No-Show Rate by Age Group",
    fontsize=17,
    fontweight="bold",
    loc="left",
    pad=15
)

ax.set_xlabel("Age Group (Years)", fontsize=11)
ax.set_ylabel("Missed Appointments (%)", fontsize=11)

# Display the percentage above each bar
for bar, rate in zip(bars, no_show_rates.values):
    ax.annotate(
        f"{rate:.1f}%",
        xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
        xytext=(0, 5),
        textcoords="offset points",
        ha="center",
        fontsize=10,
        fontweight="bold"
    )

# Apply the same visual style as the first chart
ax.set_facecolor("#F7F9FC")
fig.patch.set_facecolor("white")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

ax.tick_params(axis="y", length=0)
ax.grid(axis="y", linestyle="--", alpha=0.25)
ax.set_axisbelow(True)

plt.tight_layout()

# Save the chart
plt.savefig(
    "no_show_by_age_group.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# Chart 3: No-show rate by gender

# Calculate the percentage of missed appointments for each gender
gender_no_show = (
    df.groupby("Gender")["No-show"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

# Create the chart
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(
    gender_no_show.index,
    gender_no_show.values,
    color=["#16A6A1", "#F07870"],
    width=0.55
)

# Add the title and labels
ax.set_title(
    "No-Show Rate by Gender",
    fontsize=17,
    fontweight="bold",
    loc="left",
    pad=15
)

ax.set_xlabel("Gender", fontsize=11)
ax.set_ylabel("Missed Appointments (%)", fontsize=11)

# Display percentages above the bars
for bar, rate in zip(bars, gender_no_show.values):
    ax.annotate(
        f"{rate:.1f}%",
        xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
        xytext=(0, 6),
        textcoords="offset points",
        ha="center",
        fontsize=11,
        fontweight="bold"
    )

# Apply the chart style
ax.set_facecolor("#F7F9FC")
fig.patch.set_facecolor("white")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

ax.tick_params(axis="y", length=0)
ax.grid(axis="y", linestyle="--", alpha=0.25)
ax.set_axisbelow(True)

# Add a source note
fig.text(
    0.12,
    0.02,
    "Source: Medical Appointment No Shows dataset",
    fontsize=9,
    color="#666666"
)

plt.tight_layout(rect=[0.08, 0.06, 0.98, 0.95])

# Save the chart
plt.savefig(
    "no_show_by_gender.png",
    dpi=300,
    bbox_inches="tight"
)

# Display the chart
plt.show()

# Chart 4: No-show rate by day of the week

# Convert appointment dates to datetime format
df["AppointmentDay"] = pd.to_datetime(df["AppointmentDay"])

# Extract the day of the week
df["Appointment Weekday"] = df["AppointmentDay"].dt.day_name()

# Calculate the percentage of missed appointments per day
weekday_order = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

# Calculate appointment counts and no-show rates by weekday
weekday_summary = df.groupby("Appointment Weekday")["No-show"].agg(
    Total_Appointments="count",
    Missed_Appointments=lambda x: (x == "Yes").sum()
)

weekday_summary["No_Show_Rate"] = (
    weekday_summary["Missed_Appointments"]
    / weekday_summary["Total_Appointments"]
    * 100
)

# Keep weekdays in calendar order and exclude days with no appointments
weekday_summary = weekday_summary.reindex(weekday_order).dropna(
    subset=["Total_Appointments"]
)

weekday_no_show = weekday_summary["No_Show_Rate"]

# Create the chart
fig, ax = plt.subplots(figsize=(11, 6))

bars = ax.bar(
    weekday_no_show.index,
    weekday_no_show.values,
    color="#16A6A1",
    width=0.65
)

# Add the title and labels
ax.set_title(
    "No-Show Rate by Appointment Day",
    fontsize=17,
    fontweight="bold",
    loc="left",
    pad=15
)

ax.set_xlabel("Day of the Week", fontsize=11)
ax.set_ylabel("Missed Appointments (%)", fontsize=11)

# Display the no-show rate and appointment count above each bar
for bar, day in zip(bars, weekday_no_show.index):
    rate = weekday_no_show[day]
    total = weekday_summary.loc[day, "Total_Appointments"]

    ax.annotate(
        f"{rate:.1f}%\n(n={int(total):,})",
        xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
        xytext=(0, 6),
        textcoords="offset points",
        ha="center",
        fontsize=9,
        fontweight="bold"
    )

# Apply the same visual style
ax.set_facecolor("#F7F9FC")
fig.patch.set_facecolor("white")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

ax.tick_params(axis="y", length=0)
ax.grid(axis="y", linestyle="--", alpha=0.25)
ax.set_axisbelow(True)

plt.xticks(rotation=20, ha="right")
plt.tight_layout()

# Save the chart
plt.savefig(
    "no_show_by_weekday.png",
    dpi=300,
    bbox_inches="tight"
)

# Display the chart
plt.show()

# Chart 5: No-show rate by scholarship status

# Calculate the percentage of missed appointments
scholarship_no_show = (
    df.groupby("Scholarship")["No-show"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

# Use clear category labels
scholarship_labels = [
    "No Scholarship" if status == 0 else "Has Scholarship"
    for status in scholarship_no_show.index
]

# Create the chart
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(
    scholarship_labels,
    scholarship_no_show.values,
    color=["#16A6A1", "#F07870"],
    width=0.55
)

# Add the title and labels
ax.set_title(
    "No-Show Rate by Scholarship Status",
    fontsize=17,
    fontweight="bold",
    loc="left",
    pad=15
)

ax.set_xlabel("Scholarship Status", fontsize=11)
ax.set_ylabel("Missed Appointments (%)", fontsize=11)

# Display percentages above the bars
for bar, rate in zip(bars, scholarship_no_show.values):
    ax.annotate(
        f"{rate:.1f}%",
        xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
        xytext=(0, 6),
        textcoords="offset points",
        ha="center",
        fontsize=11,
        fontweight="bold"
    )

# Apply the chart style
ax.set_facecolor("#F7F9FC")
fig.patch.set_facecolor("white")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

ax.tick_params(axis="y", length=0)
ax.grid(axis="y", linestyle="--", alpha=0.25)
ax.set_axisbelow(True)

# Add a source note
fig.text(
    0.12,
    0.02,
    "Source: Medical Appointment No Shows dataset",
    fontsize=9,
    color="#666666"
)

plt.tight_layout(rect=[0.08, 0.06, 0.98, 0.95])

# Save the chart
plt.savefig(
    "no_show_by_scholarship.png",
    dpi=300,
    bbox_inches="tight"
)

# Display the chart
plt.show()

# Print key findings from the five visualizations

print("\n" + "=" * 40)
print("KEY FINDINGS")
print("=" * 40)

# Finding 1: Overall appointment attendance
print("\n1. OVERALL APPOINTMENT ATTENDANCE")

print(
    f"Attended: {attendance_counts.get('No', 0):,} "
    f"({attendance_percentages.get('No', 0):.1f}%)"
)

print(
    f"Missed: {attendance_counts.get('Yes', 0):,} "
    f"({attendance_percentages.get('Yes', 0):.1f}%)"
)

# Finding 2: No-show rate by age group
print("\n2. NO-SHOW RATE BY AGE GROUP")
print(no_show_rates.round(1).to_string())

# Finding 3: No-show rate by gender
print("\n3. NO-SHOW RATE BY GENDER")
print(gender_no_show.round(1).to_string())

# Finding 4: No-show rate by appointment weekday
print("\n4. NO-SHOW RATE BY APPOINTMENT DAY")
print(weekday_no_show.round(1).to_string())

# Finding 5: No-show rate by scholarship status
print("\n5. NO-SHOW RATE BY SCHOLARSHIP STATUS")

for status, rate in scholarship_no_show.items():
    label = "No Scholarship" if status == 0 else "Has Scholarship"
    print(f"{label}: {rate:.1f}%")

print("\n" + "=" * 40)


# Check the number of appointments scheduled each day

print("\n" + "=" * 45)
print("APPOINTMENT COUNTS BY WEEKDAY")
print("=" * 45)

# Count appointments for each weekday
weekday_counts = df["Appointment Weekday"].value_counts()

# Calculate the no-show rate for each weekday
weekday_summary = df.groupby("Appointment Weekday")["No-show"].agg(
    Total_Appointments="count",
    Missed_Appointments=lambda x: (x == "Yes").sum()
)

weekday_summary["Attended_Appointments"] = (
    weekday_summary["Total_Appointments"]
    - weekday_summary["Missed_Appointments"]
)

weekday_summary["No_Show_Rate_Percent"] = (
    weekday_summary["Missed_Appointments"]
    / weekday_summary["Total_Appointments"]
    * 100
)

# Display every weekday in calendar order
weekday_order = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

weekday_summary = weekday_summary.reindex(weekday_order)

print(weekday_summary.round(2).to_string())

print("\n" + "=" * 45)


