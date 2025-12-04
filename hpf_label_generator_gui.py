import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
import os
import math

class HPFLabelGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("HPF Label Generator")
        self.root.geometry("600x700")
        
        # Default values
        self.defaults = {
            'lens_name': "Makro_symmar_180HM",
            'lens_efl_mm': 179.9,
            'focusing_ring_extension_mm_per_deg': 4/45,
            'focusing_ring_max_angle': 165,
            'hpf_ring_diameter_mm': 86.7,
            'hpf_ring_width_mm': 9.5,
            'text_len': 4,
            'output_dpi': 300,
            'dash_length_mm': 1.0,
            'dash_width_mm': 0.5,
            'fontPath': "./Square721 Cn BT Bold.ttf",
            'show_efl': True,
            'save_file_path': "./"
        }
        
        # Create a scrollable frame
        canvas = tk.Canvas(root)
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Store widget references
        self.entries = {}
        
        # Create input fields
        row = 0
        
        # Lens Name
        ttk.Label(scrollable_frame, text="Lens Name:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.entries['lens_name'] = ttk.Entry(scrollable_frame, width=40)
        self.entries['lens_name'].insert(0, self.defaults['lens_name'])
        self.entries['lens_name'].grid(row=row, column=1, padx=10, pady=5)
        row += 1
        
        # Lens EFL (mm)
        ttk.Label(scrollable_frame, text="Lens EFL (mm):").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.entries['lens_efl_mm'] = ttk.Entry(scrollable_frame, width=40)
        self.entries['lens_efl_mm'].insert(0, str(self.defaults['lens_efl_mm']))
        self.entries['lens_efl_mm'].grid(row=row, column=1, padx=10, pady=5)
        row += 1
        
        # Focusing Ring Extension (mm/deg)
        ttk.Label(scrollable_frame, text="Focusing Ring Extension (mm/deg):").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.entries['focusing_ring_extension_mm_per_deg'] = ttk.Entry(scrollable_frame, width=40)
        self.entries['focusing_ring_extension_mm_per_deg'].insert(0, str(self.defaults['focusing_ring_extension_mm_per_deg']))
        self.entries['focusing_ring_extension_mm_per_deg'].grid(row=row, column=1, padx=10, pady=5)
        row += 1
        
        # Focusing Ring Max Angle
        ttk.Label(scrollable_frame, text="Focusing Ring Max Angle:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.entries['focusing_ring_max_angle'] = ttk.Entry(scrollable_frame, width=40)
        self.entries['focusing_ring_max_angle'].insert(0, str(self.defaults['focusing_ring_max_angle']))
        self.entries['focusing_ring_max_angle'].grid(row=row, column=1, padx=10, pady=5)
        row += 1
        
        # HPF Ring Diameter (mm)
        ttk.Label(scrollable_frame, text="HPF Ring Diameter (mm):").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.entries['hpf_ring_diameter_mm'] = ttk.Entry(scrollable_frame, width=40)
        self.entries['hpf_ring_diameter_mm'].insert(0, str(self.defaults['hpf_ring_diameter_mm']))
        self.entries['hpf_ring_diameter_mm'].grid(row=row, column=1, padx=10, pady=5)
        row += 1
        
        # HPF Ring Width (mm)
        ttk.Label(scrollable_frame, text="HPF Ring Width (mm):").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.entries['hpf_ring_width_mm'] = ttk.Entry(scrollable_frame, width=40)
        self.entries['hpf_ring_width_mm'].insert(0, str(self.defaults['hpf_ring_width_mm']))
        self.entries['hpf_ring_width_mm'].grid(row=row, column=1, padx=10, pady=5)
        row += 1
        
        # Text Length
        ttk.Label(scrollable_frame, text="Text Length:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.entries['text_len'] = ttk.Entry(scrollable_frame, width=40)
        self.entries['text_len'].insert(0, str(self.defaults['text_len']))
        self.entries['text_len'].grid(row=row, column=1, padx=10, pady=5)
        row += 1
        
        # Output DPI
        ttk.Label(scrollable_frame, text="Output DPI:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.entries['output_dpi'] = ttk.Entry(scrollable_frame, width=40)
        self.entries['output_dpi'].insert(0, str(self.defaults['output_dpi']))
        self.entries['output_dpi'].grid(row=row, column=1, padx=10, pady=5)
        row += 1
        
        # Dash Length (mm)
        ttk.Label(scrollable_frame, text="Dash Length (mm):").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.entries['dash_length_mm'] = ttk.Entry(scrollable_frame, width=40)
        self.entries['dash_length_mm'].insert(0, str(self.defaults['dash_length_mm']))
        self.entries['dash_length_mm'].grid(row=row, column=1, padx=10, pady=5)
        row += 1
        
        # Dash Width (mm)
        ttk.Label(scrollable_frame, text="Dash Width (mm):").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.entries['dash_width_mm'] = ttk.Entry(scrollable_frame, width=40)
        self.entries['dash_width_mm'].insert(0, str(self.defaults['dash_width_mm']))
        self.entries['dash_width_mm'].grid(row=row, column=1, padx=10, pady=5)
        row += 1
        
        # Font Path
        ttk.Label(scrollable_frame, text="Font Path:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        font_frame = ttk.Frame(scrollable_frame)
        font_frame.grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        self.entries['fontPath'] = ttk.Entry(font_frame, width=30)
        self.entries['fontPath'].insert(0, self.defaults['fontPath'])
        self.entries['fontPath'].pack(side="left", fill="x", expand=True)
        ttk.Button(font_frame, text="Browse...", command=self.browse_font).pack(side="left", padx=5)
        row += 1
        
        # Show EFL
        ttk.Label(scrollable_frame, text="Show EFL:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        self.show_efl_var = tk.BooleanVar(value=self.defaults['show_efl'])
        ttk.Checkbutton(scrollable_frame, variable=self.show_efl_var).grid(row=row, column=1, sticky="w", padx=10, pady=5)
        row += 1
        
        # Save File Path
        ttk.Label(scrollable_frame, text="Save File Path:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        path_frame = ttk.Frame(scrollable_frame)
        path_frame.grid(row=row, column=1, padx=10, pady=5, sticky="ew")
        self.entries['save_file_path'] = ttk.Entry(path_frame, width=30)
        self.entries['save_file_path'].insert(0, self.defaults['save_file_path'])
        self.entries['save_file_path'].pack(side="left", fill="x", expand=True)
        ttk.Button(path_frame, text="Browse...", command=self.browse_save_path).pack(side="left", padx=5)
        row += 1
        
        # Separator
        ttk.Separator(scrollable_frame, orient="horizontal").grid(row=row, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        row += 1
        
        # Buttons
        button_frame = ttk.Frame(scrollable_frame)
        button_frame.grid(row=row, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Generate", command=self.generate).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Reset", command=self.reset_values).pack(side="left", padx=5)
        
    def browse_font(self):
        filetypes = [("Font files", "*.ttf *.otf"), ("All files", "*.*")]
        filename = filedialog.askopenfilename(filetypes=filetypes)
        if filename:
            self.entries['fontPath'].delete(0, tk.END)
            self.entries['fontPath'].insert(0, filename)
    
    def browse_save_path(self):
        dirname = filedialog.askdirectory()
        if dirname:
            self.entries['save_file_path'].delete(0, tk.END)
            self.entries['save_file_path'].insert(0, dirname + "/")
    
    def reset_values(self):
        for key, entry in self.entries.items():
            entry.delete(0, tk.END)
            entry.insert(0, str(self.defaults[key]))
        self.show_efl_var.set(self.defaults['show_efl'])
    
    def get_values(self):
        try:
            values = {
                'lens_name': self.entries['lens_name'].get(),
                'lens_efl_mm': float(self.entries['lens_efl_mm'].get()),
                'focusing_ring_extension_mm_per_deg': float(self.entries['focusing_ring_extension_mm_per_deg'].get()),
                'focusing_ring_max_angle': int(self.entries['focusing_ring_max_angle'].get()),
                'hpf_ring_diameter_mm': float(self.entries['hpf_ring_diameter_mm'].get()),
                'hpf_ring_width_mm': float(self.entries['hpf_ring_width_mm'].get()),
                'text_len': int(self.entries['text_len'].get()),
                'output_dpi': int(self.entries['output_dpi'].get()),
                'dash_length_mm': float(self.entries['dash_length_mm'].get()),
                'dash_width_mm': float(self.entries['dash_width_mm'].get()),
                'fontPath': self.entries['fontPath'].get(),
                'show_efl': self.show_efl_var.get(),
                'save_file_path': self.entries['save_file_path'].get()
            }
            return values
        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")
            return None
    
    def generate(self):
        values = self.get_values()
        if values is None:
            return
        
        try:
            # Extract values
            lens_name = values['lens_name']
            lens_efl_mm = values['lens_efl_mm']
            focusing_ring_extension_mm_per_deg = values['focusing_ring_extension_mm_per_deg']
            focusing_ring_max_angle = values['focusing_ring_max_angle']
            hpf_ring_diameter_mm = values['hpf_ring_diameter_mm']
            hpf_ring_width_mm = values['hpf_ring_width_mm']
            text_len = values['text_len']
            output_dpi = values['output_dpi']
            dash_length_mm = values['dash_length_mm']
            dash_width_mm = values['dash_width_mm']
            fontPath = values['fontPath']
            show_efl = values['show_efl']
            save_file_path = values['save_file_path']
            
            # System variables
            output_angle = [1,2,3,4]+[(i+1)*5 for i in range(focusing_ring_max_angle//5)]
            
            image_size_mm = hpf_ring_diameter_mm * 3.1416
            mm2inch_ratio = 25.4
            image_h_pix = int(image_size_mm / mm2inch_ratio * output_dpi)
            image_w_pix = int(hpf_ring_width_mm / mm2inch_ratio * output_dpi)
            dash_len_pix = int(dash_length_mm / mm2inch_ratio * output_dpi)
            dash_width_pix = int(dash_width_mm / mm2inch_ratio * output_dpi)
            canvas_sizeX, canvas_sizeY = image_w_pix, image_h_pix
            
            project_name = lens_name + "_" + str(lens_efl_mm) + "mm" + "_M65_HPF_Sticker_" \
                + str(image_w_pix) + "x" + str(image_h_pix) + "mm_" + str(output_dpi) + "dpi"
            
            # Check if font file exists
            if not os.path.exists(fontPath):
                messagebox.showerror("Error", f"Font file not found: {fontPath}")
                return
            
            fnt = ImageFont.truetype(fontPath, image_w_pix//3)
            
            # Create canvas
            img = Image.new('L', (canvas_sizeX, canvas_sizeY), color=0)
            draw = ImageDraw.Draw(img)
            
            text_distance = hpf_ring_diameter_mm * output_dpi * 3.1416 / 360 / mm2inch_ratio
            
            dash_start_y = image_w_pix / 6 + dash_width_pix // 2
            draw.line([(0, text_distance + dash_start_y), (dash_len_pix, text_distance + dash_start_y)], fill=255, width=dash_width_pix)
            draw.text((dash_len_pix + 10, text_distance), "INF", font=fnt, fill=255)
            
            for i in output_angle:
                extension = focusing_ring_extension_mm_per_deg * i
                v = lens_efl_mm + extension
                u = 1 / (1 / lens_efl_mm - 1 / v) / 1000
                if u > 999:
                    messagebox.showwarning("Warning", "Please change your settings - u value exceeds 999")
                
                hpf_sign = str(u + v / 1000)
                
                if "." in hpf_sign and u < 100:
                    hpf_sign = hpf_sign[:text_len + 1]
                elif u >= 100 and "." in hpf_sign:
                    hpf_sign = hpf_sign[:text_len + 1]
                else:
                    hpf_sign = hpf_sign[:text_len]
                
                if i < 5:
                    draw.line([(0, text_distance * (i) * 5 + 10 + dash_start_y), (dash_len_pix, text_distance * (i) * 5 + 10 + dash_start_y)], fill=255, width=dash_width_pix)
                    draw.text((dash_len_pix + 10, text_distance * (i) * 5 + 10), hpf_sign, font=fnt, fill=255)
                else:
                    draw.line([(0, text_distance * (i + 20) + 10 + dash_start_y), (dash_len_pix, text_distance * (i + 20) + 10 + dash_start_y)], fill=255, width=dash_width_pix)
                    draw.text((dash_len_pix + 10, text_distance * (i + 20) + 10), hpf_sign, font=fnt, fill=255)
            
            if show_efl:
                draw.text((10, text_distance * (output_angle[-1] + 30) + 10), "E.F.L.", font=fnt, fill=255)
                draw.text((10, text_distance * (output_angle[-1] + 35) + 10), str(lens_efl_mm), font=fnt, fill=255)
                draw.text((10, text_distance * (output_angle[-1] + 39) + 10), "   m/m", font=fnt, fill=255)
            
            # Save image
            save_path = save_file_path + project_name + "_raw_PNG.png"
            img.save(save_path, dpi=(output_dpi, output_dpi))
            
            messagebox.showinfo("Success", f"Image saved successfully to:\n{save_path}")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during generation:\n{str(e)}")

def main():
    root = tk.Tk()
    gui = HPFLabelGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
