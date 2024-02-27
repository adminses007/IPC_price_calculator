import tkinter as tk
from tkinter import *
import random
from tkinter import font

bg_color = "#ADD8E6"
fg_color = "white"
lbl_color = 'white'

def calculate_total():
    def get_entry_value(entry):
        value = entry.get()
        if value.isdigit():
            return int(value)
        else:
            return 0

    total_1 = get_entry_value(entry_1) * get_entry_value(entry_2)
    entry_3.delete(0, tk.END)
    entry_3.insert(0, str(total_1) + "Ks")

    total_4 = get_entry_value(entry_4) * get_entry_value(entry_5)
    entry_6.delete(0, tk.END)
    entry_6.insert(0, str(total_4) + "Ks")

    total_7 = get_entry_value(entry_7) * get_entry_value(entry_8)
    entry_9.delete(0, tk.END)
    entry_9.insert(0, str(total_7) + "Ks")

    total_10 = get_entry_value(entry_10) * get_entry_value(entry_11)
    entry_12.delete(0, tk.END)
    entry_12.insert(0, str(total_10) + "Ks")

    total_13 = get_entry_value(entry_13) * get_entry_value(entry_14)
    entry_15.delete(0, tk.END)
    entry_15.insert(0, str(total_13) + "Ks")

    total_16 = get_entry_value(entry_16) * get_entry_value(entry_17)
    entry_18.delete(0, tk.END)
    entry_18.insert(0, str(total_16) + "Ks")

    total_19 = get_entry_value(entry_19) * get_entry_value(entry_20)
    entry_21.delete(0, tk.END)
    entry_21.insert(0, str(total_19) + "Ks")

    total_22 = get_entry_value(entry_22) * get_entry_value(entry_23)
    entry_24.delete(0, tk.END)
    entry_24.insert(0, str(total_22) + "Ks")

    total_25 = get_entry_value(entry_25) * get_entry_value(entry_26)
    entry_27.delete(0, tk.END)
    entry_27.insert(0, str(total_25) + "Ks")

    total_28 = get_entry_value(entry_28) * get_entry_value(entry_29)
    entry_30.delete(0, tk.END)
    entry_30.insert(0, str(total_28) + "Ks")

    total_31 = get_entry_value(entry_31) * get_entry_value(entry_32)
    entry_33.delete(0, tk.END)
    entry_33.insert(0, str(total_31) + "Ks")

    total_34 = get_entry_value(entry_34) * get_entry_value(entry_35)
    entry_36.delete(0, tk.END)
    entry_36.insert(0, str(total_34) + "Ks")

    total_37 = get_entry_value(entry_37) * get_entry_value(entry_38)
    entry_39.delete(0, tk.END)
    entry_39.insert(0, str(total_37) + "Ks")

    total_40 = get_entry_value(entry_40) * get_entry_value(entry_41)
    entry_42.delete(0, tk.END)
    entry_42.insert(0, str(total_40) + "Ks")

    total_43 = get_entry_value(entry_43) * get_entry_value(entry_44)
    entry_45.delete(0, tk.END)
    entry_45.insert(0, str(total_43) + "Ks")

    total_46 = get_entry_value(entry_46) * get_entry_value(entry_47)
    entry_48.delete(0, tk.END)
    entry_48.insert(0, str(total_46) + "Ks")

    total_49 = get_entry_value(entry_49) * get_entry_value(entry_50)
    entry_51.delete(0, tk.END)
    entry_51.insert(0, str(total_49) + "Ks")

    total_52 = get_entry_value(entry_52) * get_entry_value(entry_53)
    entry_54.delete(0, tk.END)
    entry_54.insert(0, str(total_52) + "Ks")

    total_55 = get_entry_value(entry_55) * get_entry_value(entry_56)
    entry_57.delete(0, tk.END)
    entry_57.insert(0, str(total_55) + "Ks")

    total_58 = get_entry_value(entry_58) * get_entry_value(entry_59)
    entry_60.delete(0, tk.END)
    entry_60.insert(0, str(total_58) + "Ks")

    total_61 = get_entry_value(entry_61) * get_entry_value(entry_62)
    entry_63.delete(0, tk.END)
    entry_63.insert(0, str(total_61) + "Ks")

    total_64 = get_entry_value(entry_64) * get_entry_value(entry_65)
    entry_66.delete(0, tk.END)
    entry_66.insert(0, str(total_64) + "Ks")

    total = total_1 + total_4 + total_7 + total_10 + total_13 + total_16 + total_19 + total_22 + total_25 + total_28 + total_31 \
            + total_34 + total_37 + total_40 + total_43 + total_46 + total_49 + total_52 + total_55 + total_58 + total_61 \
            + total_64
    total_label.config(text="Total Price：" + str(total) + "Ks", font=label_font,bg=bg_color)

def generate_report():
    def get_entry_value(entry):
        value = entry.get()
        if value.isdigit():
            return int(value)
        else:
            return 0

    report_window = tk.Toplevel(root)
    report_window.title("Report")

    screen_width = 500
    screen_height = 400
    report_window.geometry("{}x{}+{}+{}".format(screen_width, screen_height,
                                                (report_window.winfo_screenwidth() - screen_width) // 2,
                                                (report_window.winfo_screenheight() - screen_height) // 2))

    report_text = tk.Text(report_window, width=90, height=40)
    custom_font = font.Font(size=12)
    report_text.pack()

    center_tag = "center"
    report_text.tag_configure(center_tag, justify="center")

    report_text.insert(END, "                    MR.COLOUR TECHNOLOGY\n", "big_font")
    report_text.insert(END, "     09-254405744.09-975185524. 110st*53st*54st.Mandalay\n", "big_font")
    report_text.tag_configure("big_font", font=custom_font)
    report_text.insert(END, "\n=====================================================", center_tag)
    report_text.insert(END, "\nProduct                         Qty              Price", center_tag)
    report_text.insert(END, "\n=====================================================", center_tag)

    def bill_area(entry_value, name):
        if entry_value != 0:
            if name == "mout":
                # selected_value = var_checkbox_group_1.get()
                report_text.insert(END,
                                   f"\nM IPC4MP-A(Out)           {entry_value}              {entry_value * get_entry_value(entry_1)}Ks",
                                   center_tag)
            if name == "min":
                report_text.insert(END,
                                   f"\nM IPC4MP-A(In)            {entry_value}              {entry_value * get_entry_value(entry_4)}Ks",
                                   center_tag)
            if name == "jout":
                report_text.insert(END,
                                   f"\nJ IPC4MP-A(In)            {entry_value}              {entry_value * get_entry_value(entry_7)}Ks",
                                   center_tag)
            if name == "jin":
                report_text.insert(END,
                                   f"\nJ IPC4MP-A(In)            {entry_value}              {entry_value * get_entry_value(entry_10)}Ks",
                                   center_tag)
            if name == "360in":
                report_text.insert(END,
                                   f"\nFE IPC3MP-A(In)           {entry_value}              {entry_value * get_entry_value(entry_13)}Ks",
                                   center_tag)
            if name == "pws":
                report_text.insert(END,
                                   f"\nPower Supply             {entry_value}              {entry_value * get_entry_value(entry_16)}Ks",
                                   center_tag)
            if name == "st":
                report_text.insert(END,
                                   f"\nStands                   {entry_value}              {entry_value * get_entry_value(entry_19)}Ks",
                                   center_tag)
            if name == "nvr":
                report_text.insert(END,
                                   f"\nNVR                      {entry_value}              {entry_value * get_entry_value(entry_22)}Ks",
                                   center_tag)
            if name == "hdd":
                report_text.insert(END,
                                   f"\nStorage                  {entry_value}              {entry_value * get_entry_value(entry_25)}Ks",
                                   center_tag)
            if name == "cab":
                report_text.insert(END,
                                   f"\nNetwork Cable            {entry_value}              {entry_value * get_entry_value(entry_28)}Ks",
                                   center_tag)
            if name == "44":
                report_text.insert(END,
                                   f"\nJoin Box 4x4             {entry_value}              {entry_value * get_entry_value(entry_31)}Ks",
                                   center_tag)
            if name == "66":
                report_text.insert(END,
                                   f"\nJoin Box 6x6             {entry_value}              {entry_value * get_entry_value(entry_34)}Ks",
                                   center_tag)
            if name == "4k":
                report_text.insert(END,
                                   f"\nHDMI 4K Cable            {entry_value}              {entry_value * get_entry_value(entry_37)}Ks",
                                   center_tag)
            if name == "2p":
                report_text.insert(END,
                                   f"\nAC 2 Pin                 {entry_value}              {entry_value * get_entry_value(entry_40)}Ks",
                                   center_tag)
            if name == "camin":
                report_text.insert(END,
                                   f"\nCamera install           {entry_value}              {entry_value * get_entry_value(entry_43)}Ks",
                                   center_tag)
            if name == "cabin":
                report_text.insert(END,
                                   f"\nCable install            {entry_value}              {entry_value * get_entry_value(entry_46)}Ks",
                                   center_tag)
            if name == "swtin":
                report_text.insert(END,
                                   f"\nSwitch install           {entry_value}              {entry_value * get_entry_value(entry_49)}Ks",
                                   center_tag)
            if name == "5po":
                report_text.insert(END,
                                   f"\n5 Port Switch            {entry_value}              {entry_value * get_entry_value(entry_52)}Ks",
                                   center_tag)
            if name == "8po":
                report_text.insert(END,
                                   f"\n8 Port Switch            {entry_value}              {entry_value * get_entry_value(entry_55)}Ks",
                                   center_tag)
            if name == "wicamo":
                report_text.insert(END,
                                   f"\nWi-Fi Camera (OUT)       {entry_value}              {entry_value * get_entry_value(entry_58)}Ks",
                                   center_tag)
            if name == "wicami":
                report_text.insert(END,
                                   f"\nWi-Fi Camera (IN)        {entry_value}              {entry_value * get_entry_value(entry_61)}Ks",
                                   center_tag)
            if name == "rout":
                report_text.insert(END,
                                   f"\nWi-Fi Router             {entry_value}              {entry_value * get_entry_value(entry_64)}Ks",
                                   center_tag)
    total = 0
    entry_1_value = get_entry_value(entry_2)
    bill_area(entry_1_value, "mout")
    entry_4_value = get_entry_value(entry_5)
    bill_area(entry_4_value, "min")
    entry_7_value = get_entry_value(entry_8)
    bill_area(entry_7_value, "jout")
    entry_10_value = get_entry_value(entry_11)
    bill_area(entry_10_value, "jin")
    entry_13_value = get_entry_value(entry_14)
    bill_area(entry_13_value, "360in")
    entry_16_value = get_entry_value(entry_17)
    bill_area(entry_16_value, "pws")
    entry_19_value = get_entry_value(entry_20)
    bill_area(entry_19_value, "st")
    entry_22_value = get_entry_value(entry_23)
    bill_area(entry_22_value, "nvr")
    entry_25_value = get_entry_value(entry_26)
    bill_area(entry_25_value, "hdd")
    entry_28_value = get_entry_value(entry_29)
    bill_area(entry_28_value, "cab")
    entry_31_value = get_entry_value(entry_32)
    bill_area(entry_31_value, "44")
    entry_34_value = get_entry_value(entry_35)
    bill_area(entry_34_value, "66")
    entry_37_value = get_entry_value(entry_38)
    bill_area(entry_37_value, "4k")
    entry_40_value = get_entry_value(entry_41)
    bill_area(entry_40_value, "2p")
    entry_43_value = get_entry_value(entry_44)
    bill_area(entry_43_value, "camin")
    entry_46_value = get_entry_value(entry_47)
    bill_area(entry_46_value, "cabin")
    entry_49_value = get_entry_value(entry_50)
    bill_area(entry_49_value, "swtin")
    entry_52_value = get_entry_value(entry_53)
    bill_area(entry_52_value, "5po")
    entry_55_value = get_entry_value(entry_56)
    bill_area(entry_55_value, "8po")
    entry_58_value = get_entry_value(entry_59)
    bill_area(entry_58_value, "wicamo")
    entry_61_value = get_entry_value(entry_62)
    bill_area(entry_61_value, "wincami")
    entry_64_value = get_entry_value(entry_65)
    bill_area(entry_64_value, "rout")

    total_1 = get_entry_value(entry_1) * get_entry_value(entry_2)
    entry_3.delete(0, tk.END)
    entry_3.insert(0, str(total_1) + "Ks")

    total_4 = get_entry_value(entry_4) * get_entry_value(entry_5)
    entry_6.delete(0, tk.END)
    entry_6.insert(0, str(total_4) + "Ks")

    total_7 = get_entry_value(entry_7) * get_entry_value(entry_8)
    entry_9.delete(0, tk.END)
    entry_9.insert(0, str(total_7) + "Ks")

    total_10 = get_entry_value(entry_10) * get_entry_value(entry_11)
    entry_12.delete(0, tk.END)
    entry_12.insert(0, str(total_10) + "Ks")

    total_13 = get_entry_value(entry_13) * get_entry_value(entry_14)
    entry_15.delete(0, tk.END)
    entry_15.insert(0, str(total_13) + "Ks")

    total_16 = get_entry_value(entry_16) * get_entry_value(entry_17)
    entry_18.delete(0, tk.END)
    entry_18.insert(0, str(total_16) + "Ks")

    total_19 = get_entry_value(entry_19) * get_entry_value(entry_20)
    entry_21.delete(0, tk.END)
    entry_21.insert(0, str(total_19) + "Ks")

    total_22 = get_entry_value(entry_22) * get_entry_value(entry_23)
    entry_24.delete(0, tk.END)
    entry_24.insert(0, str(total_22) + "Ks")

    total_25 = get_entry_value(entry_25) * get_entry_value(entry_26)
    entry_27.delete(0, tk.END)
    entry_27.insert(0, str(total_25) + "Ks")

    total_28 = get_entry_value(entry_28) * get_entry_value(entry_29)
    entry_30.delete(0, tk.END)
    entry_30.insert(0, str(total_28) + "Ks")

    total_31 = get_entry_value(entry_31) * get_entry_value(entry_32)
    entry_33.delete(0, tk.END)
    entry_33.insert(0, str(total_31) + "Ks")

    total_34 = get_entry_value(entry_34) * get_entry_value(entry_35)
    entry_36.delete(0, tk.END)
    entry_36.insert(0, str(total_34) + "Ks")

    total_37 = get_entry_value(entry_37) * get_entry_value(entry_38)
    entry_39.delete(0, tk.END)
    entry_39.insert(0, str(total_37) + "Ks")

    total_40 = get_entry_value(entry_40) * get_entry_value(entry_41)
    entry_42.delete(0, tk.END)
    entry_42.insert(0, str(total_40) + "Ks")

    total_43 = get_entry_value(entry_43) * get_entry_value(entry_44)
    entry_45.delete(0, tk.END)
    entry_45.insert(0, str(total_43) + "Ks")

    total_46 = get_entry_value(entry_46) * get_entry_value(entry_47)
    entry_48.delete(0, tk.END)
    entry_48.insert(0, str(total_46) + "Ks")

    total_49 = get_entry_value(entry_49) * get_entry_value(entry_50)
    entry_51.delete(0, tk.END)
    entry_51.insert(0, str(total_49) + "Ks")

    total_52 = get_entry_value(entry_52) * get_entry_value(entry_53)
    entry_54.delete(0, tk.END)
    entry_54.insert(0, str(total_52) + "Ks")

    total_55 = get_entry_value(entry_55) * get_entry_value(entry_56)
    entry_57.delete(0, tk.END)
    entry_57.insert(0, str(total_55) + "Ks")

    total_58 = get_entry_value(entry_58) * get_entry_value(entry_59)
    entry_60.delete(0, tk.END)
    entry_60.insert(0, str(total_58) + "Ks")

    total_61 = get_entry_value(entry_61) * get_entry_value(entry_62)
    entry_63.delete(0, tk.END)
    entry_63.insert(0, str(total_61) + "Ks")

    total_64 = get_entry_value(entry_64) * get_entry_value(entry_65)
    entry_66.delete(0, tk.END)
    entry_66.insert(0, str(total_64) + "Ks")

    total = total_1 + total_4 + total_7 + total_10 + total_13 + total_16 + total_19 + total_22 + total_25 + total_28 + total_31 \
            + total_34 + total_37 + total_40 + total_43 + total_46 + total_49 + total_52 + total_55 + total_58 + total_61 \
            + total_64
    total_label.config(text="Total Price：" + str(total) + "Ks", font=label_font,bg=bg_color)



    report_text.insert(END, "\n=====================================================", center_tag)
    report_text.insert(END, f"\n                     Total Price:{total}Ks", center_tag)

def exit_application():
    root.quit()

def clear_entries():
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END)
    entry_3.delete(0, tk.END)
    entry_4.delete(0, tk.END)
    entry_5.delete(0, tk.END)
    entry_6.delete(0, tk.END)
    entry_7.delete(0, tk.END)
    entry_8.delete(0, tk.END)
    entry_9.delete(0, tk.END)
    entry_10.delete(0, tk.END)
    entry_11.delete(0, tk.END)
    entry_12.delete(0, tk.END)
    entry_13.delete(0, tk.END)
    entry_14.delete(0, tk.END)
    entry_15.delete(0, tk.END)
    entry_16.delete(0, tk.END)
    entry_17.delete(0, tk.END)
    entry_18.delete(0, tk.END)
    entry_19.delete(0, tk.END)
    entry_20.delete(0, tk.END)
    entry_21.delete(0, tk.END)
    entry_22.delete(0, tk.END)
    entry_23.delete(0, tk.END)
    entry_24.delete(0, tk.END)
    entry_25.delete(0, tk.END)
    entry_26.delete(0, tk.END)
    entry_27.delete(0, tk.END)
    var_checkbox_group_1.set(None)
    var_checkbox_group_2.set(None)
    var_checkbox_group_3.set(None)
    var_checkbox_group_4.set(None)
    var_checkbox_group_5.set(None)
    var_checkbox_group_6.set(None)
    var_checkbox_group_7.set(None)
    var_checkbox_group_8.set(None)
    var_checkbox_group_9.set(None)
    var_checkbox_group_10.set(None)
    total_label.config(text="Total Price:", font=label_font)
    entry_28.delete(0, tk.END)
    entry_29.delete(0, tk.END)
    entry_30.delete(0, tk.END)
    entry_31.delete(0, tk.END)
    entry_32.delete(0, tk.END)
    entry_33.delete(0, tk.END)
    entry_34.delete(0, tk.END)
    entry_35.delete(0, tk.END)
    entry_36.delete(0, tk.END)
    entry_37.delete(0, tk.END)
    entry_38.delete(0, tk.END)
    entry_39.delete(0, tk.END)
    entry_40.delete(0, tk.END)
    entry_41.delete(0, tk.END)
    entry_42.delete(0, tk.END)
    entry_43.delete(0, tk.END)
    entry_44.delete(0, tk.END)
    entry_45.delete(0, tk.END)
    entry_46.delete(0, tk.END)
    entry_47.delete(0, tk.END)
    entry_48.delete(0, tk.END)
    entry_49.delete(0, tk.END)
    entry_50.delete(0, tk.END)
    entry_51.delete(0, tk.END)
    entry_52.delete(0, tk.END)
    entry_53.delete(0, tk.END)
    entry_54.delete(0, tk.END)
    entry_55.delete(0, tk.END)
    entry_56.delete(0, tk.END)
    entry_57.delete(0, tk.END)
    entry_58.delete(0, tk.END)
    entry_59.delete(0, tk.END)
    entry_60.delete(0, tk.END)
    entry_61.delete(0, tk.END)
    entry_62.delete(0, tk.END)
    entry_63.delete(0, tk.END)
    entry_64.delete(0, tk.END)
    entry_65.delete(0, tk.END)
    entry_66.delete(0, tk.END)


root = tk.Tk()
root.title("Quickly calculate quotes")
root.configure(bg="#ADD8E6")

var_checkbox_group_1 = tk.StringVar()
var_checkbox_group_2 = tk.StringVar()
var_checkbox_group_3 = tk.StringVar()
var_checkbox_group_4 = tk.StringVar()
var_checkbox_group_5 = tk.StringVar()
var_checkbox_group_6 = tk.StringVar()
var_checkbox_group_7 = tk.StringVar()
var_checkbox_group_8 = tk.StringVar()
var_checkbox_group_9 = tk.StringVar()
var_checkbox_group_10 = tk.StringVar()

label_1 = tk.Label(root, text="Mercury IPC4MP-A(Outdoor):", relief=FLAT,bg=bg_color)
label_1.grid(row=0, column=0)
entry_1 = tk.Entry(root, width=8, relief=GROOVE)
entry_1.grid(row=0, column=1)
label_2 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_2.grid(row=0, column=2)
entry_2 = tk.Entry(root, width=3, relief=GROOVE)
entry_2.grid(row=0, column=3)
label_3 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_3.grid(row=0, column=4)
entry_3 = tk.Entry(root, width=10, relief=GROOVE)
entry_3.grid(row=0, column=5)

label_4 = tk.Label(root, text="Mercury IPC4MP-A(Indoor):", relief=FLAT,bg=bg_color)
label_4.grid(row=1, column=0)
entry_4 = tk.Entry(root, width=8, relief=GROOVE)
entry_4.grid(row=1, column=1)
label_5 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_5.grid(row=1, column=2)
entry_5 = tk.Entry(root, width=3, relief=GROOVE)
entry_5.grid(row=1, column=3)
label_6 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_6.grid(row=1, column=4)
entry_6 = tk.Entry(root, width=10, relief=GROOVE)
entry_6.grid(row=1, column=5)

label_7 = tk.Label(root, text="JOOAN IPC4MP-A(Outdoor):", relief=FLAT,bg=bg_color)
label_7.grid(row=2, column=0)
entry_7 = tk.Entry(root, width=8, relief=GROOVE)
entry_7.grid(row=2, column=1)
label_8 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_8.grid(row=2, column=2)
entry_8 = tk.Entry(root, width=3, relief=GROOVE)
entry_8.grid(row=2, column=3)
label_9 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_9.grid(row=2, column=4)
entry_9 = tk.Entry(root, width=10, relief=GROOVE)
entry_9.grid(row=2, column=5)

label_10 = tk.Label(root, text="JOOAN IPC4MP-A(Indoor):", relief=FLAT,bg=bg_color)
label_10.grid(row=3, column=0)
entry_10 = tk.Entry(root, width=8, relief=GROOVE)
entry_10.grid(row=3, column=1)
label_11 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_11.grid(row=3, column=2)
entry_11 = tk.Entry(root, width=3, relief=GROOVE)
entry_11.grid(row=3, column=3)
label_12 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_12.grid(row=3, column=4)
entry_12 = tk.Entry(root, width=10, relief=GROOVE)
entry_12.grid(row=3, column=5)

label_13 = tk.Label(root, text="Mercury IPC4MP-A(360°)", relief=FLAT,bg=bg_color)
label_13.grid(row=4, column=0)
entry_13 = tk.Entry(root, width=8, relief=GROOVE)
entry_13.grid(row=4, column=1)
label_14 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_14.grid(row=4, column=2)
entry_14 = tk.Entry(root, width=3, relief=GROOVE)
entry_14.grid(row=4, column=3)
label_15 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_15.grid(row=4, column=4)
entry_15 = tk.Entry(root, width=10, relief=GROOVE)
entry_15.grid(row=4, column=5)

label_16 = tk.Label(root, text="Power Supply", relief=FLAT,bg=bg_color)
label_16.grid(row=5, column=0)
radio_button_1_1 = tk.Radiobutton(root, text="12v~2a", variable=var_checkbox_group_1, value="12v~2a", relief=FLAT,bg=bg_color)
radio_button_1_1.grid(row=5, column=9,sticky="w")
radio_button_1_2 = tk.Radiobutton(root, text="12v~20a", variable=var_checkbox_group_1, value="12v~20a", relief=FLAT,bg=bg_color)
radio_button_1_2.grid(row=5, column=11,sticky="w")
radio_button_1_3 = tk.Radiobutton(root, text="12v~30a", variable=var_checkbox_group_1, value="12v~30a", relief=FLAT,bg=bg_color)
radio_button_1_3.grid(row=5, column=13,sticky="w")
entry_16 = tk.Entry(root, width=8, relief=GROOVE)
entry_16.grid(row=5, column=1)
label_17 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_17.grid(row=5, column=2)
entry_17 = tk.Entry(root, width=3, relief=GROOVE)
entry_17.grid(row=5, column=3)
label_18 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_18.grid(row=5, column=4)
entry_18 = tk.Entry(root, width=10, relief=GROOVE)
entry_18.grid(row=5, column=5)

label_19 = tk.Label(root, text="Camera Stands", relief=FLAT,bg=bg_color)
label_19.grid(row=6, column=0)
entry_19 = tk.Entry(root, width=8, relief=GROOVE)
entry_19.grid(row=6, column=1)
label_20 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_20.grid(row=6, column=2)
entry_20 = tk.Entry(root, width=3, relief=GROOVE)
entry_20.grid(row=6, column=3)
label_21 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_21.grid(row=6, column=4)
entry_21 = tk.Entry(root, width=10, relief=GROOVE)
entry_21.grid(row=6, column=5)

label_22 = tk.Label(root, text="NVR", relief=FLAT,bg=bg_color)
label_22.grid(row=7, column=0)
radio_button_2_1 = tk.Radiobutton(root, text="8CHANNEL", variable=var_checkbox_group_2, value="8CHANNEL", relief=FLAT,bg=bg_color)
radio_button_2_1.grid(row=7, column=9,sticky="w")
radio_button_2_2 = tk.Radiobutton(root, text="16CHANNEL", variable=var_checkbox_group_2, value="16CHANNEL", relief=FLAT,bg=bg_color)
radio_button_2_2.grid(row=7, column=11,sticky="w")
radio_button_2_3 = tk.Radiobutton(root, text="32CHANNEL", variable=var_checkbox_group_2, value="32CHANNEL", relief=FLAT,bg=bg_color)
radio_button_2_3.grid(row=7, column=13,sticky="w")
entry_22 = tk.Entry(root, width=8, relief=GROOVE)
entry_22.grid(row=7, column=1)
label_23 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_23.grid(row=7, column=2)
entry_23 = tk.Entry(root, width=3, relief=GROOVE)
entry_23.grid(row=7, column=3)
label_24 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_24.grid(row=7, column=4)
entry_24 = tk.Entry(root, width=10, relief=GROOVE)
entry_24.grid(row=7, column=5)

label_25 = tk.Label(root, text="Storage", relief=FLAT,bg=bg_color)
label_25.grid(row=8, column=0)
radio_button_3_1 = tk.Radiobutton(root, text="2TB", variable=var_checkbox_group_3, value="2TB", relief=FLAT,bg=bg_color)
radio_button_3_1.grid(row=8, column=9,sticky="w")
radio_button_3_2 = tk.Radiobutton(root, text="4TB", variable=var_checkbox_group_3, value="4TB", relief=FLAT,bg=bg_color)
radio_button_3_2.grid(row=8, column=11,sticky="w")
radio_button_3_3 = tk.Radiobutton(root, text="6TB", variable=var_checkbox_group_3, value="6TB", relief=FLAT,bg=bg_color)
radio_button_3_3.grid(row=8, column=13,sticky="w")
radio_button_3_4 = tk.Radiobutton(root, text="8TB", variable=var_checkbox_group_3, value="8TB", relief=FLAT,bg=bg_color)
radio_button_3_4.grid(row=8, column=15,sticky="w")
entry_25 = tk.Entry(root, width=8, relief=GROOVE)
entry_25.grid(row=8, column=1)
label_26 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_26.grid(row=8, column=2)
entry_26 = tk.Entry(root, width=3, relief=GROOVE)
entry_26.grid(row=8, column=3)
label_27 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_27.grid(row=8, column=4)
entry_27 = tk.Entry(root, width=10, relief=GROOVE)
entry_27.grid(row=8, column=5)

label_28 = tk.Label(root, text="Network Cable Cat5e P+D", relief=FLAT,bg=bg_color)
label_28.grid(row=9, column=0)
entry_28 = tk.Entry(root, width=8, relief=GROOVE)
entry_28.grid(row=9, column=1)
label_29 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_29.grid(row=9, column=2)
entry_29 = tk.Entry(root, width=3, relief=GROOVE)
entry_29.grid(row=9, column=3)
label_30 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_30.grid(row=9, column=4)
entry_30 = tk.Entry(root, width=10, relief=GROOVE)
entry_30.grid(row=9, column=5)

label_31 = tk.Label(root, text="Join Box 4x4", relief=FLAT,bg=bg_color)
label_31.grid(row=10, column=0)
entry_31 = tk.Entry(root, width=8, relief=GROOVE)
entry_31.grid(row=10, column=1)
label_32 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_32.grid(row=10, column=2)
entry_32 = tk.Entry(root, width=3, relief=GROOVE)
entry_32.grid(row=10, column=3)
label_33 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_33.grid(row=10, column=4)
entry_33 = tk.Entry(root, width=10, relief=GROOVE)
entry_33.grid(row=10, column=5)

label_34 = tk.Label(root, text="Join Box 6x6", relief=FLAT,bg=bg_color)
label_34.grid(row=11, column=0)
entry_34 = tk.Entry(root, width=8, relief=GROOVE)
entry_34.grid(row=11, column=1)
label_35 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_35.grid(row=11, column=2)
entry_35 = tk.Entry(root, width=3, relief=GROOVE)
entry_35.grid(row=11, column=3)
label_36 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_36.grid(row=11, column=4)
entry_36 = tk.Entry(root, width=10, relief=GROOVE)
entry_36.grid(row=11, column=5)

label_37 = tk.Label(root, text="HDMI 4K Cable", relief=FLAT,bg=bg_color)
label_37.grid(row=12, column=0)
radio_button_4_1 = tk.Radiobutton(root, text="4K 1.5Meter", variable=var_checkbox_group_4, value="4K 1.5Meter",
                                  relief=FLAT,bg=bg_color)
radio_button_4_1.grid(row=12, column=9,sticky="w")
radio_button_4_2 = tk.Radiobutton(root, text="4K 3Meter", variable=var_checkbox_group_4, value="4K 3Meter", relief=FLAT,bg=bg_color)
radio_button_4_2.grid(row=12, column=11,sticky="w")
radio_button_4_3 = tk.Radiobutton(root, text="4K 5Meter", variable=var_checkbox_group_4, value="4K 5Meter", relief=FLAT,bg=bg_color)
radio_button_4_3.grid(row=12, column=13,sticky="w")
entry_37 = tk.Entry(root, width=8, relief=GROOVE)
entry_37.grid(row=12, column=1)
label_38 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_38.grid(row=12, column=2)
entry_38 = tk.Entry(root, width=3, relief=GROOVE)
entry_38.grid(row=12, column=3)
label_39 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_39.grid(row=12, column=4)
entry_39 = tk.Entry(root, width=10, relief=GROOVE)
entry_39.grid(row=12, column=5)

label_40 = tk.Label(root, text="Power 2 Pin", relief=FLAT,bg=bg_color)
label_40.grid(row=13, column=0)
entry_40 = tk.Entry(root, width=8, relief=GROOVE)
entry_40.grid(row=13, column=1)
label_41 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_41.grid(row=13, column=2)
entry_41 = tk.Entry(root, width=3, relief=GROOVE)
entry_41.grid(row=13, column=3)
label_42 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_42.grid(row=13, column=4)
entry_42 = tk.Entry(root, width=10, relief=GROOVE)
entry_42.grid(row=13, column=5)

label_43 = tk.Label(root, text="Camera installation", relief=FLAT,bg=bg_color)
label_43.grid(row=14, column=0)
radio_button_5_1 = tk.Radiobutton(root, text="Super installers", variable=var_checkbox_group_5,
                                  value="Super installers", relief=FLAT,bg=bg_color)
radio_button_5_1.grid(row=14, column=9,sticky="w")
radio_button_5_2 = tk.Radiobutton(root, text="Pro installers", variable=var_checkbox_group_5, value="Pro installers",
                                  relief=FLAT,bg=bg_color)
radio_button_5_2.grid(row=14, column=11,sticky="w")
entry_43 = tk.Entry(root, width=8, relief=GROOVE)
entry_43.grid(row=14, column=1)
label_44 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_44.grid(row=14, column=2)
entry_44 = tk.Entry(root, width=3, relief=GROOVE)
entry_44.grid(row=14, column=3)
label_45 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_45.grid(row=14, column=4)
entry_45 = tk.Entry(root, width=10, relief=GROOVE)
entry_45.grid(row=14, column=5)

label_46 = tk.Label(root, text="Cable installation", relief=FLAT,bg=bg_color)
label_46.grid(row=15, column=0)
radio_button_6_1 = tk.Radiobutton(root, text="Super installers", variable=var_checkbox_group_6,
                                  value="Super installers", relief=FLAT,bg=bg_color)
radio_button_6_1.grid(row=15, column=9,sticky="w")
radio_button_6_2 = tk.Radiobutton(root, text="Pro installers", variable=var_checkbox_group_6, value="Pro installers",
                                  relief=FLAT,bg=bg_color)
radio_button_6_2.grid(row=15, column=11,sticky="w")
entry_46 = tk.Entry(root, width=8, relief=GROOVE)
entry_46.grid(row=15, column=1)
label_47 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_47.grid(row=15, column=2)
entry_47 = tk.Entry(root, width=3, relief=GROOVE)
entry_47.grid(row=15, column=3)
label_48 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_48.grid(row=15, column=4)
entry_48 = tk.Entry(root, width=10, relief=GROOVE)
entry_48.grid(row=15, column=5)

label_49 = tk.Label(root, text="Switch installation", relief=FLAT,bg=bg_color)
label_49.grid(row=16, column=0)
radio_button_7_1 = tk.Radiobutton(root, text="Super installers", variable=var_checkbox_group_7,
                                  value="Super installers", relief=FLAT,bg=bg_color)
radio_button_7_1.grid(row=16, column=9,sticky="w")
radio_button_7_2 = tk.Radiobutton(root, text="Pro installers", variable=var_checkbox_group_7, value="Pro installers",
                                  relief=FLAT,bg=bg_color)
radio_button_7_2.grid(row=16, column=11,sticky="w")
entry_49 = tk.Entry(root, width=8, relief=GROOVE)
entry_49.grid(row=16, column=1)
label_50 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_50.grid(row=16, column=2)
entry_50 = tk.Entry(root, width=3, relief=GROOVE)
entry_50.grid(row=16, column=3)
label_51 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_51.grid(row=16, column=4)
entry_51 = tk.Entry(root, width=10, relief=GROOVE)
entry_51.grid(row=16, column=5)

label_52 = tk.Label(root, text="5 Port Switch 1G", relief=FLAT,bg=bg_color)
label_52.grid(row=17, column=0)
entry_52 = tk.Entry(root, width=8, relief=GROOVE)
entry_52.grid(row=17, column=1)
label_53 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_53.grid(row=17, column=2)
entry_53 = tk.Entry(root, width=3, relief=GROOVE)
entry_53.grid(row=17, column=3)
label_54 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_54.grid(row=17, column=4)
entry_54 = tk.Entry(root, width=10, relief=GROOVE)
entry_54.grid(row=17, column=5)

label_55 = tk.Label(root, text="8 Port Switch 1G", relief=FLAT,bg=bg_color)
label_55.grid(row=18, column=0)
entry_55 = tk.Entry(root, width=8, relief=GROOVE)
entry_55.grid(row=18, column=1)
label_56 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_56.grid(row=18, column=2)
entry_56 = tk.Entry(root, width=3, relief=GROOVE)
entry_56.grid(row=18, column=3)
label_57 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_57.grid(row=18, column=4)
entry_57 = tk.Entry(root, width=10, relief=GROOVE)
entry_57.grid(row=18, column=5)

label_58 = tk.Label(root, text="Wi-Fi Camera(Outdoor)", relief=FLAT,bg=bg_color)
label_58.grid(row=19, column=0)
radio_button_8_1 = tk.Radiobutton(root, text="Tenda CH7", variable=var_checkbox_group_8, value="Tenda CH7", relief=FLAT,bg=bg_color)
radio_button_8_1.grid(row=19, column=9,sticky="w")
radio_button_8_2 = tk.Radiobutton(root, text="Dual 5MP", variable=var_checkbox_group_8, value="Dual 5MP", relief=FLAT,bg=bg_color)
radio_button_8_2.grid(row=19, column=11,sticky="w")
radio_button_8_3 = tk.Radiobutton(root, text="XVV Pro 2K", variable=var_checkbox_group_8, value="XVV Pro 2K",
                                  relief=FLAT,bg=bg_color)
radio_button_8_3.grid(row=19, column=13,sticky="w")
radio_button_8_4 = tk.Radiobutton(root, text="Robot 3MP", variable=var_checkbox_group_8, value="Robot 3MP", relief=FLAT,bg=bg_color)
radio_button_8_4.grid(row=19, column=15,sticky="w")
entry_58 = tk.Entry(root, width=8, relief=GROOVE)
entry_58.grid(row=19, column=1)
label_59 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_59.grid(row=19, column=2)
entry_59 = tk.Entry(root, width=3, relief=GROOVE)
entry_59.grid(row=19, column=3)
label_60 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_60.grid(row=19, column=4)
entry_60 = tk.Entry(root, width=10, relief=GROOVE)
entry_60.grid(row=19, column=5)

label_61 = tk.Label(root, text="Wi-Fi Camera(Indoor)", relief=FLAT,bg=bg_color)
label_61.grid(row=20, column=0)
radio_button_9_1 = tk.Radiobutton(root, text="Tenda CP7", variable=var_checkbox_group_9, value="Tenda CP7", relief=FLAT,bg=bg_color)
radio_button_9_1.grid(row=20, column=9,sticky="w")
radio_button_9_2 = tk.Radiobutton(root, text="Dual 5MP", variable=var_checkbox_group_9, value="Dual 5MP", relief=FLAT,bg=bg_color)
radio_button_9_2.grid(row=20, column=11,sticky="w")
radio_button_9_3 = tk.Radiobutton(root, text="360°Fish Eye", variable=var_checkbox_group_9, value="360°Fish Eye",
                                  relief=FLAT,bg=bg_color)
radio_button_9_3.grid(row=20, column=13,sticky="w")
radio_button_9_4 = tk.Radiobutton(root, text="Lamp 3MP", variable=var_checkbox_group_9, value="Lamp 3MP", relief=FLAT,bg=bg_color)
radio_button_9_4.grid(row=20, column=15,sticky="w")
entry_61 = tk.Entry(root, width=8, relief=GROOVE)
entry_61.grid(row=20, column=1)
label_62 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_62.grid(row=20, column=2)
entry_62 = tk.Entry(root, width=3, relief=GROOVE)
entry_62.grid(row=20, column=3)
label_63 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_63.grid(row=20, column=4)
entry_63 = tk.Entry(root, width=10, relief=GROOVE)
entry_63.grid(row=20, column=5)

label_64 = tk.Label(root, text="Wi-Fi Router", relief=FLAT,bg=bg_color)
label_64.grid(row=21, column=0)
radio_button_10_1 = tk.Radiobutton(root, text="2.4GHz", variable=var_checkbox_group_10, value="2.4GHz", relief=FLAT,bg=bg_color)
radio_button_10_1.grid(row=21, column=9,sticky="w")
radio_button_10_2 = tk.Radiobutton(root, text="2.4GHz & 5GHz", variable=var_checkbox_group_10, value="2.4GHz & 5GHz",
                                   relief=FLAT,bg=bg_color)
radio_button_10_2.grid(row=21, column=11,sticky="w")
entry_64 = tk.Entry(root, width=8, relief=GROOVE)
entry_64.grid(row=21, column=1)
label_65 = tk.Label(root, text="Qty:", relief=FLAT,bg=bg_color)
label_65.grid(row=21, column=2)
entry_65 = tk.Entry(root, width=3, relief=GROOVE)
entry_65.grid(row=21, column=3)
label_66 = tk.Label(root, text="=", relief=FLAT,bg=bg_color)
label_66.grid(row=21, column=4)
entry_66 = tk.Entry(root, width=10, relief=GROOVE)
entry_66.grid(row=21, column=5)

var_checkbox_group_1.set(None)
var_checkbox_group_2.set(None)
var_checkbox_group_3.set(None)
var_checkbox_group_4.set(None)
var_checkbox_group_5.set(None)
var_checkbox_group_6.set(None)
var_checkbox_group_7.set(None)
var_checkbox_group_8.set(None)
var_checkbox_group_9.set(None)
var_checkbox_group_10.set(None)

total_label = tk.Label(root, text="Total Price：", font=('Arial', 15),bg=bg_color)
total_label.grid(row=27, columnspan=6)

calculate_button = tk.Button(root, text="Calculate", command=calculate_total, width=15, height=2,bg=bg_color)
calculate_button.grid(row=32, columnspan=4, padx=7, pady=7)

clear_button = tk.Button(root, text="Clear", command=clear_entries, width=10, height=2,bg=bg_color)
clear_button.grid(row=32, column=2, columnspan=5)

exit_button = tk.Button(root, text="Exit", command=exit_application, width=10, height=2,bg=bg_color)
exit_button.grid(row=32, column=6, columnspan=22)

generate_report_button = tk.Button(root, text="Generate Report", command=generate_report, width=15, height=2,bg=bg_color)
generate_report_button.grid(row=32, column=9, columnspan=1)

label_font = ('Arial', 15)

label_4 = tk.Label(root, text="By  Tiger.Yang", relief=FLAT, font=('Arial', 12),bg=bg_color)

label_4.grid(row=32, column=15,sticky="s")

screen_width = 830
screen_height = 650
root.geometry("{}x{}+{}+{}".format(screen_width, screen_height,
                                   (root.winfo_screenwidth() - screen_width) // 2,
                                   (root.winfo_screenheight() - screen_height) // 2))

root.mainloop()
