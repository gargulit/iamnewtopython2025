import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz # For timezone handling

# List of timezones with country names
# This is a subset for simplicity, you can expand this list
TIMEZONES_DATA = [
    {'country': 'United States (New York)', 'timezone': 'America/New_York', 'code': 'US'},
    {'country': 'United States (Los Angeles)', 'timezone': 'America/Los_Angeles', 'code': 'US'},
    {'country': 'United Kingdom (London)', 'timezone': 'Europe/London', 'code': 'GB'},
    {'country': 'France (Paris)', 'timezone': 'Europe/Paris', 'code': 'FR'},
    {'country': 'Germany (Berlin)', 'timezone': 'Europe/Berlin', 'code': 'DE'},
    {'country': 'Japan (Tokyo)', 'timezone': 'Asia/Tokyo', 'code': 'JP'},
    {'country': 'China (Shanghai)', 'timezone': 'Asia/Shanghai', 'code': 'CN'},
    {'country': 'India (Kolkata)', 'timezone': 'Asia/Kolkata', 'code': 'IN'},
    {'country': 'Australia (Sydney)', 'timezone': 'Australia/Sydney', 'code': 'AU'},
    {'country': 'Canada (Toronto)', 'timezone': 'America/Toronto', 'code': 'CA'},
    {'country': 'Brazil (São Paulo)', 'timezone': 'America/Sao_Paulo', 'code': 'BR'},
    {'country': 'Russia (Moscow)', 'timezone': 'Europe/Moscow', 'code': 'RU'},
    {'country': 'South Korea (Seoul)', 'timezone': 'Asia/Seoul', 'code': 'KR'},
    {'country': 'Singapore', 'timezone': 'Asia/Singapore', 'code': 'SG'},
    {'country': 'UAE (Dubai)', 'timezone': 'Asia/Dubai', 'code': 'AE'},
    {'country': 'South Africa (Johannesburg)', 'timezone': 'Africa/Johannesburg', 'code': 'ZA'},
    {'country': 'Mexico (Mexico City)', 'timezone': 'America/Mexico_City', 'code': 'MX'},
    {'country': 'Argentina (Buenos Aires)', 'timezone': 'America/Argentina/Buenos_Aires', 'code': 'AR'},
    {'country': 'Italy (Rome)', 'timezone': 'Europe/Rome', 'code': 'IT'},
    {'country': 'Spain (Madrid)', 'timezone': 'Europe/Madrid', 'code': 'ES'}
]

class WorldClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("World Clock")
        self.root.geometry("500x350") # Adjusted window size
        self.root.configure(bg="#f0f0f0")

        # Style
        style = ttk.Style()
        style.configure("TLabel", padding=6, font=("Helvetica", 12), background="#f0f0f0")
        style.configure("Title.TLabel", font=("Helvetica", 16, "bold"), background="#f0f0f0")
        style.configure("Time.TLabel", font=("Helvetica", 36, "bold"), foreground="#333", background="#f0f0f0")
        style.configure("Date.TLabel", font=("Helvetica", 14), foreground="#555", background="#f0f0f0")
        style.configure("TCombobox", padding=6, font=("Helvetica", 12))
        style.map("TCombobox", fieldbackground=[("readonly", "white")])


        # --- UI Elements ---
        # Title
        self.title_label = ttk.Label(root, text="World Clock", style="Title.TLabel")
        self.title_label.pack(pady=(20,10))

        # Frame for dropdown and label
        self.selection_frame = ttk.Frame(root, style="TFrame", padding=(10,0))
        self.selection_frame.pack(pady=5)
        
        self.dropdown_label = ttk.Label(self.selection_frame, text="Select Country:")
        self.dropdown_label.pack(side=tk.LEFT, padx=(0, 5))

        self.country_names = [tz['country'] for tz in TIMEZONES_DATA]
        self.selected_country_var = tk.StringVar()
        self.country_dropdown = ttk.Combobox(
            self.selection_frame,
            textvariable=self.selected_country_var,
            values=self.country_names,
            state="readonly", # Makes it so user can't type, only select
            width=30,
            font=("Helvetica", 11)
        )
        self.country_dropdown.pack(side=tk.LEFT)
        self.country_dropdown.bind("<<ComboboxSelected>>", self.update_time_display)
        if self.country_names:
            self.country_dropdown.current(0) # Select the first country by default

        # Time display
        self.time_label = ttk.Label(root, text="", style="Time.TLabel")
        self.time_label.pack(pady=10)

        # Date display
        self.date_label = ttk.Label(root, text="", style="Date.TLabel")
        self.date_label.pack(pady=5)
        
        # Info label for timezone
        self.timezone_info_label = ttk.Label(root, text="", font=("Helvetica", 10, "italic"), foreground="#777", background="#f0f0f0")
        self.timezone_info_label.pack(pady=(5, 20))


        # Initial time update
        self.update_time_display()
        self.schedule_time_update()

    def get_timezone_by_country_name(self, country_name):
        for tz_data in TIMEZONES_DATA:
            if tz_data['country'] == country_name:
                return tz_data['timezone']
        return None

    def update_time_display(self, event=None):
        selected_country_name = self.selected_country_var.get()
        if not selected_country_name:
            self.time_label.config(text="--:--:--")
            self.date_label.config(text="Select a country")
            self.timezone_info_label.config(text="")
            return

        timezone_str = self.get_timezone_by_country_name(selected_country_name)

        if timezone_str:
            try:
                target_tz = pytz.timezone(timezone_str)
                current_time = datetime.now(target_tz)
                
                time_string = current_time.strftime("%H:%M:%S")
                date_string = current_time.strftime("%A, %B %d, %Y")
                
                self.time_label.config(text=time_string)
                self.date_label.config(text=date_string)
                self.timezone_info_label.config(text=f"Timezone: {timezone_str.replace('_', ' ')}")
            except pytz.exceptions.UnknownTimeZoneError:
                self.time_label.config(text="Error")
                self.date_label.config(text="Invalid Timezone")
                self.timezone_info_label.config(text=f"Error with: {timezone_str}")
            except Exception as e:
                self.time_label.config(text="Error")
                self.date_label.config(text=f"An error occurred: {str(e)[:30]}") # Show brief error
                self.timezone_info_label.config(text="")
        else:
            self.time_label.config(text="--:--:--")
            self.date_label.config(text="Timezone not found")
            self.timezone_info_label.config(text="")


    def schedule_time_update(self):
        self.update_time_display()
        # Schedule the next update in 1000 ms (1 second)
        self.root.after(1000, self.schedule_time_update)

if __name__ == "__main__":
    # Before starting Tkinter, check for pytz
    try:
        import pytz
    except ImportError:
        print("--------------------------------------------------------------------")
        print("ERROR: The 'pytz' library is not installed.")
        print("Please install it by running: pip install pytz")
        print("Or, if you use pip3: pip3 install pytz")
        print("--------------------------------------------------------------------")
        exit()

    root = tk.Tk()
    app = WorldClockApp(root)
    root.mainloop()