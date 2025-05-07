class UserSession:
    def __init__(self):
        self.logged_in = True

    def logout(self):
        try:
            if not self.logged_in:
                print("User is already logged out.")
                return
            # Simulate logout process
            self.logged_in = False
            print("User logged out successfully.")
        except RuntimeError as e:
            print(f"Error: {e}")

# Example usage test
if __name__ == "__main__":
    session = UserSession()
    session.logout()  # Logs out successfully
    session.logout()  # Triggers an error

    

