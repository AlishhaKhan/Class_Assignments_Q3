class Logger:
    def __init__(self):
        print("📥 Logger Initialized (Object Created)")

    def __del__(self):
        print("📤 Logger Terminated (Object Destroyed)")

# Create object
logger1 = Logger()

# Optional: Delete manually to see destructor instantly
del logger1
