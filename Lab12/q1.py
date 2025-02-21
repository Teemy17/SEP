# from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QDateEdit, QListWidget, QLabel
# from PySide6.QtCore import Qt
# from datetime import date as Date
# import sys

# class BookingSystem(object):
#     def __init__(self):
#         self.observers = []
#         self.bookings = {}
    
#     def add_observer(self, o):
#         self.observers.append(o)
    
#     def addBooking(self, date, booking):
#         if date in self.bookings:
#             self.bookings[date].append(booking)
#         else:
#             self.bookings[date] = [booking]

#     def notify_observers(self, data):
#         for o in self.observers:
#             o.update(data)
        
#     def getBookings(self, date):
#         bookings = []
#         for k, v in self.bookings.items():
#             if k == date:
#                 bookings.append((k, v))

#         self.notify_observers(bookings)
#         return bookings

#     def display(self, date):
#         self.getBookings(date)

# class BookingsObserver(object):
#     def update(self, data):
#         pass

# class StaffUi(BookingsObserver):
#     def __init__(self, s, name, ui):
#         self.name = name
#         self.system = s
#         self.ui = ui

#     def update(self, bookings):
#         self.ui.update_booking_list(bookings)

#     def submit(self, date):
#         self.system.display(date)

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         # Create the booking system
#         self.system = BookingSystem()
#         self.ui = StaffUi(self.system, "StaffUI", self)

#         # Initialize the UI components
#         self.setWindowTitle("Booking System")

#         # Layout
#         self.layout = QVBoxLayout()
        
#         # Date picker
#         self.date_picker = QDateEdit()
#         self.date_picker.setDate(Date(2011, 9, 1))  # Default date
#         self.layout.addWidget(QLabel("Select Date:"))
#         self.layout.addWidget(self.date_picker)

#         # List widget to show bookings
#         self.booking_list = QListWidget()
#         self.layout.addWidget(QLabel("Bookings for Selected Date:"))
#         self.layout.addWidget(self.booking_list)

#         # Submit button
#         self.submit_button = QPushButton("Show Bookings")
#         self.submit_button.clicked.connect(self.on_submit)
#         self.layout.addWidget(self.submit_button)

#         # Set layout
#         self.setLayout(self.layout)

#         # Adding some bookings to the system
#         self.system.addBooking(Date(2011, 9, 1), "Booking #1")
#         self.system.addBooking(Date(2011, 9, 1), "Booking #2")
#         self.system.addBooking(Date(2011, 9, 2), "Booking #3")
#         self.system.addBooking(Date(2011, 9, 3), "Booking #4")
#         self.system.addBooking(Date(2011, 9, 3), "Booking #5")

#         # Add the observer (this UI)
#         self.system.add_observer(self.ui)

#     def on_submit(self):
#         # Get the selected date
#         selected_date = self.date_picker.date()
#         py_date = Date(selected_date.year(), selected_date.month(), selected_date.day())
#         self.ui.submit(py_date)


#     def update_booking_list(self, bookings):
#         # Clear the current list
#         self.booking_list.clear()

#         # Add new bookings
#         for date, items in bookings:
#             for item in items:
#                 self.booking_list.addItem(f"{date}: {item}")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     window = MainWindow()
#     window.show()

#     sys.exit(app.exec())

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QHBoxLayout, QDialog
from PySide6.QtCore import Qt
from datetime import date as Date
import sys

class BookingSystem(object):
    def __init__(self):
        self.observers = []
        self.bookings = {}
    
    def add_observer(self, o):
        self.observers.append(o)
    
    def addBooking(self, date, booking):
        if date in self.bookings:
            self.bookings[date].append(booking)
        else:
            self.bookings[date] = [booking]

    def notify_observers(self, data):
        for o in self.observers:
            o.update(data)
        
    def getBookings(self, date):
        bookings = []
        for k, v in self.bookings.items():
            if k == date:
                bookings.append((k, v))

        self.notify_observers(bookings)
        return bookings

    def display(self, date):
        self.getBookings(date)

class BookingsObserver(object):
    def update(self, data):
        pass

class StaffUi(BookingsObserver):
    def __init__(self, s, name, ui):
        self.name = name
        self.system = s
        self.ui = ui

    def update(self, bookings):
        self.ui.update_booking_list(bookings)

    def submit(self, date):
        self.system.display(date)

class DateInputWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Enter Date")

        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel("Enter Day:"))
        self.day_input = QLineEdit()
        self.layout.addWidget(self.day_input)

        self.layout.addWidget(QLabel("Enter Month:"))
        self.month_input = QLineEdit()
        self.layout.addWidget(self.month_input)

        self.layout.addWidget(QLabel("Enter Year:"))
        self.year_input = QLineEdit()
        self.layout.addWidget(self.year_input)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.on_submit)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def on_submit(self):
        # Get the values from the inputs
        try:
            day = int(self.day_input.text())
            month = int(self.month_input.text())
            year = int(self.year_input.text())
            selected_date = Date(year, month, day)
            self.accept()  # Close the dialog
            self.parent().on_date_selected(selected_date)  # Notify parent (MainWindow)
        except ValueError:
            # Show error message if any of the inputs is invalid
            print("Invalid date input. Please enter valid numbers.")
            return

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create the booking system
        self.system = BookingSystem()
        self.ui = StaffUi(self.system, "StaffUI", self)

        # Initialize the UI components
        self.setWindowTitle("Booking System")

        # Layout
        self.layout = QVBoxLayout()

        # Label
        self.layout.addWidget(QLabel("Bookings System"))

        # Booking list to show bookings
        self.booking_list = QLabel("No bookings selected.")
        self.layout.addWidget(self.booking_list)

        # Select Booking button
        self.select_booking_button = QPushButton("Select Booking")
        self.select_booking_button.clicked.connect(self.open_date_input_window)
        self.layout.addWidget(self.select_booking_button)

        # Set layout
        self.setLayout(self.layout)

        # Adding some bookings to the system
        self.system.addBooking(Date(2011, 9, 1), "Booking #1")
        self.system.addBooking(Date(2011, 9, 1), "Booking #2")
        self.system.addBooking(Date(2011, 9, 2), "Booking #3")
        self.system.addBooking(Date(2011, 9, 3), "Booking #4")
        self.system.addBooking(Date(2011, 9, 3), "Booking #5")

        # Add the observer (this UI)
        self.system.add_observer(self.ui)

    def open_date_input_window(self):
        # Open the date input dialog
        date_input_window = DateInputWindow(self)
        date_input_window.exec()  # Show as modal window

    def on_date_selected(self, selected_date):
        # Get the selected date and show the bookings for that date
        self.ui.submit(selected_date)

    def update_booking_list(self, bookings):
        # Update the list of bookings
        booking_text = ""
        for date, items in bookings:
            for item in items:
                booking_text += f"{date}: {item}\n"
        self.booking_list.setText(booking_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
