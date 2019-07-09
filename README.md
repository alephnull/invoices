# Generate invoices

## Requires
You need Python3 and XeTeX. TexLive is the probably your best bet.

## By hand
```
$ python3 generate-invoice.py
Could not find invoice.last, using invoice number 0.
Invoice generated: Jul-2019.tex
$ xelatex Jul-2019.tex && xelatex Jul-2019.tex # Twice for references
```

## Automation
Use the Makefile in the repo

## Hacking
`invoice.tmpl` is a Python `string` template. It requires `invoice_num` and `month` as template vars. 

Modify the template file to your needs. Change names, etc.

A file `invoice.last` is stored in current dir to keep track of invoice numbers.

## Credits
I shamelessly stole and hacked dapper-invoice from [mkropat/dapper-invoice](/mkropat/dapper-invoice) to add a month based itemisation template. It isn't very pretty though the output looks nice.

