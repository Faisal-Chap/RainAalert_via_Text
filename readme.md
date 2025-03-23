# Weather Forecast Notification Script

## Overview
This Python script fetches weather forecast data from the OpenWeather API and sends a rain notification via SMS using the Twilio API. It predicts rain timings and notifies the user accordingly.

## Features
- Fetches hourly weather forecast data.
- Identifies rain and no-rain periods.
- Constructs a detailed message about the forecast.
- Sends an SMS alert via Twilio.

## Requirements
Ensure you have the following dependencies installed:

```sh
pip install requests twilio
```

## Configuration
Before running the script, update the following placeholders with your credentials:

1. **Twilio Credentials**
   - `account_sid`: Your Twilio Account SID.
   - `auth_token`: Your Twilio Auth Token.
   - `from_`: Your Twilio phone number.
   - `to`: Your recipient phone number.

2. **OpenWeather API Credentials**
   - `APPID`: Your OpenWeather API key.

3. **Location Coordinates**
   - Update `lat` and `lon` to your desired location.

## Usage
Run the script using Python:

```sh
python weather_forecast.py
```

## Explanation
- The script fetches the 3-hour interval weather forecast from OpenWeather API.
- It extracts the rain prediction timings.
- It generates a formatted SMS message containing rain and no-rain periods.
- The Twilio API sends the forecast as an SMS to the specified recipient.

## Example SMS Output
```
Asalam-U-Alikum Faisal
Here is the Cloud Report for Today
Following the 3 HOURLY Rain Forecast,
12:00 to 15:00    Rain
15:00 to 18:00    No Rain
There is Rain Later in the Day
```

## Notes
- The script checks for weather conditions using weather condition codes (e.g., `500-599` for rain).
- Make sure your Twilio account has enough credits to send messages.
- OpenWeather API has free-tier limits; ensure you are within the allowed API call limits.

## Future Enhancements
- Add support for multiple recipients.
- Implement real-time updates instead of 3-hour intervals.
- Integrate push notifications or email alerts.

