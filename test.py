from datetime import date, timedelta
import random
import calendar
import pandas as pd

# Define the team members
C1_available = ["P1", "P2", "P3"]        # Can do both C1 and C2
C2_only = ["P4", "P5"]                   # Can only do C2

# Date range: today to end of next month
today = date.today()
year, month = today.year, today.month

# Calculate the last day of next month
next_month = month + 1 if month < 12 else 1
next_month_year = year if month < 12 else year + 1
last_day_next_month = calendar.monthrange(next_month_year, next_month)[1]
end_date = date(next_month_year, next_month, last_day_next_month)

# Create list of days from today to end of next month
date_range = [today + timedelta(days=i) for i in range((end_date - today).days + 1)]

# Schedule
schedule = []

# Shuffle queues for pseudo-random fair distribution
c1_queue = C1_available.copy()
c2_queue = C1_available + C2_only

random.shuffle(c1_queue)
random.shuffle(c2_queue)

# Function to rotate and assign
def get_next_person(queue):
    person = queue.pop(0)
    queue.append(person)
    return person

# Assign each day
for d in date_range:
    c1_person = get_next_person(c1_queue)
    
    # C2 must be P4 or P5
    c2_eligible = [p for p in c2_queue if p in C2_only]
    c2_person = get_next_person(c2_eligible)
    
    schedule.append({
        "Date": d.isoformat(),
        "C1 (Section 1)": c1_person,
        "C2 (Section 2)": c2_person
    })

# Convert to DataFrame for display
df = pd.DataFrame(schedule)
df.to_csv('schedule.csv', index=False)