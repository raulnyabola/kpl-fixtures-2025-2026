import csv
from datetime import datetime, timedelta

# Input CSV and output ICS file
csv_file = "fixtures.csv"
ics_file = "fixtures.ics"

# Function to convert date and time to ICS datetime format
def to_ics_datetime(date_str, time_str):
    # Normalize time string
    time_str = time_str.upper().replace(" ", "")
    hour = int(time_str[:-2])
    if "PM" in time_str and hour != 12:
        hour += 12
    if "AM" in time_str and hour == 12:
        hour = 0

    # Try parsing date in multiple formats
    for fmt in ("%d/%m/%y", "%d/%m/%Y"):
        try:
            dt = datetime.strptime(date_str, fmt)
            break
        except ValueError:
            continue
    else:
        raise ValueError(f"Date format not recognized: {date_str}")

    dt = dt.replace(hour=hour, minute=0, second=0)
    return dt.strftime("%Y%m%dT%H%M%S")

# Read CSV and create ICS events
events = []
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        start_dt = to_ics_datetime(row['Date'], row['Time'])
        end_dt = (datetime.strptime(start_dt, "%Y%m%dT%H%M%S") + timedelta(hours=2)).strftime("%Y%m%dT%H%M%S")
        summary = f"{row['Home']} vs {row['Away']}"
        location = f"{row['Stadium']}, {row['City']}"

        event = f"""BEGIN:VEVENT
SUMMARY:{summary}
DTSTART:{start_dt}
DTEND:{end_dt}
LOCATION:{location}
END:VEVENT"""
        events.append(event)

# Write ICS file
with open(ics_file, 'w', encoding='utf-8') as f:
    f.write("BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//SPORTPESA Fixtures//EN\n")
    for event in events:
        f.write(event + "\n")
    f.write("END:VCALENDAR")

print(f"ICS file '{ics_file}' created successfully!")
