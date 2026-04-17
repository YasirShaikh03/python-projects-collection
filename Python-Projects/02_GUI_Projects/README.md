# 🖥️ 02 — GUI Projects

Desktop GUI applications built with **Tkinter**.

## Scripts

| File | Description |
|------|-------------|
| `digital_clock.py` | Real-time HH:MM:SS digital clock |
| `analog_clock.py` | Animated analog clock using Canvas and math |
| `gui_calendar.py` | Interactive calendar with date selection |
| `alarm_clock.py` | Set alarm time — plays WAV sound on trigger |
| `notification.py` | Desktop pop-up notification every hour |

## Run

```bash
python digital_clock.py
python analog_clock.py
```

## Dependencies

```bash
pip install tkcalendar plyer playsound
```

## Notes

- `alarm_clock.py` — update the `.wav` file path to your local alarm sound file.
- `notification.py` — runs in an infinite loop; press `Ctrl+C` to stop.
