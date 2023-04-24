#####INCOMPLETE CODE- MAKE SCALP TEXTURE CHANGES IN ALL HAIR PROBLEMS SECTIONS############



import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Hair Quiz")
root.geometry("500x500")
root.config(bg="white")

# Set up fonts
title_font = ("Helvetica", 24, "bold")
label_font = ("Helvetica", 12)
optionmenu_font = ("Helvetica", 10)

# Set up background color
bg_color = "red"

# Set up hair type options
hair_type_options = ["Select your hair type","Straight", "Wavy", "Curly", "Coily"]
hair_type_var = tk.StringVar(root)
hair_type_var.set(hair_type_options[0])

# Set up hair texture options
hair_texture_options = ["Select your hair texture","Fine", "Medium", "Coarse"]
hair_texture_var = tk.StringVar(root)
hair_texture_var.set(hair_texture_options[0])

# Set up scalp texture options
scalp_texture_options = ["Select your scalp texture","Dry", "Normal", "Oily"]
scalp_texture_var = tk.StringVar(root)
scalp_texture_var.set(scalp_texture_options[0])

# Set up hair problem options
hair_problem_options = ["Select your hair problems","Frizz", "Breakage", "Dryness", "Dandruff"]
hair_problem_var = tk.StringVar(root)
hair_problem_var.set(hair_problem_options[0])

# Set up title label
title_label = tk.Label(root, text="Take the Hair Quiz!", font=title_font, bg=bg_color)
title_label.pack(pady=20)

# Set up hair type option menu
hair_type_label = tk.Label(root, text="Q1)What is your hair type?", font=label_font, bg=bg_color)
hair_type_label.pack()
hair_type_menu = ttk.OptionMenu(root, hair_type_var, *hair_type_options, style="TMenubutton")
hair_type_menu.pack(pady=10)

# Set up hair texture option menu
hair_texture_label = tk.Label(root, text="Q2)What is the texture of your hair?", font=label_font, bg=bg_color)
hair_texture_label.pack()
hair_texture_menu = ttk.OptionMenu(root, hair_texture_var, *hair_texture_options, style="TMenubutton")
hair_texture_menu.pack(pady=10)

# Set up scalp texture option menu
scalp_texture_label = tk.Label(root, text="Q3)What is the texture of your scalp?", font=label_font, bg=bg_color)
scalp_texture_label.pack()
scalp_texture_menu = ttk.OptionMenu(root, scalp_texture_var, *scalp_texture_options, style="TMenubutton")
scalp_texture_menu.pack(pady=10)

# Set up hair problem option menu
hair_problem_label = tk.Label(root, text="Q4)What hair problems do you face?", font=label_font, bg=bg_color)
hair_problem_label.pack()
hair_problem_menu = ttk.OptionMenu(root, hair_problem_var, *hair_problem_options, style="TMenubutton")
hair_problem_menu.pack(pady=10)

# Set up function to display the solution
def display_solution():
    hair_type = hair_type_var.get()
    hair_texture = hair_texture_var.get()
    scalp_texture = scalp_texture_var.get()
    hair_problem = hair_problem_var.get()

#################################################FRIZZ####################################################
    if hair_problem == "Frizz": 

    #CHOICES#
        if hair_type == "Straight": 
         if hair_texture == "Fine": 
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
             if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
             if scalp_texture == "Dry":
                 solution = "ADD SOLUTION." 
         if hair_texture == "Medium":
            if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
            solution = "Use a normal smoothing serum to control frizz"
         if hair_texture == "Coarse":
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
             
#/////////////////////////////////////////////////////////////////////////////////////////////////////#
        if hair_type == "Wavy":       
         if hair_texture == "Fine": 
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
             if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
             if scalp_texture == "Dry":
                 solution = "ADD SOLUTION." 
         if hair_texture == "Medium":
            if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
            solution = "Use a normal smoothing serum to control frizz"
         if hair_texture == "Coarse":
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
#/////////////////////////////////////////////////////////////////////////////////////////////////////#
        if hair_type == "Curly":
         if hair_texture == "Fine": 
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
             if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
             if scalp_texture == "Dry":
                 solution = "ADD SOLUTION." 
         if hair_texture == "Medium":
            if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
            solution = "Use a normal smoothing serum to control frizz"
         if hair_texture == "Coarse":
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."  
#/////////////////////////////////////////////////////////////////////////////////////////////////////#
        if hair_type == "Coily":
         if hair_texture == "Fine": 
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
             if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
             if scalp_texture == "Dry":
                 solution = "ADD SOLUTION." 
         if hair_texture == "Medium":
            if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
            solution = "Use a normal smoothing serum to control frizz"
         if hair_texture == "Coarse":
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."

 #--------------------------------------------BREAKAGE-------------------------------------------------#
    if hair_problem == "Breakage":
      if hair_type == "Straight":
         if hair_texture == "Fine": 
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
             if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
             if scalp_texture == "Dry":
                 solution = "ADD SOLUTION." 
         if hair_texture == "Medium":
            if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
            solution = "Use a normal smoothing serum to control frizz"
         if hair_texture == "Coarse":
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
             
#/////////////////////////////////////////////////////////////////////////////////////////////////////#            
      if hair_type == "Wavy":
         if hair_texture == "Fine": 
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
             if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
             if scalp_texture == "Dry":
                 solution = "ADD SOLUTION." 
         if hair_texture == "Medium":
            if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
            solution = "Use a normal smoothing serum to control frizz"
         if hair_texture == "Coarse":
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
#/////////////////////////////////////////////////////////////////////////////////////////////////////#
      if hair_type == "Curly":
         if hair_texture == "Fine": 
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
             if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
             if scalp_texture == "Dry":
                 solution = "ADD SOLUTION." 
         if hair_texture == "Medium":
            if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
            solution = "Use a normal smoothing serum to control frizz"
         if hair_texture == "Coarse":
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
 #/////////////////////////////////////////////////////////////////////////////////////////////////////#     
      if hair_type == "Curly":
        if hair_texture == "Fine": 
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
             if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
             if scalp_texture == "Dry":
                 solution = "ADD SOLUTION." 
        if hair_texture == "Medium":
            if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
            solution = "Use a normal smoothing serum to control frizz"
        if hair_texture == "Coarse":
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
#--------------------------------------------DRYNESS-------------------------------------------------#
    if hair_problem == "Dryness":
     if hair_texture == "Fine": 
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
             if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
             if scalp_texture == "Dry":
                 solution = "ADD SOLUTION." 
    if hair_texture == "Medium":
            if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
            solution = "Use a normal smoothing serum to control frizz"
    if hair_texture == "Coarse":
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
#/////////////////////////////////////////////////////////////////////////////////////////////////////#
    if hair_type == "Wavy":       
     if hair_texture == "Fine": 
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
             if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
             if scalp_texture == "Dry":
                 solution = "ADD SOLUTION." 
    if hair_texture == "Medium":
            if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
            solution = "Use a normal smoothing serum to control frizz"
    if hair_texture == "Coarse":
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
#/////////////////////////////////////////////////////////////////////////////////////////////////////#
    if hair_type == "Curly":        
     if hair_texture == "Fine": 
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
             if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
             if scalp_texture == "Dry":
                 solution = "ADD SOLUTION." 
    if hair_texture == "Medium":
            if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
            solution = "Use a normal smoothing serum to control frizz"
    if hair_texture == "Coarse":
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
#/////////////////////////////////////////////////////////////////////////////////////////////////////#
    if hair_type == "Curly":        
     if hair_texture == "Fine": 
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
             if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
             if scalp_texture == "Dry":
                 solution = "ADD SOLUTION." 
    if hair_texture == "Medium":
            if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
            solution = "Use a normal smoothing serum to control frizz"
    if hair_texture == "Coarse":
             if scalp_texture == "Normal": 
              solution = "Use a smoothing serum to control frizz." 
              if scalp_texture == "Oily":
                 solution = "ADD SOLUTION." 
              if scalp_texture == "Dry":
                 solution = "ADD SOLUTION."
#/////////////////////////////////////////////////////////////////////////////////////////////////////#

    # Create solution label
    solution_label = tk.Label(root, text=solution, font=label_font, bg="red", fg="white")
    solution_label.pack(pady=20)      
    solution_label.pack(pady=20)

#Set up solution button

solution_button = tk.Button(root, text="Submit", command=display_solution, bg="red", fg="white", font=label_font)
solution_button.pack(pady=20)
        
  

root.mainloop()