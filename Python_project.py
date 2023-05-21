                                                                  #####COMPLETED CODE#####
                                                                   ###PYTHON PROJECT###
                                                                  #PERSONALISED HAIR CARE#

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser

root = tk.Tk()
root.title("Hair Quiz")
root.geometry("1920x1080")

root.config(bg="#d4d4ec")
bg_color = "#d4d4ec"

# Set up fonts
title_font = ("Helvetica", 20, "bold")
label_font = ("Helvetica", 12)
optionmenu_font = ("Helvetica", 6)

# Set up hair type options
hair_type_options = ["Select your hair type", "Straight", "Wavy", "Curly", "Coily"]
hair_type_var = tk.StringVar(root)
hair_type_var.set(hair_type_options[0])

# Set up hair texture options
hair_texture_options = ["Select your hair texture", "Fine", "Medium", "Coarse"]
hair_texture_var = tk.StringVar(root)
hair_texture_var.set(hair_texture_options[0])

# Set up scalp texture options
scalp_texture_options = ["Select your scalp texture", "Dry", "Normal", "Oily"]
scalp_texture_var = tk.StringVar(root)
scalp_texture_var.set(scalp_texture_options[0])

# Load images
images = {
    "title": ImageTk.PhotoImage(Image.open("heading.png")),
    "hair_type": ImageTk.PhotoImage(Image.open("hair-type.png")),
    "hair_texture": ImageTk.PhotoImage(Image.open("hair-texture .png")),
    "scalp_texture": ImageTk.PhotoImage(Image.open("Scalp-type.png"))
}

root.config(bg="#d4d4ec")
bg_color = "#d4d4ec"

# Set up fonts
title_font = ("Helvetica", 20, "bold")
label_font = ("Helvetica", 10)
optionmenu_font = ("Helvetica", 8)

# Set up hair type options
hair_type_options = ["Select your hair type", "Straight", "Wavy", "Curly", "Coily"]
hair_type_var = tk.StringVar(root)
hair_type_var.set(hair_type_options[0])

# Set up hair texture options
hair_texture_options = ["Select your hair texture", "Fine", "Medium", "Coarse"]
hair_texture_var = tk.StringVar(root)
hair_texture_var.set(hair_texture_options[0])

# Set up scalp texture options
scalp_texture_options = ["Select your scalp texture", "Dry", "Normal", "Oily"]
scalp_texture_var = tk.StringVar(root)
scalp_texture_var.set(scalp_texture_options[0])

# ///////////////////////////////////////////////////////////////////////
panel1 = Label(root, image=images["title"])
panel1.pack()

# Set up hair type option menu
panel2 = Label(root, image=images["hair_type"])
panel2.pack()
hair_type_label = tk.Label(root, text="Q1) What is your hair type?", font=label_font, bg=bg_color)
hair_type_label.pack()
hair_type_menu = ttk.OptionMenu(root, hair_type_var, *hair_type_options, style="TMenubutton")
hair_type_menu.pack()

# Set up hair texture option menu
panel3 = Label(root, image=images["hair_texture"])
panel3.pack()
hair_texture_label = tk.Label(root, text="Q2) What is the texture of your hair?", font=label_font, bg=bg_color)
hair_texture_label.pack()
hair_texture_menu = ttk.OptionMenu(root, hair_texture_var, *hair_texture_options, style="TMenubutton")
hair_texture_menu.pack()

# Set up scalp texture option menu
panel4 = Label(root, image=images["scalp_texture"])
panel4.pack()
scalp_texture_label = tk.Label(root, text="Q3) What is the texture of your scalp?", font=label_font, bg=bg_color)
scalp_texture_label.pack()
scalp_texture_menu = ttk.OptionMenu(root, scalp_texture_var, *scalp_texture_options, style="TMenubutton")
scalp_texture_menu.pack()

# ////////////////////////////////////////SOLUTIONS/////////////////////////////////////////////////////////////////////////////////////////////////////////////#

solutions = {
    "Straight": {
        "Fine": {
            "Normal": {
                "solution": "Shampoo & Conditioner once a week",
            },
            "Oily": {
                "solution": "Serum once a week",
                "url": "https://www.amazon.in/hz/wishlist/ls/195699WKONHJ3?ref_=wl_share "
            },
            "Dry": {
                "solution": "Oil once every three days",
                "url": "https://www.amazon.in/hz/wishlist/ls/TJJBENFY2OGF?ref_=wl_share  "
            }
        },
        "Medium": {
            "Normal": {
                "solution": "Shampoo & Conditioner 3 times a week",
                "url": "https://www.amazon.in/hz/wishlist/ls/J59I9OSPGH2A?ref_=wl_share  "
            },
            "Oily": {
                "solution": "Serum once every two days",
                "url": "https://www.amazon.in/hz/wishlist/ls/J59I9OSPGH2A?ref_=wl_share  "
            },
            "Dry": {
                "solution": "Oil once every two days",
                "url": "https://www.amazon.in/hz/wishlist/ls/TJJBENFY2OGF?ref_=wl_share"
            }
        },
        "Coarse": {
            "Normal": {
                "solution": "Shampoo & Conditioner after every two days /n ",
                "url": "https://www.amazon.in/hz/wishlist/ls/J59I9OSPGH2A?ref_=wl_share  "
            },
            "Oily": {
                "solution": "Serum every other day",
                "url": "https://www.amazon.in/hz/wishlist/ls/J59I9OSPGH2A?ref_=wl_share "
            },
            "Dry": {
                "solution": "Oil everyday",
                "url": "https://www.amazon.in/hz/wishlist/ls/TJJBENFY2OGF?ref_=wl_share"
            }
        }      
    },
#////////////////////////////////////////////////////////////////////////////////////////////////#  

    "Wavy": {
      "Fine": {
            "Normal": {
                "solution": "Shampoo & Conditioner once a week",
            },
            "Oily": {
                "solution": "Serum once a week",
                "url": "https://www.amazon.in/hz/wishlist/ls/FTLS412YQRU4?ref_=list_d_wl_lfu_nav_11 "
            },
            "Dry": {
                "solution": "Oil once every three days",
                "url": "https://www.amazon.in/hz/wishlist/ls/15TNL0SUYFSU1?ref_=wl_share  "
            }
        },
        "Medium": {
            "Normal": {
                "solution": "Shampoo & Conditioner 3 times a week",
            },
            "Oily": {
                "solution": "Serum once every two days",
                "url": "https://www.amazon.in/hz/wishlist/ls/FTLS412YQRU4?ref_=list_d_wl_lfu_nav_11"
            },
            "Dry": {
                "solution": "Oil once every two days",
                "url": "https://www.amazon.in/hz/wishlist/ls/15TNL0SUYFSU1?ref_=wl_share "
            }
        },
        "Coarse": {
            "Normal": {
                "solution": "Shampoo & Conditioner after every two days",
            },
            "Oily": {
                "solution": "Serum every other day",
                "url": "https://www.amazon.in/hz/wishlist/ls/FTLS412YQRU4?ref_=list_d_wl_lfu_nav_11"
            },
            "Dry": {
                "solution": "Oil everyday",
                "url": "https://www.amazon.in/hz/wishlist/ls/15TNL0SUYFSU1?ref_=wl_share"
            }
        }
        
    },
#////////////////////////////////////////////////////////////////////////////////////////////////#    


    "Curly": {
        "Fine": {
            "Normal": {
                "solution": "Shampoo & Conditioner once a week",
            },
            "Oily": {
                "solution": "Serum once a week",
                "url": "https://www.amazon.in/hz/wishlist/ls/16OF46LL6X35I?ref_=wl_share   "
            },
            "Dry": {
                "solution": "Oil once every three days",
                "url": "https://www.amazon.in/hz/wishlist/ls/3HM4OJ6GDGPB2?ref_=wl_share  "
            }
        },
        "Medium": {
            "Normal": {
                "solution": "Shampoo & Conditioner 3 times a week",
                "url": " https://www.amazon.in/hz/wishlist/ls/9AUDV64CGVLF?ref_=wl_share"
            },
            "Oily": {
                "solution": "Serum once every two days",
                "url": " https://www.amazon.in/hz/wishlist/ls/16OF46LL6X35I?ref_=wl_share"
            },
            "Dry": {
                "solution": "Oil once every two days",
                "url": "https://www.amazon.in/hz/wishlist/ls/3HM4OJ6GDGPB2?ref_=wl_share"
            }
        },
        "Coarse": {
            "Normal": {
                "solution": "Use a smoothing serum to control frizz.",
            },
            "Oily": {
                "solution": "ADD SOLUTION.",
                "url": "https://www.amazon.in/hz/wishlist/ls/16OF46LL6X35I?ref_=wl_share"
            },
            "Dry": {
                "solution": "ADD SOLUTION.",
                "url": "https://www.amazon.in/hz/wishlist/ls/3HM4OJ6GDGPB2?ref_=wl_share"
            }
        }
    },
#////////////////////////////////////////////////////////////////////////////////////////////////#


    "Coily": {
        "Fine": {
            "Normal": {
                "solution": "Shampoo & Conditioner once a week",
            },
            "Oily": {
                "solution": "Serum once a week",
                "url": "https://www.amazon.in/hz/wishlist/ls/16OF46LL6X35I?ref_=wl_share  "
            },
            "Dry": {
                "solution": "Oil once every three days",
                "url": "https://www.amazon.in/hz/wishlist/ls/ACO42UJT0PMY?ref_=wl_share  "
            }
        },
        "Medium": {
            "Normal": {
                "solution": "Shampoo & Conditioner 3 times a week",
                "url": "https://www.amazon.com/product-url-straight-medium-normal"
            },
            "Oily": {
                "solution": "Serum once every two days",
                "url": "https://www.amazon.in/hz/wishlist/ls/16OF46LL6X35I?ref_=wl_share   "
            },
            "Dry": {
                "solution": "Oil once every two days",
                "url": "https://www.amazon.in/hz/wishlist/ls/ACO42UJT0PMY?ref_=wl_share "
            }
        },
        "Coarse": {
            "Normal": {
                "solution": "Shampoo & Conditioner after every two days",
                "url": "https://www.amazon.com/product-url-straight-coarse-normal"
            },
            "Oily": {
                "solution": "Serum every other day",
                "url": "https://www.amazon.in/hz/wishlist/ls/1084XEQOOJ81M?ref_=wl_share "
            },
            "Dry": {
                "solution": "Oil every day",
                "url": "https://www.amazon.in/hz/wishlist/ls/ACO42UJT0PMY?ref_=wl_share "
            }
        }
    }
}
def display_solution():
    hair_type = hair_type_var.get()
    hair_texture = hair_texture_var.get()
    scalp_texture = scalp_texture_var.get()

    selected_solution = solutions.get(hair_type, {}).get(hair_texture, {}).get(scalp_texture)
    solution = selected_solution.get("solution", "")
    url = selected_solution.get("url", "")

    # Create solution label
    solution_label = tk.Label(root, text=solution, font=label_font, bg="#cc92df", fg="white")
    solution_label.pack(pady=5)

    # Open URL in web browser
    if url:
        def open_url():
            webbrowser.open(url)

        url_button = tk.Button(root, text="Buy on Amazon", command=open_url)
        url_button.pack()

# Create button to display solution
solution_button = tk.Button(root, text="Show Solution", command=display_solution)
solution_button.pack()

root.mainloop()
