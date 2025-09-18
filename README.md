Kenya Premier League 2025/2026 Fixtures → CSV & ICS

This project converts the Kenya Premier League 2025/2026 Fixtures into two useful formats:

1. CSV (tabular format, easy to view and manage)
2. ICS (calendar format, importable into Google Calendar, Outlook, Apple Calendar, etc.)

📂 Project Structure
├── create_csv.py      # Parse raw fixtures text into CSV
├── create_ics.py      # Convert CSV into ICS calendar
├── fixtures.csv       # Example CSV (generated)
├── fixtures.ics       # Example ICS (generated)
├── README.md          # Documentation

⚡ Features
1. Convert raw fixtures into a clean CSV file
2. Convert CSV into an ICS calendar file
3. Each event includes:
◯ Match title (Home vs Away)
◯ Date & Kickoff Time
◯ Location (Stadium, City)
◯ Automatic 2-hour match duration

🚀 Usage
1. Clone the repository
2. Generate Fixtures CSV: Run the script to create fixtures.csv from the raw fixture text:
python create_csv.py

3. Generate Calendar File (ICS): Convert the CSV into an ICS calendar file:
python create_ics.py


This creates a fixtures.ics file.

📅 How to Import fixtures.ics into Google Calendar
1. Create a New Calendar (Recommended)
2. Open Google Calendar
3. On the left, click “Other calendars” → “+” → Create new calendar
4. Give it a name, e.g. Kenya Premier League 2025/2026
5. Import the Fixtures
◯ Go to ⚙ Settings → Import & Export
◯ Select fixtures.ics
◯ Under Add to calendar, choose the new calendar you just created
◯ Click Import

Now all fixtures will appear in that calendar, keeping them separate from your personal events.

📊 Example

CSV Row:

Date	Day	Time	Home Team	Away Team	Stadium	City
20/9/25	SATURDAY	4PM	AFC Leopards	Sofapaka	Nyayo Stadium	Nairobi

ICS Event:

BEGIN:VEVENT
SUMMARY:AFC Leopards vs Sofapaka
DTSTART:20250920T160000
DTEND:20250920T180000
LOCATION:Nyayo Stadium, Nairobi
END:VEVENT

📌 Project Background
Fans requested a way to integrate official Kenya Premier League Fixtures into Google Calendar.
The fixtures were initially shared as a PDF document, which wasn’t formatted well.
The PDF was converted to Excel using ILovePDF.com
After manual cleaning, the fixtures were processed with two scripts:

create_csv.py → generates a CSV file
create_ics.py → converts the CSV into a Google Calendar compatible ICS file

Once imported into Google Calendar, each fixture appears as a 2-hour match event.

🔄 Updating Events After Matches
We also plan to update the events in the calendar with extra details after each match, such as:
Goal scorers
Match lineups
Key highlights

This will make the fixtures calendar both a schedule and a results archive.