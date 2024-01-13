from tkinter import *

#window
window = Tk()
window.title("BMI Calculate")
window.minsize(width=300,height=300)


#label
my_weight=Label(text="Enter your weight (kilogram).",font=('Arial',12,'normal'))
my_height=Label(text="Enter your height (meter).",font=('Arial',12,'normal'))
my_weight.grid(row=2,column=5)
my_height.grid(row=2,column=0)

#entry
weight_entry=Entry(width=20)
height_entry=Entry(width=20)
weight_entry.grid(row=3,column=5)
height_entry.grid(row=3,column=0)


#button
def clicked_button():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        result = weight / (height ** 2)
        print(result)
        if result < 18.5:
            underweight_label = Label(text=f'BMI: {result}, This is not normal, you should gain weight.',
                                      font=('Arial', 10, 'normal'))
            underweight_label.grid(row=8, column=3)
        elif 18.5 <= result < 24.9:
            normal_label = Label(text=f'BMI: {result}, This is normal.', font=('Arial', 10, 'normal'))
            normal_label.grid(row=8, column=3)
        elif 25.0 <= result < 29.9:
            overweight_label = Label(text=f'BMI: {result}, You are overweight, you should lose weight',
                                      font=('Arial', 10, 'normal'))
            overweight_label.grid(row=8, column=3)
        elif 30.0 <= result < 34.9:
            obese1_label = Label(text=f'BMI: {result}, You are obese, you have to lose weight urgently',
                                 font=('Arial', 10, 'normal'))
            obese1_label.grid(row=8, column=3)
        elif 35.0 <= result < 39.9:
            obese2_label = Label(text=f'BMI: {result}, You are obese, you have to lose weight urgently',
                                 font=('Arial', 10, 'normal'))
            obese2_label.grid(row=8, column=3)
        elif result >= 40.0:
            obese3_label = Label(text=f'BMI: {result}, You are obese, you have to lose weight urgently',
                                 font=('Arial', 10, 'normal'))
            obese3_label.grid(row=8, column=3)

    except ValueError:
        error_label = Label(text="Please enter valid numeric values for weight and height.",
                            font=('Arial', 10, 'normal'))
        error_label.grid(row=8, column=3)



my_button=Button(text="Calculate",command=clicked_button)
my_button.grid(row=6,column=3)






window.mainloop()