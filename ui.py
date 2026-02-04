import tkinter as tk

class FloatingWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AI Code Helper")
        self.root.geometry("600x400+200+200")
        self.root.attributes("-topmost", True)

        self.text = tk.Text(
            self.root,
            wrap="word",
            padx=10,
            pady=10
        )
        self.text.pack(expand=True, fill="both")

        self.show_message(
            "AI Code Helper is running.\n\n"
            "1. Copy code from any IDE\n"
            "2. Press Ctrl + Shift + A\n"
            "3. Review suggestions here"
        )

    def show_message(self, content: str):
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, content)
        self.root.update_idletasks()

    def run(self):
        self.root.mainloop()
