import customtkinter as ctk
from tkinter import messagebox, filedialog
from cryptosteganography import CryptoSteganography
import os

class SteganographyApplication:
    def __init__(self, window):
        self.window = window
        self.window.title("Image Steganography")
        self.window.geometry("500x350")

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.steganography = None

        self.label_password = ctk.CTkLabel(window, text="Password:", font=("Helvetica", 16))
        self.label_password.pack(pady=10)

        self.entry_password = ctk.CTkEntry(window, show="*", width=250)
        self.entry_password.pack(pady=5)

        self.btn_select_image = ctk.CTkButton(window, text="Select Image", command=self.select_image, width=200)
        self.btn_select_image.pack(pady=10)

        self.btn_select_text = ctk.CTkButton(window, text="Select Text File", command=self.select_text, width=200)
        self.btn_select_text.pack(pady=10)

        self.btn_embed = ctk.CTkButton(window, text="Embed Text into Image", command=self.embed_text, width=200)
        self.btn_embed.pack(pady=10)

        self.btn_extract = ctk.CTkButton(window, text="Extract Text from Image", command=self.extract_text, width=200)
        self.btn_extract.pack(pady=10)

        self.watermark_label = ctk.CTkLabel(window, text="~ Imaduddin Qazi  ", font=("Helvetica", 10, "italic"))
        self.watermark_label.pack(side="bottom", pady=2, anchor="se")

        self.image_path = None
        self.text_path = None

    def select_image(self):
        self.image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("PNG Files", "*.png")])
        if self.image_path:
            messagebox.showinfo("Selected Image", f"Selected Image: {os.path.basename(self.image_path)}")

    def select_text(self):
        self.text_path = filedialog.askopenfilename(title="Select Text File", filetypes=[("Text files", "*.txt")])
        if self.text_path:
            messagebox.showinfo("Selected Text File", f"Selected Text File: {os.path.basename(self.text_path)}")

    def embed_text(self):
        if not self.image_path:
            messagebox.showwarning("Input Missing", "Please Select an Image")
            return
        if not self.text_path:
            messagebox.showwarning("Input Missing", "Please Select a Text File")
            return
        if not self.entry_password.get():
            messagebox.showwarning("Input Missing", "Please Enter a Password")
            return
            
        password = self.entry_password.get()
        self.steganography = CryptoSteganography(password)

        with open(self.text_path, "r") as file:
            secret_message = file.read()
            
        output_image_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                         filetypes=[("PNG files", "*.png")],
                                                         title="Save as")

        if output_image_path:
            self.steganography.hide(self.image_path, output_image_path, secret_message)
            messagebox.showinfo("Success", f"Text Embedded into {os.path.basename(output_image_path)}")

    def extract_text(self):
        if not self.image_path:
            messagebox.showwarning("Input Missing", "Please Select an Image")
            return
        if not self.entry_password.get():
            messagebox.showwarning("Input Missing", "Please Enter the Password")
            return

        password = self.entry_password.get()
        self.steganography = CryptoSteganography(password)

        try:
            secret_message = self.steganography.retrieve(self.image_path)
        
            if secret_message:
                output_text_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                                filetypes=[("Text files", "*.txt")],
                                                                title="Save extracted text as")

                if output_text_path:
                    with open(output_text_path, "w") as file:
                        file.write(secret_message)
                    messagebox.showinfo("Success", f"Text extracted and saved as {os.path.basename(output_text_path)} successfully!")
            else:
                messagebox.showerror("Error", "Failed to extract text. No valid data found or incorrect password")

        except ValueError:
            messagebox.showerror("Error", "Wrong password entered.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to extract text: {e}")

if __name__ == "__main__":
    window = ctk.CTk()
    application = SteganographyApplication(window)
    window.mainloop()