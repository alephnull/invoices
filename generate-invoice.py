#! /usr/bin/env python

import sys
from string import Template
from datetime import date

class InvoiceNumber:
    def __init__(self, fname='invoice.last'):
        self.fname = fname
        try:
            self.latest = int(open(self.fname, encoding='utf-8').read().strip())
        except FileNotFoundError:
            print("Could not find {}, using invoice number 0.".format(self.fname),
            file=sys.stderr)
            
            self.latest = 0
        except ValueError:
            print("Could read value from {}, using invoice number 0.".format(self.fname),
            file=sys.stderr)
            self.latest = 0

    def incr(self, new_num='1'):
        with open(self.fname, 'w') as f:
            if new_num:
                f.write("{}".format(new_num))
            else:
                f.write("{}".format(self.latest+1))

def generate_invoice(tdata,
                     tfile='invoice.tmpl',
                     iname=date.today().strftime('%b-%Y.tex')):
    tmpl = Template(open(tfile, encoding='utf-8').read().strip())
    with open(iname, 'w') as f:
        f.write(tmpl.substitute(tdata))

    return iname

invn = InvoiceNumber()
tdata = dict(invoice_num = invn.latest+1,
             month = date.today().strftime('%B %Y'))
invf = generate_invoice(tdata)
print("Invoice generated: {}".format(invf))
invn.incr()
