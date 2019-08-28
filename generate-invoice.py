#! /usr/bin/env python

import sys
from string import Template
from datetime import date

class InvoiceNumber:
    latest = fname = None
    def __init__(self, fname='invoice.last'):
        self.fname = fname
        try:
            with open(self.fname, encoding='utf-8') as f:
                self.latest = int(f.read().strip())
        except FileNotFoundError:
            sys.stderr.write("Could not find {}, using invoice number 0.\n".format(self.fname))
            self.latest = 0
        except ValueError:
            sys.stderr.write("Could read value from {}, using invoice number 0.\n".format(self.fname))
            self.latest = 0

    def incr(self):
        with open(self.fname, 'w', encoding='utf-8') as f:
            self.latest += 1
            sys.stderr.write("Writing {} to {}.\n".format(self.latest, self.fname))
            f.write("{}".format(self.latest))

def generate_invoice(tdata,
                     tfile='invoice.tmpl'):
    tmpl = Template(open(tfile, encoding='utf-8').read().strip())
    print(tmpl.substitute(tdata))

invn = InvoiceNumber()
tdata = dict(invoice_num = invn.latest+1,
             month = date.today().strftime('%B %Y'))
generate_invoice(tdata)
invn.incr()
