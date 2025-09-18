# Kenya Premier League 2025/2026 Fixtures → CSV & ICS

This project converts the Kenya Premier League 2025/2026 Fixtures into two useful formats:

1. CSV – tabular format, easy to view and manage
2. ICS – calendar format, importable into Google Calendar, Outlook, Apple Calendar, etc.

---

## 📂 Project Structure

```
├── create_csv.py      # Parse raw fixtures text into CSV
├── create_ics.py      # Convert CSV into ICS calendar
├── fixtures.csv       # Example CSV (generated)
├── fixtures.ics       # Example ICS (generated)
├── README.md          # Documentation
```

---

## ⚡ Features

* Convert raw fixtures into a clean CSV file
* Convert the CSV into an ICS calendar file
* Each calendar event includes: <br>
  ◯ Match title (Home vs Away) <br>
  ◯ Date & Kickoff Time <br>
  ◯ Location (Stadium, City) <br>
  ◯ Automatic 2-hour match duration <br>

---

## 🚀 Usage

### 1. Clone the Repository

```bash
git clone https://github.com/raulnyabola/kpl-fixtures-2025-2026
cd kpl-fixtures-2025-2026
```

### 2. Generate Fixtures CSV

Run the script to create fixtures.csv from the raw fixture text:

```bash
python create_csv.py
```

### 3. Generate Calendar File (ICS)

Convert the CSV into an ICS calendar file:

```bash
python create_ics.py
```

This creates a file called fixtures.ics.

---

## 📅 Importing `fixtures.ics` into Google Calendar

1. Create a New Calendar (Recommended):

   * Open Google Calendar
   * On the left, click “Other calendars” → “+” → Create new calendar
   * Give it a name, e.g. *Kenya Premier League 2025/2026*

2. Import the Fixtures:

   * Go to ⚙ Settings → Import & Export
   * Select fixtures.ics
   * Under *Add to calendar*, choose the new calendar you just created
   * Click Import

✅ Now all fixtures will appear in that calendar, keeping them separate from your personal events.

---

## 📊 Example

### CSV Row

```
Date        Day       Time   Home Team     Away Team   Stadium         City
20/9/25     SATURDAY  4PM    AFC Leopards  Sofapaka    Nyayo Stadium   Nairobi
```

### ICS Event

```
BEGIN:VEVENT
SUMMARY:AFC Leopards vs Sofapaka
DTSTART:20250920T160000
DTEND:20250920T180000
LOCATION:Nyayo Stadium, Nairobi
END:VEVENT
```

---

## 📌 Project Background

Fans requested a way to integrate the official Kenya Premier League Fixtures into Google Calendar.

* The fixtures were initially shared as a PDF document, which wasn’t well formatted.
* The PDF was converted to Excel using [ILovePDF.com] (https://www.ilovepdf.com).
* After manual cleaning, the fixtures were processed with two scripts:

  * `create_csv.py` → generates a CSV file
  * `create_ics.py` → converts the CSV into a Google Calendar compatible ICS file

Once imported into Google Calendar, each fixture appears as a 2-hour match event.

---

## 🔄 Updating Events After Matches

We also plan to update the events in the calendar with extra details after each match, such as:

* Goal scorers
* Match lineups
* Key highlights

This will make the fixtures calendar both a schedule and a results archive.
