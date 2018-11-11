
.PHONY: all
all: CS685_Midterm_McKerley.pdf

CS685_HW1_McKerley.pdf: CS685_Midterm_McKerley.tex $(pdf_t_files)

include ../latex.mk
