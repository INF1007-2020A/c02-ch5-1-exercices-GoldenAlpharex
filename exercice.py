#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	TAX_RATE = 0.15

	# Calculer le sous-total (somme des items)
	sous_total = 0
	for item in data:
		sous_total += item[INDEX_QUANTITY] * item[INDEX_PRICE]

	# Calculer les taxes et total
	taxes = TAX_RATE * sous_total
	total = sous_total + taxes

	# Retourner la facture formattée (sous-total, taxes, total)
	result = name
	result += "\n" + f"SOUS-TOTAL {sous_total : >10.2f} $" # L'espace représente le caractère de remplissage dans "{sous_total : >10.2f}"
	result += "\n" + f"TAXES      {taxes : >10.2f} $"
	result += "\n" + f"TOTAL      {total : >10.2f} $"

	# Façon plus smart de le faire, donné par le prof.
	bill_data = [
		("SOUS-TOTAL", sous_total),
		("TAXES     ", taxes),
		("TOTAL     ", total)
	]
	result = name
	for d in bill_data:
		result += "\n" + f"{d[0]} {d[1] : >10.2f} $"
	
	return result


def format_number(number, num_decimal_digits):
	# Séparer la partie entière et la partie décimale
	decimal_part = abs(number) % 1.0
	whole_part = int(abs(number))
	# Formatter la partie décimale
	decimal_str = "." + str(int(round(decimal_part * 10**num_decimal_digits)))
	# decimal_str = f"{decimal_part:.{num_decimal_digits}f}"[1:] # version facile

	# Formatter la partie entière
	whole_part_str = ""
	while whole_part >= 1000:
		digits = whole_part % 1000
		digits_str = f" {digits :0>3}"
		whole_part_str = digits_str + whole_part_str
		whole_part //= 1000
	whole_part_str = str(whole_part) + whole_part_str

	# Concaténer les deux parties pour le return.
	return ("-" if number < 0 else "") + whole_part_str + decimal_str

def get_triangle(num_rows):
	BORDER_CHAR = "+"
	TRIANGLE_CHAR = "A"
	# Calcul de la longueur du milieu et définition de la bordure
	length_middle = 2 * num_rows - 1
	border_row = (length_middle + 2) * BORDER_CHAR
	result = border_row

	# Créer les lignes du triangle et les ajouter aux résultats
	for i in range (num_rows):
		triangle_chars = (i*2 + 1) * TRIANGLE_CHAR
		result += "\n" + f"{BORDER_CHAR}{triangle_chars : ^{length_middle}}{BORDER_CHAR}"

	# Ajout de la dernière bordure et renvoi du résultat.
	result += "\n" + border_row
	return result


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print("\n", "-------------", "\n")
	print(format_number(-12345.678, 2))

	print("\n", "-------------", "\n")
	print(get_triangle(2))
	print("\n")
	print(get_triangle(5))
