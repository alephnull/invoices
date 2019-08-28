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

`make` will generate the invoice for the current month and link it
into `sent/`.

 | Target      | Action                             |
 | --------    | -------                            |
 | `gen`       | Will generate the TeX source file  |
 | `pdf`       | Will generate PDF given TeX source |
 | `clean`     | Remove XeTeX detritus              |
 | `realclean` | `clean` + PDFs                     |


## Hacking
`invoice.tmpl` is a Python `string` template. It requires `invoice_num` and `month` as template vars. 

Modify the template file to your needs. Change names, etc.

A file `invoice.last` is stored in current dir to keep track of invoice numbers.

## Credits
I hacked [mkropat/dapper-invoice](https://github.com/mkropat/dapper-invoice) to add a month based itemisation template. It isn't very pretty though the output looks nice.
