# Makefile
INVOICE_NAME := $(shell date '+%b-%Y')

all: gen pdf

gen: 
	python3 generate-invoice.py > $(INVOICE_NAME).tex

pdf: $(INVOICE_NAME).tex dapper-invoice.cls
	xelatex $(INVOICE_NAME).tex && xelatex $(INVOICE_NAME).tex #Twice for references
	ln $(INVOICE_NAME).pdf sent/$(INVOICE_NAME).pdf

install: dapper-invoice.cls
	mkdir -p "$$(kpsewhich -expand-var '$$TEXMFHOME')/tex/latex/base"
	cp -a $? "$$(kpsewhich -expand-var '$$TEXMFHOME')/tex/latex/base/"

uninstall:
	rm -f "$$(kpsewhich -expand-var '$$TEXMFHOME')/tex/latex/base/dapper-invoice.cls"

clean:
	rm -fv *.aux *.log *.out

realclean: clean
	rm -fv *.pdf *.tex

.PHONY : install uninstall clean realclean
